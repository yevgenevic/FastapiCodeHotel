from fastapi import FastAPI
from app.bookings.router import router as router_bookings
from app.users.router import router as router_users
from app.pages.router import router as router_pages
from app.hotels.router import router as router_hotels
from fastapi_cache import FastAPICache

app = FastAPI()
app.include_router(router_users)
app.include_router(router_hotels)
app.include_router(router_bookings)
app.include_router(router_pages)
