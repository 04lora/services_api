from pydantic import BaseModel

class ServicioCrear(BaseModel):
    name: str
    price: float
    description: str

class ServicioRespuesta(BaseModel):
    id: int
    name: str
    price: float
    description: str

    class Config:
        from_attributes = True