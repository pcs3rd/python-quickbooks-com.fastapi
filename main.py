from fastapi import FastAPI
import qbcom as pyqb
import xmltodict
import json
import socket
#######################
#Start some app stuff #
#######################
api = FastAPI()
#qbcom
qb = pyqb.open()
tk = pyqb.begin(qb)
#web server
@api.get("/items/{item_id}")
async def read_item(item_id):
    returndata = json.dumps(xmltodict.parse(pyqb.itemquery(qb, tk, 43313), dict_constructor=dict, encoding='utf-8'))
    return returndata

@api.get("/inventorydump")
async def inventorydump():
    returndata = json.dumps(xmltodict.parse(pyqb.inventory(qb, tk), dict_constructor=dict, encoding='utf-8'))
    return returndata

@api.get("/netinfo")
async def netinfo():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    returndata = host_ip, host_name
    return returndata
