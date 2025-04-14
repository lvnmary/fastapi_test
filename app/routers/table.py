from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app import models, schemas

router = APIRouter(prefix="/tables", tags=["Tables"])

@router.get("/", response_model=list[schemas.table.TableRead])
def get_tables(db: Session = Depends(get_db)):
    return db.query(models.table.Table).all()

@router.post("/", response_model=schemas.table.TableRead)
def create_table(table: schemas.table.TableCreate, db: Session = Depends(get_db)):
    db_table = models.table.Table(**table.dict())
    db.add(db_table)
    db.commit()
    db.refresh(db_table)
    return db_table

@router.delete("/{table_id}")
def delete_table(table_id: int, db: Session = Depends(get_db)):
    table = db.query(models.table.Table).filter_by(id=table_id).first()
    if not table:
        raise HTTPException(status_code=404, detail="Table not found")
    db.delete(table)
    db.commit()
    return {"message": "Deleted"}
