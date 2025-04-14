from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app import models, schemas
from datetime import datetime, timedelta

router = APIRouter(prefix="/reservations", tags=["Reservations"])

@router.get("/", response_model=list[schemas.reservation.ReservationRead])
def get_reservations(db: Session = Depends(get_db)):
    return db.query(models.reservation.Reservation).all()

@router.post("/", response_model=schemas.reservation.ReservationRead)
def create_reservation(reservation: schemas.reservation.ReservationCreate, db: Session = Depends(get_db)):
    # Проверка на пересечение времени
    existing_reservation = db.query(models.reservation.Reservation).filter(
        models.reservation.Reservation.table_id == reservation.table_id,
        models.reservation.Reservation.reservation_time <= reservation.reservation_time + timedelta(minutes=reservation.duration_minutes),
        models.reservation.Reservation.reservation_time + timedelta(minutes=reservation.duration_minutes) >= reservation.reservation_time
    ).first()
    
    if existing_reservation:
        raise HTTPException(status_code=400, detail="Table is already booked in this time slot.")

    db_reservation = models.reservation.Reservation(**reservation.dict())
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation

@router.delete("/{reservation_id}")
def delete_reservation(reservation_id: int, db: Session = Depends(get_db)):
    reservation = db.query(models.reservation.Reservation).filter_by(id=reservation_id).first()
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    db.delete(reservation)
    db.commit()
    return {"message": "Deleted"}
