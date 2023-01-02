import requests, time, json
from khl import Bot, Message, EventTypes, Event
from khl.card import Card, CardMessage, Module, Element, Types, Struct

bot = Bot(token = '')
info_channel = ''

def server_info(port):
    try:
        Query = requests.get('http://43.143.135.75:18888/index.php?method=xPaw&host=teawaste.cn&port=' + str(port) + '&type=info', timeout = 2)
    except requests.exceptions.RequestException as error:
        print(error)
        return False
    try:
        Query_player = requests.get('http://43.143.135.75:18888/index.php?method=xPaw&host=teawaste.cn&port=' + str(port) + '&type=player', timeout = 2)
    except requests.exceptions.RequestException as error:
        print(error)
        return False
    Query.encoding = 'utf-8'
    Query_player.encoding = 'utf-8'
    if Query.text != '' and Query_player.text != '':
        print(Query.text)
        Json = json.loads(Query.text)
        Info = '服务器:\n' + Json['HostName'] + '\n当前地图: ' + Json['Map'] + '\n[' + str(Json['Players']) + '/' + str(Json['MaxPlayers']) + ']\n' + str(Json['Bots']) + '机器人'
        #print(Query_player.text)
        Json_Array = json.loads(Query_player.text)
        if Query_player.text != '[]' and Query_player.text != '[[]]':
            iplayer = 0
            store_list = ''
            for Json in Json_Array:
                #iplayer = iplayer + 1
                if Json['Name'] == '':
                    #store_list = store_list + '\n' + str(iplayer) + '. FakeClient'
                    continue
                else:
                    iplayer = iplayer + 1
                    #print(str(iplayer) + '.' + Json['Name'])
                    store_list = store_list + '\n' + str(iplayer) + '. ' + Json['Name']
            #print(store_list)
            #print(Info)
            return Info + '\n--------------------------------------------------' + store_list
        else:
            return Info
    else:
        print('查询结果异常')
        return False

@bot.command(name='info')
async def info(msg: Message):
    await msg.ctx.channel.send(
        CardMessage(
            Card(
                Module.Header('Tea社区'),
                Module.Context('请选择要查询的服务器'),
                Module.ActionGroup(
                    Element.Button('魔怔鸟狙①服', 's_30001', Types.Click.RETURN_VAL),
                    Element.Button('魔怔鸟狙②服', 's_30002', Types.Click.RETURN_VAL)
                ),
                Module.ActionGroup(
                    Element.Button('魔怔鸟狙③服', 's_30003', Types.Click.RETURN_VAL),
                    Element.Button('鸟狙爆头①服', 's_30004', Types.Click.RETURN_VAL)
                ),
                Module.ActionGroup(
                    Element.Button('干拉魔怔①服', 's_30005', Types.Click.RETURN_VAL),
                    Element.Button('干拉魔怔②服', 's_30006', Types.Click.RETURN_VAL)
                ),
                Module.ActionGroup(
                    Element.Button('纯净魔怔①服', 's_30007', Types.Click.RETURN_VAL),
                    Element.Button('纯净魔怔②服', 's_30008', Types.Click.RETURN_VAL)
                ),
                Module.ActionGroup(
                    Element.Button('混战魔怔①服', 's_30009', Types.Click.RETURN_VAL),
                    Element.Button('混战魔怔②服', 's_30010', Types.Click.RETURN_VAL)
                ),
                Module.Divider(),
                Module.Section('加入我们'),
                Module.ActionGroup(
                    Element.Button('QQ群', 'https://jq.qq.com/?_wv=1027&k=OHFSQSD6', Types.Click.LINK)
                )
            )
        )
    )

@bot.command(name='join')
async def join(msg: Message):
    await msg.ctx.channel.send(
        CardMessage(
            Card(
                Module.Header('Tea社区'),
                Module.Context('请选择要加入的服务器'),
                Module.ActionGroup(
                    Element.Button('魔怔鸟狙①服', 'http://43.143.135.75:18888/steam.php?Host=teawaste.cn&Port=30001', Types.Click.LINK),
                    Element.Button('魔怔鸟狙②服', 'http://43.143.135.75:18888/steam.php?Host=teawaste.cn&Port=30002', Types.Click.LINK)
                ),
                Module.ActionGroup(
                    Element.Button('魔怔鸟狙③服', 'http://43.143.135.75:18888/steam.php?Host=teawaste.cn&Port=30003', Types.Click.LINK),
                    Element.Button('鸟狙爆头①服', 'http://43.143.135.75:18888/steam.php?Host=teawaste.cn&Port=30004', Types.Click.LINK)
                ),
                Module.ActionGroup(
                    Element.Button('干拉魔怔①服', 'http://43.143.135.75:18888/steam.php?Host=teawaste.cn&Port=30005', Types.Click.LINK),
                    Element.Button('干拉魔怔②服', 'http://43.143.135.75:18888/steam.php?Host=teawaste.cn&Port=30006', Types.Click.LINK)
                ),
                Module.ActionGroup(
                    Element.Button('纯净魔怔①服', 'http://43.143.135.75:18888/steam.php?Host=teawaste.cn&Port=30007', Types.Click.LINK),
                    Element.Button('纯净魔怔②服', 'http://43.143.135.75:18888/steam.php?Host=teawaste.cn&Port=30008', Types.Click.LINK)
                ),
                Module.ActionGroup(
                    Element.Button('混战魔怔①服', 'http://43.143.135.75:18888/steam.php?Host=teawaste.cn&Port=30009', Types.Click.LINK),
                    Element.Button('混战魔怔②服', 'http://43.143.135.75:18888/steam.php?Host=teawaste.cn&Port=30010', Types.Click.LINK)
                ),
                Module.Divider(),
                Module.Section('加入我们'),
                Module.ActionGroup(
                    Element.Button('QQ群', 'https://jq.qq.com/?_wv=1027&k=OHFSQSD6', Types.Click.LINK)
                )
            )
        )
    )
    
@bot.on_event(EventTypes.MESSAGE_BTN_CLICK)
async def print_btn_value(_: Bot, e: Event):
    #print(str(e.body))
    print(f'''{e.body['user_info']['nickname']} 点击了 {e.body['value']} 按钮''')
    val = e.body['value']
    if 's' in val:
        port = val.replace('s_', '')
        info = server_info(port)
        if not info:
            info_text = f'''查询失败'''
        else:
            info_text = info
    
    cb = Card(Module.Header('Tea社区'), Module.Section(info_text))
    cmb = CardMessage(cb)
    await bot.client.send(
        await bot.client.fetch_public_channel(
            channel_id=info_channel
        ), cmb, temp_target_id=e.body['user_id']
    )
        
bot.run()
