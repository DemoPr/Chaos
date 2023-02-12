import json
data = [{"name":"Jack", "age":18},{"name":"Azure", "age":24},{"name":"Chaos","age":31}]
print(type(data))
jsons = json.dumps(data, ensure_ascii=False)
print(type(jsons))
print(jsons)
lists = json.loads(jsons)
print(type(lists))
print(lists)