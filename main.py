from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import Base, motor, obtener_bd
from models import Servicio
from schemas import ServicioCrear, ServicioRespuesta

Base.metadata.create_all(bind=motor)

app = FastAPI(title="API de Servicios")

@app.get("/servicios", response_model=list[ServicioRespuesta])
def listar_servicios(bd: Session = Depends(obtener_bd)):
    return bd.query(Servicio).all()

@app.get("/servicios/{servicio_id}", response_model=ServicioRespuesta)
def obtener_servicio(servicio_id: int, bd: Session = Depends(obtener_bd)):
    servicio = bd.query(Servicio).filter(Servicio.id == servicio_id).first()
    if not servicio:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return servicio

@app.post("/servicios", response_model=ServicioRespuesta, status_code=201)
def crear_servicio(datos: ServicioCrear, bd: Session = Depends(obtener_bd)):
    nuevo = Servicio(
        name=datos.name,
        price=datos.price,
        description=datos.description
    )
    bd.add(nuevo)
    bd.commit()
    bd.refresh(nuevo)
    return nuevo