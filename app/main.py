from fastapi import FastAPI, Query
from typing import Optional
from datetime import date
from pydantic import BaseModel
from app.bookings.router import router as router_bookings

app = FastAPI()
app.include_router(router_bookings)


@app.get("/hotels")
def get_hotels(
        location: str,
        date_from: date,
        date_to: date,
        has_spa: Optional[bool] = None,
        stars: Optional[int] = Query(None, ge=1, le=5),

):
    return date_from, date_to


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post("/bookings")
def add_bookings(booking: SBooking):
    pass
