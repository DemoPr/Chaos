class dealFile:
    def getFile(self, path, encoding="UTF-8-sig"):
        # 处理zabbix excel文件获取需要的数据。
        fr = open(path, 'r', encoding=encoding)
        # 读所有行
        lines = fr.readlines()
        # 存储读出来的lines遍历成列表
        str_list = list()
        # 将str_list进行切割，然后嵌套字典存储
        split_list = list()
        for line in lines:
            str_list.append(line.strip())
        for strsplit in str_list:
            splitStr = strsplit.split(",")
            split_list.append({
                "Hostname": splitStr[0],
                "AllHostname": splitStr[1],
                "Ip": splitStr[2],
                "Os": splitStr[3],
                "Type": splitStr[4]
            })
        return split_list
        fr.close()
if __name__ == '__main__':
    df = dealFile()
    vmlists = df.getFile(path='E:\shiseido.csv',encoding='UTF-8-sig')
    print(vmlists[1]['Hostname'])
    print(vmlists[1]['AllHostname'])
    print(vmlists[1]['Ip'])
    print(vmlists[1]['Os'])