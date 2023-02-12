import requests

res = requests.post(url="http://monitor.azurememory.com/zabbix/api_jsonrpc.php",json={
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "user": "Admin",
            "password": "zabbix"
        },
        "id": 1
})
# print(res.text)
# auth_list = res.text.replace("\"","").split(",")
# auth = auth_list[1][7::]
# print(auth)
# # print(auth_list)
aaa = "333"
name = {
    "name": "chaos",
    f"nickname": aaa,
}
print(name)