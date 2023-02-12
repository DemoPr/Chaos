import requests
class zabbix_apis:
    httpApiUrl = "http://monitor.azurememory.com/zabbix/api_jsonrpc.php"
    auth = ""
    # respon = ""
    getAuth: dict = {
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "user": "Admin",
            "password": "zabbix"
        },
        "id": 1
    }
    def getConn(self) -> str:  # 获得zabbix的Auth信息。
        res = requests.post(url=zabbix_apis.httpApiUrl, json=zabbix_apis.getAuth)
        auth_list = res.text.replace("\"", "").split(",")
        auth = auth_list[1][7::]
        return auth



