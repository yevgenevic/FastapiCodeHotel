from typing import List
from fastapi import APIRouter, Depends
from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/bookings",
    tags=["бронирование"]
)


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)):
    return user
    # return await BookingDAO.find_all()
