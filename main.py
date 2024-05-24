from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI()

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, for specific origins, use the list of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers

)
class Aeroplanedetails(BaseModel):
    id: int
    num_seates: int
    name_aero: str
aeroplane_details = [
    Aeroplanedetails(id=1, num_seates=15,name_aero= "Aircanada" ),
    Aeroplanedetails(id=2, num_seates=20,name_aero= "Lufthansa" ),
    Aeroplanedetails(id=3, num_seates=18,name_aero= "Airindia" ),
]
@app.get("/aeroplane", response_model=list[Aeroplanedetails])
def return_aeroplane():
    return aeroplane_details

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)