import fastapi
import uvicorn
import requests
import pydantic
from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv("KEY")

class CurrrentWeather(pydantic.BaseModel):
    temperature: float
    condition: str 
    class Meta:
        from_attributes = True

app = fastapi.FastAPI()
@app.get('/current-weather',response_model=CurrrentWeather)
def get_current_weather():
    response = requests.get(
        f'http://api.weatherapi.com/v1/current.json?key={key}&q=saint-petersburg&aqi=no'
    ).json()
    return CurrrentWeather(temperature=response['current']['temp_c'],condition=response['current']['condition']['text'])
uvicorn.run(app=app,host='0.0.0.0',port=3000)
