import random
from turtle import position
from PIL import Image
import os
import json

from asyncio import sleep
from aiocqhttp.exceptions import ActionFailed
from html2text import element_style

from hoshino import Service, priv, util, R
from hoshino.typing import CQEvent, MessageSegment
from hoshino.config import NICKNAME, RES_DIR
from hoshino.util import FreqLimiter, DailyNumberLimiter, pic2b64

from .config import *

if type(NICKNAME)!=list:
    NICKNAME=[NICKNAME]

lmt = DailyNumberLimiter(DAILY_LIMIT)

working_path = os.path.dirname(__file__)
res_dir = os.path.join(RES_DIR,'img','tarot')
# res_dir ='/root/HoshinoBot/hoshino/modules/tarot/assets/' #请修改为自己的assets path，注意windows斜杠转义
# res_dir ='C:\\Users\\Administrator\\HoshinoBot\\hoshino\\modules\\tarot\\assets\\' windows路径格式参考

card_data = json.load(open(os.path.join(working_path, "data.json"), encoding="utf-8"))

all_arcana=[str(x) for x in range(0,78)]

major_arcana=[str(x) for x in range(0,22)]

minor_arcana=[str(x) for x in range(22,78)]


sv_help='''
塔罗牌
[(@bot)塔罗牌/占卜 (牌阵号)] 使用指定牌阵进行一次塔罗牌占卜，未指定时使用默认牌阵
[塔罗牌牌阵] 查看可用的塔罗牌牌阵
[塔罗卡面列表] 查看可用的塔罗牌卡面
[切换塔罗牌卡面 (卡面号)] 切换本群所用塔罗牌卡面
[切换塔罗牌规则 (规则名)] 切换本群所用塔罗牌规则，可选：标准、仅大阿卡纳、仅小阿卡纳
[随机塔罗牌 (编号)] 欣赏一张随机塔罗牌及其信息，后附编号时可指定塔罗牌

'''.strip()

sv = Service('tarot', visible= True, enable_on_default= True, bundle='娱乐', help_=sv_help)

        
def group_init(gid):
    group_data[str(gid)] = { "deck": DEFUALT_DECK, "rule": DEFUALT_RULE }

def save_group_data():
    with open(os.path.join(working_path, "group_data.json"), "w", encoding="utf-8") as f:
        json.dump(group_data, f, ensure_ascii=False, indent=2)

try:
    group_data = json.load(open(os.path.join(working_path, "group_data.json"), encoding="utf-8"))
except FileNotFoundError:
    group_data = {}
    with open(os.path.join(working_path, "group_data.json"), 'w', encoding="utf-8") as f:
        json.dump({}, f, ensure_ascii=False, indent=2)


def generate_describe(key, pos, mode=0):
    delist=[f"{card_data[key]['name']}({card_data[key]['engname']})："]
    if key in major_arcana:
        delist.append(f"元素属性为{card_data[key]['info']['element']}，对应天体为{card_data[key]['info']['celestial']}；")
    elif key in minor_arcana:
        delist.append(f"元素属性为{card_data[key]['info']['element']}，代表色为{card_data[key]['info']['color']}；")
        delist.append(f"含义是{card_data[key]['info']['mean']}；")
    delist.append(f"关键词是{card_data[key]['info']['keyword']};\n")
    if mode==0:
        if pos == '正位':
            delist.append(f"正位时含义为：{card_data[key]['info']['describe']}。")
        else:
            delist.append(f"逆位时含义为：{card_data[key]['info']['reverse_describe']}。")
    else:
        delist.append(f"{card_data[key]['info']['content']};\n")
        delist.append(f"正位时含义为：{card_data[key]['info']['describe']}；\n")
        delist.append(f"逆位时含义为：{card_data[key]['info']['reverse_describe']}。")
    return '\n'.join(delist)

def gen_sample_pic(deck):
    deck_path = os.path.join(res_dir, "decks", decks_data[deck]['dir'])
    if os.path.exists(os.path.join(deck_path, 'sample.jpg')):
        sample = Image.open(os.path.join(deck_path, 'sample.jpg'))
        return sample
    p0=Image.open(os.path.join(deck_path, f'0.jpg'))
    sizey = int(p0.size[1]*300/p0.size[0])
    des = Image.new("RGB", (4 * 300, 6 * sizey), (0, 0, 0, 0))
    for key in major_arcana:
        path = os.path.join(deck_path, f'{key}.jpg')
        card = Image.open(path).convert("RGB").resize((300, sizey), Image.LANCZOS)
        x = int(key) % 4
        y = int(int(key) / 4)
        des.paste(card, (x * 300, y * sizey))
    des.save(os.path.join(deck_path, 'sample.jpg'))
    return des

