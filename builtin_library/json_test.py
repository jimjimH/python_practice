import json

user = {
	"UserName" : "A003",
	"Password" : 777
}

user_json = json.dumps(user)
print(user_json) # > {"UserName": "A003", "Password": 777}
print(type(user_json)) # > <class 'str'> json_string


def json_to_dict(json_string):
    user = json.loads(json_string)
    print(user) # > {'UserName': 'A003', 'Password': 777}
    print(type(user)) # > <class 'dict'>

json_to_dict(user_json)
