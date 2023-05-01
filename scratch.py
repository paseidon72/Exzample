import json
import requests


response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)
with open("file.json", "w") as write_file:
    json.dump(todos, write_file, indent=4)
print(todos == response.json())  # True
print(type(todos))  # <class 'list'>

print(todos[:10])

