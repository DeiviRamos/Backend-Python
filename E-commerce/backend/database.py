from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base

# URL conexion a PostgreSQL
DATABASE_URL = ""

#Motor de la base de datos
engine = create_engine(DATABASE_URL)

#Sesion para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Crea las tablas de los modelos
Base.metadata.create_all(bing=engine)