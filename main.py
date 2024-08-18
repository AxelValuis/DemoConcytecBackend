from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
import pandas as pd
from pydantic import BaseModel

app = FastAPI()

# Configuración de la conexión
db_url = "postgresql+psycopg2://postgres_renacyt:ConcyTEC%26SdC.TI%232024%23.@database-renacyt.ctaiaeus24we.us-east-1.rds.amazonaws.com/RENACYTDB"
# Configuracion de CORS
origins = [
    "http://localhost:4200",  # Permite el origen de tu aplicación Angular
    "http://127.0.0.1:4200",  # También puedes incluir esta línea si accedes desde esta URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los encabezados
)
# Clase para manejar la estructura de la respuesta
class Criterion(BaseModel):
    name: str
    value: float

class RowDetail(BaseModel):
    solicitud_id: int
    postulante_id: int
    id_investigador: int
    prob_sospechoso: float
    var_import: list[Criterion]

@app.get("/data-types/{table_name}")
def get_data_types(table_name: str):
    try:
        # Crear el motor de conexión
        engine = create_engine(db_url)
        
        # Obtener los tipos de datos
        query = f"SELECT * FROM {table_name} LIMIT 1;"
        df = pd.read_sql(query, engine)
        
        # Convertir los tipos de datos a una estructura Python
        dtypes = df.dtypes.astype(str).to_dict()
        
        return {"dtypes": dtypes}
    
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Error al conectar a la base de datos: {error}")

@app.get("/row-details/{table_name}/{row_id}", response_model=RowDetail)
def get_row_details(table_name: str, row_id: int):
    try:
        # Crear el motor de conexión
        engine = create_engine(db_url)
        
        # Consultar el registro específico
        query = f"SELECT * FROM {table_name} WHERE solicitud_id = {row_id} LIMIT 1;"
        df = pd.read_sql(query, engine)
        
        if df.empty:
            raise HTTPException(status_code=404, detail="Registro no encontrado")

        # Procesar `var_import` para convertirlo en lista de criterios
        var_import = eval(df.at[0, 'var_import'])
        criterios = [{"name": f"Criterio {i+1}", "value": valor} for i, valor in enumerate(var_import)]
        
        row_detail = {
            "solicitud_id": df.at[0, "solicitud_id"],
            "postulante_id": df.at[0, "postulante_id"],
            "id_investigador": df.at[0, "id_investigador"],
            "prob_sospechoso": df.at[0, "prob_sospechoso"],
            "var_import": criterios
        }
        
        return row_detail
    
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Error al obtener los detalles de la fila: {error}")

@app.get("/all-records/{table_name}")
def get_all_records(table_name: str):
    try:
        # Crear el motor de conexión
        engine = create_engine(db_url)
        
        # Consultar todos los registros
        query = f"SELECT * FROM {table_name};"
        df = pd.read_sql(query, engine)
        
        if df.empty:
            raise HTTPException(status_code=404, detail="No se encontraron registros en la tabla")

        # Procesar `var_import` para convertirlo en lista de criterios
        for index, row in df.iterrows():
            var_import = eval(row['var_import'])
            criterios = [{"name": f"Criterio {i+1}", "value": valor} for i, valor in enumerate(var_import)]
            df.at[index, 'var_import'] = criterios

        # Convertir los registros a una estructura Python
        data = df.to_dict(orient='records')
        
        return {"data": data}
    
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Error al obtener los registros: {error}")



@app.get("/first-100-records/{table_name}")
def get_first_100_records(table_name: str):
    try:
        # Crear el motor de conexión
        engine = create_engine(db_url)
        
        # Consultar los primeros 100 registros
        query = f"SELECT * FROM {table_name} LIMIT 100;"
        df = pd.read_sql(query, engine)
        
        if df.empty:
            raise HTTPException(status_code=404, detail="No se encontraron registros en la tabla")

        # Procesar `var_import` para convertirlo en lista de criterios
        for index, row in df.iterrows():
            var_import = eval(row['var_import'])
            criterios = [{"name": f"Criterio {i+1}", "value": valor} for i, valor in enumerate(var_import)]
            df.at[index, 'var_import'] = criterios

        # Convertir los registros a una estructura Python
        data = df.to_dict(orient='records')
        
        return {"data": data}
    
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Error al obtener los registros: {error}")
    
@app.get("/first-50-records/{table_name}")
def get_first_50_records(table_name: str):
    try:
        # Crear el motor de conexión
        engine = create_engine(db_url)
        
        # Consultar los primeros 100 registros
        query = f"SELECT * FROM {table_name} LIMIT 50;"
        df = pd.read_sql(query, engine)
        
        if df.empty:
            raise HTTPException(status_code=404, detail="No se encontraron registros en la tabla")

        # Procesar `var_import` para convertirlo en lista de criterios
        for index, row in df.iterrows():
            var_import = eval(row['var_import'])
            criterios = [{"name": f"Criterio {i+1}", "value": valor} for i, valor in enumerate(var_import)]
            df.at[index, 'var_import'] = criterios

        # Convertir los registros a una estructura Python
        data = df.to_dict(orient='records')
        
        return {"data": data}
    
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Error al obtener los registros: {error}")
@app.get("/criteria-by-solicitud/{table_name}/{solicitud_id}", response_model=list[Criterion])
def get_criteria_by_solicitud(table_name: str, solicitud_id: int):
    try:
        # Crear el motor de conexión
        engine = create_engine(db_url)
        
        # Consultar el registro específico
        query = f"SELECT var_import FROM {table_name} WHERE solicitud_id = {solicitud_id} LIMIT 1;"
        df = pd.read_sql(query, engine)
        
        if df.empty:
            raise HTTPException(status_code=404, detail="Registro no encontrado")

        # Procesar `var_import` para convertirlo en lista de criterios
        var_import = eval(df.at[0, 'var_import'])
        criterios = [{"name": f"Criterio {i+1}", "value": valor} for i, valor in enumerate(var_import)]
        
        return criterios
    
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Error al obtener los criterios: {error}")