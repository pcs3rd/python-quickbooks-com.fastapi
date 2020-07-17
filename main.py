from fastapi import FastAPI
import qbcom as pyqb
import xmltodict
#######################
#Start some app stuff #
#######################
api = FastAPI()
#qbcom
qb = pyqb.open()
tk = pyqb.begin(qb)
#web server
@api.get("/itemquery/{itemid}")
async def read_item(item_id: str, q: Optional[str] = None):
    if q:
        returndata = xmltodict.parse(pyqb.itemquery(qb, tk, item_id))
        return returndata
    return {"Error: no itemid gaven. Gotta give to get."}

@api.get("/inventorydump")
async def inventorydump():
    returndata = pyqb.inventory(qb, tk)
    return returndata