spreads_rev={}
for sp in spreads_data:
    name=spreads_data[sp]['name']
    spreads_rev[name]=sp
    if name[-2:]=='牌阵':
        spreads_rev[name[:-2]]=sp


@sv.on_prefix(('塔罗牌','占卜','塔罗'), only_to_me=True)
async def tarot_act(bot, ev):
    gid = str(ev.group_id)
    if not gid in group_data:
        group_init(gid)
        save_group_data()
    uid = ev.user_id
    if not priv.check_priv(ev, priv.SUPERUSER):
        if not lmt.check(uid):
            await bot.send(ev, EXCEED_NOTICE, at_sender=True)
            return

    name = util.normalize_str(ev.message.extract_plain_text().strip())
    default=False
    if not name:
        spread=DEFUALT_SPREAD
        default=True
    else:
        if name in spreads_data:
            spread=name
        elif name in spreads_rev:
            spread=spreads_rev[name]
        else:
            await bot.send(ev,'未找到此牌阵……请确认输入是否正确')
            return

    rule = group_data[gid]['rule']
    if rule == 'all':
        card_used=all_arcana
    elif rule == 'major-only':
        card_used=major_arcana
    elif rule == 'minor-only':
        card_used=minor_arcana
    
    deck=group_data[gid]['deck']
    if decks_data[deck]["set"]=='major-only':
        card_used=major_arcana

    num=spreads_data[spread]['num']
    indices =random.sample(card_used, num)

    chain = []
    if default:
        await bot.send(ev, f'您未选择牌阵，将为您使用默认的{spreads_data[spread]["name"]}进行占卜……')

    await bot.send(ev,'请稍等，正在洗牌中……')

    msg=f'您使用的是{spreads_data[spread]["level"]}牌阵：{spreads_data[spread]["name"]}\n此牌阵使用{spreads_data[spread]["num"]}张塔罗牌，是一种{spreads_data[spread]["describe"]}。'
    chain = await chain_reply(bot, ev, chain, msg)
    
    if WITH_PIC:
        chain = await chain_reply(bot, ev, chain, R.img(f'tarot/spreads/{spreads_data[spread]["pic"]}').cqcode)

    for count in range(num):
        #sv.logger.info(f'第{count}轮')	
        card_key = indices[count]

        meaning_key = list(spreads_data[spread]["meaning"].keys())[count]
        meaning_value = spreads_data[spread]["meaning"][meaning_key]
        
        position = random.choice(['正位', '逆位'])

        msg=f'{meaning_key}：{meaning_value};\n\n您抽到了：{card_data[card_key]["name"]} ({position})'
        chain = await chain_reply(bot, ev, chain, msg)

        if WITH_PIC:
            img_path = os.path.join(res_dir, "decks", decks_data[deck]['dir'], f"{card_key}.jpg")
            img = Image.open(img_path)
            if position == '逆位':
                img=img.rotate(180)
            picmsg = str(MessageSegment.image(pic2b64(img)))
            chain = await chain_reply(bot, ev, chain, picmsg)

        msg=generate_describe(card_key, position)
        chain = await chain_reply(bot, ev, chain, msg)

    if CHAIN_REPLY:
        try:
            await bot.send_group_forward_msg(group_id=ev['group_id'], messages=chain)
            lmt.increase(uid)
            return
        except ActionFailed:
            await bot.send(ev,'结果发送失败，账号可能被风控……')
    lmt.increase(uid)


async def chain_reply(bot, ev, chain, msg):
    if not CHAIN_REPLY:
        await bot.send(ev, msg)
        return chain
    else:
        data = {
            "type": "node",
            "data": {
                    "name": str(NICKNAME[0]),
                    "user_id": str(ev.self_id),
                    "content": str(msg)
            }
        }
        chain.append(data)
        return chain


@sv.on_fullmatch(('查看塔罗牌卡面','查看塔罗卡面','塔罗牌卡面列表','塔罗卡面列表',))
async def show_decks(bot, ev):
    gid = str(ev.group_id)
    if not gid in group_data:
        group_init(gid)
        save_group_data()
    info=[f'目前有{len(decks_data)}种塔罗卡面主题可选，请使用[切换塔罗牌卡面 序号]命令选择要使用的卡面！\n\n']
    for deck in decks_data:
        info.append(deck)
        info.append(': ')
        info.append(decks_data[deck]['name'])
        if decks_data[deck]['set']=='complete':
            info.append(' (完整)')
        elif decks_data[deck]['set']=='major-only':
            info.append(' (仅大阿卡纳)')
        info.append('\n')
    await bot.send(ev, ''.join(info))


