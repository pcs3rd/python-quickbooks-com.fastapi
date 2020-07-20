from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
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
    requestdata = xmltodict.parse(pyqb.itemquery(qb, tk, item_id), dict_constructor=dict, encoding='utf-8')
    returndata = jsonable_encoder(requestdata)
    return JSONResponse(content=returndata)

@api.get("/inventorydump")
async def inventorydump():
    requestdata = xmltodict.parse(pyqb.inventory(qb, tk), dict_constructor=dict, encoding='utf-8')
    returndata = jsonable_encoder(requestdata)
    return returndata

@api.get("/netinfo")
async def netinfo():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    returndata = host_ip, host_name
    return returndata
