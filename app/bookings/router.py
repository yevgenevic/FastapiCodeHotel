from typing import List
from fastapi import APIRouter,Request
from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking

router = APIRouter(
    prefix="/bookings",
    tags=["бронирование"]
)


@router.get("")
async def get_bookings(request: Request):
    return dir(request)

    #return await BookingDAO.find_all()
