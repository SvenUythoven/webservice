import uvicorn
from fastapi import FastAPI
import pyproj
from pyproj import Transformer

wgs84 = "EPSG:4326"
lv95= "EPSG:2056"



app = FastAPI()

@app.get("/wgs84lv95")
async def wgs84lv95(lng: float =0, lat: float =0):
    t1 = Transformer.from_crs(wgs84, lv95)
    return {"Coordinat LV95": t1.transform(lng, lat)
    }
@app.get("/lv95wgs84")
async def lv95wgs84(E: float =0, N: float =0):
    t2 = Transformer.from_crs(lv95, wgs84)
    return {"Coordinat WGS84": t2.transform(E, N)
    }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)