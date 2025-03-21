#Parsing json string
import json
string = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(string)
print(data)
print(data['name'])

#