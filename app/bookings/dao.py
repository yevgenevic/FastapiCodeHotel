from app.bookings.models import Bookings
from app.dao.base import BaseDao


class BookingDAO(BaseDao):
    model = Bookings
