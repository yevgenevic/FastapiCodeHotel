from datetime import date
from typing import List
from fastapi import APIRouter, Depends
from pydantic.main import BaseModel

from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking
from app.exceptions import RoomCannotBooked
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/bookings",
    tags=["бронирование"]
)


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)) -> List[SBooking]:
    return await BookingDAO.find_all(user_id=user.id)


class BookingRequest(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@router.post("")
async def add_booking(booking_request: BookingRequest, user: Users = Depends(get_current_user)):
    room_id = booking_request.room_id
    date_from = booking_request.date_from
    date_to = booking_request.date_to
    booking = await BookingDAO.add(user.id, room_id, date_from, date_to)
    if not booking:
        raise RoomCannotBooked
