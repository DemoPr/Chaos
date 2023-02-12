import requests
import json
from zabbix_file import dealFile
class zabbix_utils:

    auth = ""

    def __init__(self):
        # 实例化以后将zabbix账号token存储在实例auth或者类auth中
        Url = "http://monitor.azurememory.com/zabbix/api_jsonrpc.php"
        AuthKey: dict = {
            "jsonrpc": "2.0",
            "method": "user.login",
            "params": {
                "user": "Admin",
                "password": "zabbix"
            },
            "id": 1
        }
        res = requests.post(url=Url, json=AuthKey)
        auth_list = res.text.replace("\"", "").split(",")
        self.auth = auth_list[1][7::]
        zabbix_utils.auth = auth_list[1][7::]

    def getAllHostGroupIdAndName(self, httpApiUrl, auth):
        getHostGroup :dict = {
            "jsonrpc": "2.0",
            "method": "hostgroup.get",
            "params": {
                "output": "extend",
                "filter": {
                    "groupids": [
                        "*"
                    ]
                }
            },
            "auth": auth,
            "id": 1
        }
        # print("get:",getHostGroup)
        # HostGroup = json.dumps(getHostGroup,ensure_ascii=False)
        # print(HostGroup)
        res = requests.post(url=httpApiUrl,json=getHostGroup)
        # print(auth)
        # print(res.text)
        list_group = json.loads(res.text)
        dict_group = list()
        i = 0
        while i < len(list_group["result"]):
            dict_group.append({list_group["result"][i]["groupid"]:list_group["result"][i]["name"]})
            i+=1
        return dict_group

    def addHost(self, vmlists, httpApiUrl, port, groupId, templatesId, auth):

        i = 1
        failCount = 0
        succCount = 0
        failMesg = list()
        while i < len(vmlists):
            addHostJson = {
                "jsonrpc": "2.0",
                "method": "host.create",
                "params": {
                    "host": vmlists[i]['AllHostname'],
                    "interfaces": [
                        {
                            "type": 1,
                            "main": 1,
                            "useip": 1,
                            "ip": vmlists[i]['Ip'],
                            "dns": "",
                            "port": port
                        }
                    ],
                    "groups": [
                        {
                            "groupid": groupId
                        }
                    ],
                    "templates": [
                        {
                            "templateid": templatesId
                        }
                    ],
                    "inventory_mode": 0
                },
                "auth": auth,
                "id": 1
            }
            res = requests.post(url=httpApiUrl, json=addHostJson)
            # print(res.text)
            str_list = res.text.replace("{","").replace("}","").split(",")
            # print(f"第{i}次",str_list)
            # for str in str_list:
            #     print(str)
            if str_list[1].__contains__("error"):
                failCount +=1
                failMesg.append({str_list[1][7::]:str_list[3][5::]})
            elif str_list[1].__contains__("result"):
                succCount += 1
            # str
            # {"jsonrpc":"2.0","result":{"hostids":["10457"]},"id":1}
            # {"jsonrpc":"2.0","error":{"code":-32602,"message":"Invalid params.","data":"Host with the same name \"10.26.51.20_cna-ipsapmnicrm-dev-app02\" already exists."},"id":1
            i +=1
        return failCount, failMesg, succCount
if __name__ == '__main__':
    Url = "http://monitor.azurememory.com/zabbix/api_jsonrpc.php"
    # 实例化对象生成auth码
    zu = zabbix_utils()
    print(zabbix_utils.auth)
    df = dealFile()
    vmlists = df.getFile(path='E:\shiseido.csv', encoding='UTF-8-sig')
    failCount,failMesg,succCount = zu.addHost(vmlists,Url,20073,"2","10047",zabbix_utils.auth)
    print("失败数",failCount)
    print(failMesg)
    print("成功数",succCount)
    # # 获取所有的主机ID和名字，并进行遍历输出
    # aa = zu.getAllHostGroupIdAndName(Url,zabbix_utils.auth)
    # for a in aa:
    # print(a)
    # zu.addHost(Url,"chaos3","192.168.0.111","10055","4","1",zabbix_utils.auth)

    # {"jsonrpc":"2.0","error":{"code":-32602,"message":"Invalid params.","data":"Host with the same name \"chaos1\" already exists."},"id":1}
    # {"jsonrpc":"2.0","error":{"code":-32500,"message":"Application error.","data":"No permissions to referred object or it does not exist!"},"id":1}
    # {"jsonrpc":"2.0","result":{"hostids":["10445"]},"id":1}
    # hosts = getAllHostGroupIdAndName()
    # print(auth)
    # print(hosts)
    # for host in hosts:
    # print(host)
