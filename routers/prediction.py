from datetime import date, datetime
from time import mktime
from typing import Optional
from fastapi import APIRouter, HTTPException, File, UploadFile
from pydantic.main import BaseModel
from sqlalchemy import create_engine
import pandas as pd

router = APIRouter(
    tags = ["Predictions"],
    prefix = "/predict"
)

engine_rds = create_engine(
    'postgresql://postgres:postgres@ds4a-ec3.cddqgqis1uzk.us-east-2.rds.amazonaws.com:5432/postgres'
)

class response_message(BaseModel):
    msg: str

@router.post("/model")
async def predict(X: Optional[list] = None):

    """Here will be the model"""

    y = []

    for elem in X:
        y.append("Data predicted: " + str(elem**2))

    return y

@router.get("/existing_tables")
async def existing_tables():

    query = "SELECT * FROM team43_doria.averias;"
    df_averias = pd.read_sql(query, engine_rds)

    return f"Tamaño de la tabla averías: {df_averias.shape}"

@router.post("/load_data")
async def load_data(file: UploadFile = File(...)):

    df_loaded = pd.read_csv(file.file, sep = ";")

    df_loaded.to_sql(name = "testing", con = engine_rds, schema = "team43_doria", if_exists = 'replace')

    return{
        "filename": file.filename,
        "data loaded": df_loaded.head(5)
    }