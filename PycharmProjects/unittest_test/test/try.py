url = 'https://api.inewmaker.com/sys/user/add'
header = {"Content-Type":"application/json",
            "Authorization":"695927bb21f0019e910d254aa60a4b9b"}

data ={
            "name": "5231",
            "password": "1234567",
            "roleIdList": [
                1
            ],

            "username": "xuxu008"
        }
import requests
res = requests.post(url = url,json=data,headers= header)
print(res.text)