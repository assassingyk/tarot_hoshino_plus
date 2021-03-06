DEFUALT_DECK = '1'  # 默认使用卡组

DEFUALT_RULE = 'all'  # 默认规则， all：使用全卡组， major_only:仅使用大阿卡纳， minor_only:仅使用小阿卡纳

DEFUALT_SPREAD = '1'   # 默认使用牌阵

DAILY_LIMIT = 5   # 每日上限

EXCEED_NOTICE = f'您今天已经进行过{DAILY_LIMIT}次占卜了，请明早5点后再来~'   # 超额提示

WITH_PIC = True   # 是否带图，关闭可能可以减轻风控情况

CHAIN_REPLY = True   # 是否启用转发模式


#牌阵信息  name:牌阵名  num:牌阵卡数  pic:牌阵图片
spreads_data={
    "1": {
        "name": "身心灵牌阵",
        "num": 4,
        "level": "初级",
        "describe": "常用来测算每天的运势的牌阵，也可以用来占卜感情或分析某一事件对当事人的影响",
        "pic": "bms.jpg",
        "meaning": {
            "第一张牌": "代表着身体状况或事情对身体状况的影响",
            "第二张牌": "代表着心理状况或事件对心理的影响",
            "第三张牌": "代表着精神状态或事件对精神上的影响",
            "切牌": "表示问卜者主观的想法，或问卜当事人的特质"
        }
    },
    "2": {
        "name": "圣三角牌阵",
        "num": 3,
        "level": "初级",
        "describe": "适合非两难选择问题的牌阵，可占卜工作、学业、爱情以及运势",
        "pic": "triangle.jpg",
        "meaning": {
            "第一张牌": "代表你对过去事情所形成的原因以及经验所指",
            "第二张牌": "代表你当下面对问题的状态是什么样的",
            "第三张牌": "代表你未来可能会出现的情况的预测"
        }
    },
    "3": {
        "name": "难题牌阵",
        "num": 4,
        "level": "初级",
        "describe": "专门针对疑难问题所设计的牌阵，遇到不知如何是好的情况时，可以选择难题牌阵",
        "pic": "difficult.jpg",
        "meaning": {
            "第一张牌": "表示现今存在的状况",
            "第二张牌": "表示困难所导致的现实局面",
            "第三张牌": "表示困难可能有的解决方法",
            "切牌": "表示问卜者主观的想法，或问卜当事人的特质"
        }
    },
    "4": {
        "name": "平安扇牌阵",
        "num": 4,
        "level": "初级",
        "describe": "专门针对人际关系进行占卜的牌阵",
        "pic": "fan.jpg",
        "meaning": {
            "第一张牌": "表示当事人目前的人际关系状况",
            "第二张牌": "表示问卜当事人与对方结识的因缘",
            "第三张牌": "表示双方关系未来的发展趋势",
            "第四张牌": "表示对双方关系的结论"
        }
    },
    "5": {
        "name": "四要素展开法牌阵",
        "num": 4,
        "level": "初级",
        "describe": "为想了解如何解决问题的求问者提供解释的牌阵",
        "pic": "fourelements.jpg",
        "meaning": {
            "第一张牌": "代表火，火象征行动，提供给你行动上的建议",
            "第二张牌": "代表气，气象征言语、沟通，提供你言语上应该采取的对策",
            "第三张牌": "代表水，水象征情绪、感情，告诉你感情层次上，应该采取的态度为何",
            "第四张牌": "代表土，土象征实际物质、金钱，告诉你物质方面 (如金钱) 应该如何处理，才能彻底解决问题"
        }
    },
    "6": {
        "name": "恋人三角牌阵",
        "num": 4,
        "level": "初级",
        "describe": "专门针对恋爱的状况以及出现的问题进行占卜的牌阵",
        "pic": "lover.jpg",
        "meaning": {
            "第一张牌": "代表了问卜当事人本身的状况，也包括内心的情绪",
            "第二张牌": "代表恋爱对方的情况，同样包括对方的内心想法",
            "第三张牌": "表示目前问卜者与恋爱对象的恋爱关系状况",
            "第四张牌": "表示对方关系未来的发展情况"
        }
    },
    "7": {
        "name": "吉普赛十字牌阵",
        "num": 5,
        "level": "中级",
        "describe": "针对爱情问题进行分析的塔罗占卜牌阵",
        "pic": "cross.jpg",
        "meaning": {
            "第一张牌": "表示的是问卜者目前的心态",
            "第二张牌": "表示的是问卜者现在的状况",
            "第三张牌": "显示的是问卜者采取的举措",
            "第四张牌": "显示的是恋爱双方周围的情势，即环境",
            "第五张牌": "表示两人关系未来的状况"
        }
    },
    "8": {
        "name": "二选一牌阵",
        "num": 6,
        "level": "中级",
        "describe": "专门对两难选择问题进行判断，并进而推出最佳方案的一种牌阵",
        "pic": "2t1.jpg",
        "meaning": {
            "第一张牌": "表示问卜者现在的情况",
            "第二张牌": "表示做出第一种选择后会出现的情况",
            "第三张牌": "表示做出第一种选择所造成的影响",
            "第四张牌": "表示做出第二种选择后会出现的情况",
            "第五张牌": "表示第二种选择所造成的影响",
            "切牌": "表示问卜者主观的想法，或问卜当事人的特质"
        }
    },
    "9": {
        "name": "马蹄牌阵",
        "num": 6,
        "level": "中级",
        "describe": "对我们身处的环境及其变化做出描述从而了解自身处境的牌阵",
        "pic": "horseshoe.jpg",
        "meaning": {
            "第一张牌": "表示目前的状况",
            "第二张牌": "表示环境变化中可以预知的情况",
            "第三张牌": "表示环境变化中本人无法预知的情况",
            "第四张牌": "表示事情即将有的发展",
            "第五张牌": "表示如果延续第四张牌的发展趋势，将会出现的结果",
            "切牌": "表示问卜者主观的想法，或问卜当事人的特质"
        }
    },
    "10": {
        "name": "行星牌阵",
        "num": 7,
        "level": "中级",
        "describe": "分析一个人目前在各方面的状态的塔罗牌阵",
        "pic": "planet.jpg",
        "meaning": {
            "第一张牌": "代表月，月亮掌管的是求问者的家人状况与家庭环境",
            "第二张牌": "代表土星。土星掌管的是人的智能、精神状况",
            "第三张牌": "代表金星。金星掌管的是人的智能、精神状况",
            "第四张牌": "代表太阳。太阳掌管的是情感",
            "第五张牌": "代表火星。火星指示求问者和其对手的竞争情况，或是潜在的意见分裂",
            "第六张牌": "代表木星。木星象征着物质的获取，或是任何人际关系、精神性物质的获得",
            "第七张牌": "代表水星。水星掌管贸易、商业工作和学习的状况"
        }
    },
    "11": {
        "name": "六芒星牌阵",
        "num": 7,
        "level": "中级",
        "describe": "用来理解事情的来龙去脉，在此基础上选择方法解决问题的塔罗牌阵",
        "pic": "hex.jpg",
        "meaning": {
            "第一张牌": "代表过去，表示事情已经发生的部分",
            "第二张牌": "代表现在，表示正在进行的事情",
            "第三张牌": "代表未来，表示事情尚未发展到的阶段",
            "第四张牌": "代表原因，表示事情发生的原因",
            "第五张牌": "代表环境，表示影响事情的环境因素",
            "第六张牌": "代表对策，表示应对事情的方法",
            "切牌": "表示问卜者主观的想法，或问卜当事人的特质"
        }
    },
    "12": {
        "name": "凯尔特十字牌阵",
        "num": 10,
        "level": "高级",
        "describe": "针对某一个问题的各个层面去判断，并且解读过去、现在和未来事情发展的预测的牌阵",
        "pic": "celtic.jpg",
        "meaning": {
            "第一张牌": "代表问题的现状",
            "第二张牌": "代表对问题的阻碍或者帮助",
            "第三张牌": "代表求问者对问题的理想、未来目标",
            "第四张牌": "代表问题过去的成因、状况",
            "第五张牌": "代表问题的最近过去状况(通常在过去两、三个月内)",
            "第六张牌": "代表问题的最近未来发展(未来两、三个月内)",
            "第七张牌": "代表着求问者本身的现状",
            "第八张牌": "代表周围环境对问题的影响，以及周围的人对这个问题的看法",
            "第九张牌": "代表求问者的能力",
            "第十张牌": "代表问题的最终结果"
        }
    },
    "13": {
        "name": "维纳斯牌阵",
        "num": 8,
        "level": "高级",
        "describe": "专门针对爱情问题进行占卜的牌阵",
        "pic": "venus.jpg",
        "meaning": {
            "第一张牌": "表示问卜当事人对问题的看法",
            "第二张牌": "表示爱情另一方对问卜者的心态",
            "第三张牌": "表示问卜当事人对对方的影响",
            "第四张牌": "表示对方对问卜当事人的影响",
            "第五张牌": "表示双方之间的某些障碍",
            "第六张牌": "表示恋情的结果",
            "第七张牌": "表示问卜当事人以后回首这件事时的想法和心情",
            "第八张牌": "表示对方以后的想法和心情"
        }
    },
    "14": {
        "name": "黄道十二宫牌阵",
        "num": 13,
        "level": "高级",
        "describe": "与占星术相结合，对某人、某事或某物在某种状况下进行细节分析的牌阵",
        "pic": "zodiac.jpg",
        "meaning": {
            "第一张牌": "白羊宫，表示事物的本质、个人因素及人的外貌",
            "第二张牌": "金牛宫，表示事物的物质基础、财务状况和人的价值观",
            "第三张牌": "双子宫，表示沟通、学习和人的表达能力",
            "第四张牌": "巨蟹宫，表示事物的根源、本地的事物和家庭的事情",
            "第五张牌": "狮子宫，表示玩乐、恋爱和自我表现",
            "第六张牌": "室女宫，表示劳动、工作和健康",
            "第七张牌": "天平宫，表示婚姻、合作和他人的关系",
            "第八张牌": "天蝎宫，表示共有的财务、投资和性",
            "第九张牌": "射手宫，表示目标、信仰和外国的事物",
            "第十张牌": "摩羯宫，表示对外的形象、地位和事业",
            "第十一张牌": "宝瓶宫，表示朋友、群体和理想",
            "第十二张牌": "双鱼宫，表示小人、隐藏的事物和个人的心理层面",
            "切牌": "表示问卜者主观的想法，或问卜当事人的特质"
        }
    }
}


#卡面信息  set:complete,major-only  dir:卡面目录名

decks_data={
    '1':{
        'name':'经典塔罗(rider-waite)',
        'set':'complete',
        'dir':'smith-waite'
    },
    '2':{
        'name':'中世纪塔罗',
        'set':'complete',
        'dir':'cary-yale-visconti'
    },
    '3':{
        'name':'文艺复兴塔罗',
        'set':'complete',
        'dir':'renaissance'
    },
    '4':{
        'name':'占星学塔罗',
        'set':'complete',
        'dir':'celestial'
    },
    '5':{
        'name':'简约塔罗',
        'set':'complete',
        'dir':'astro'
    },
    '6':{
        'name':'bilibili塔罗 (by 影法师)',
        'set':'complete',
        'dir':'bilibili'
    },
    '7':{
        'name':'猫meme',
        'set':'major-only',
        'dir':'cat'
    },
}