@sv.on_prefix(('切换塔罗牌卡面','切换塔罗卡面','设置塔罗牌卡面','设置塔罗卡面'))
async def chaneg_decks(bot, ev):
    gid = str(ev.group_id)
    if not gid in group_data:
        group_init(gid)
        save_group_data()
    name = util.normalize_str(ev.message.extract_plain_text().strip())
    if not name:
        await show_decks(bot, ev)
    else:
        if name in decks_data:
            group_data[gid]['deck']=name
            save_group_data()
            await bot.send(ev, f'本群卡面套组已变更为{decks_data[name]["name"]}！')
            if decks_data[name]["set"]=='major-only' and group_data[gid]['rule']!='major-only':
                await bot.send(ev, f'请注意，此卡面套组仅包含大阿卡纳牌，占卜时将自动使用仅大阿卡纳规则！')
            img = gen_sample_pic(name)
            picmsg = str(MessageSegment.image(pic2b64(img)))
            await bot.send(ev, picmsg)
        else:
            await bot.send(ev,'未找到此卡面编号……请确认输入是否正确')
            return

rule_set={'all':'标准', 'major_only':'仅大阿卡纳', 'minor_only':'仅小阿卡纳'}
rule_set_rev={'标准':'all', '仅大阿卡纳':'major_only', '仅小阿卡纳':'minor_only'}

@sv.on_prefix(('切换塔罗牌规则','切换塔罗规则','设置塔罗牌规则','设置塔罗规则'))
async def chaneg_rule(bot, ev):
    gid = str(ev.group_id)
    if not gid in group_data:
        group_init(gid)
        save_group_data()
    name = util.normalize_str(ev.message.extract_plain_text().strip())
    if not name:
        await bot.send(ev, f"请后附需切换的规则！\n目前规则：{rule_set[group_data[gid]['rule']]}；可选规则：{rule_set_rev.keys()}")
    else:
        if name in rule_set_rev.keys():
            group_data[gid]['rule']=rule_set_rev[name]
            save_group_data()
            await bot.send(ev, f'本群规则已变更为{name}！')
            if decks_data[name]["set"]=='major-only' and group_data[gid]['rule']!='major-only':
                await bot.send(ev, f'请注意，目前所用卡面套组仅包含大阿卡纳牌，占卜时将自动使用仅大阿卡纳规则！')
        else:
            await bot.send(ev,'未找到此规则……请确认输入是否正确')
            return


@sv.on_fullmatch(('查看塔罗牌牌阵','查看塔罗牌阵','塔罗牌牌阵','塔罗牌阵'))
async def show_spreads(bot, ev):
    gid = str(ev.group_id)
    if not gid in group_data:
        group_init(gid)
        save_group_data()
    info=[f'目前有{len(spreads_data)}种塔罗牌阵可用，请在占卜时使用序号选择要使用的牌阵！\n\n']
    for spread in spreads_data:
        info.append(spread)
        info.append(': ')
        info.append(spreads_data[spread]['name'])
        info.append('，')
        info.append(spreads_data[spread]['describe'])
        info.append('，')
        info.append(f"使用牌数{spreads_data[spread]['num']}张。")
        info.append('\n')
    await bot.send(ev, ''.join(info))


@sv.on_prefix(('随机塔罗牌','随机塔罗'))
async def random_tarot(bot, ev):
    gid = str(ev.group_id)
    if not gid in group_data:
        group_init(gid)
        save_group_data()
    name = util.normalize_str(ev.message.extract_plain_text().strip())

    deck=group_data[gid]['deck']
    if decks_data[deck]["set"]=='major-only':
        card_used=major_arcana
    elif decks_data[deck]["set"]=='complete':
        card_used=all_arcana

    if not name:
        key=random.choice(card_used)
    else:
        if name in card_used:
            key=name
        else:
            await bot.send(ev, '此卡号不在当前卡组内，将使用默认卡面……')
            deck='1'
            # key=random.choice(card_used)
    await bot.send(ev, R.img(f"tarot/decks/{decks_data[deck]['dir']}/{key}.jpg").cqcode)
    await bot.send(ev,generate_describe(key, '正位', mode=1))
