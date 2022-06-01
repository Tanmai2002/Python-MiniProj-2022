import requests


def pushLog(payLoad):
    # payLoad = {"date": "6/6/2022", "timeOfSleep": "22.45", "quality": "55.0"}
    req = requests.post('http://localhost:5001/api/logs/', json=payLoad)
    print(req.text)

# pushLog()
