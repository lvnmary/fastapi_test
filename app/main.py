import logging
from fastapi import FastAPI
from app.routers import table, reservation

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.include_router(table.router)
app.include_router(reservation.router)
