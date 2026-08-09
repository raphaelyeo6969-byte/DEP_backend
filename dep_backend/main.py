from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
import os

from database import SessionLocal
from crud import save_reading


app = FastAPI()

API_KEY = os.getenv("NESSO_API_KEY")


class Reading(BaseModel):
    sample_no: int
    time: float
    interval: float

    accel_x: float
    accel_y: float
    accel_z: float

    gyro_x: float
    gyro_y: float
    gyro_z: float


class NessoData(BaseModel):
    device_id: str
    readings: list[Reading]
