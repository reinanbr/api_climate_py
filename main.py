import requests as req
from datetime import datetime
import pytz
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi import FastAPI,Request
import os

app = FastAPI(debug=True)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


data_climate = req.get('https://raw.githubusercontent.com/reinanbr/noawclg/main/data_info/juazeiro_ba.json').json()
 

def get_date_key(dt_now:datetime):
    hours = dt_now.hour
    
    hours_key = 0
    hours_rest = hours%3
    if hours_rest > 1:
        hours_key = (hours//3)+3
    elif hours_rest==1:
        hours_key = hours//3
    else:
        hours_key = hours
    
    date_base = datetime(dt_now.year,dt_now.month,dt_now.day,hours_key,0)
    date_key = date_base.strftime("%d/%m/%Y_%H:%M")
    return date_key


def get_data_by_date(dt):
    dt_key = get_date_key(dt)
    data_date = data_climate[dt_key]
    return data_date






@app.get('/jua')
def jua():
    dt_now = datetime.now(pytz.timezone('America/Sao_Paulo'))
    data_now = (get_data_by_date(dt_now))

    return data_now


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    uvicorn.run('main:app', host="0.0.0.0", port=port, reload=True)