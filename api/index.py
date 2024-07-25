from fastapi import FastAPI
import json
from typing import List, Dict

app = FastAPI()

# Load data from x.json
with open('x.json', 'r') as file:
    appointment_data = json.load(file)

@app.get("/{time}")
async def get_appointments(time: str) -> List[Dict[str, str]]:
    if time in appointment_data:
        return appointment_data[time]
    else:
        return []