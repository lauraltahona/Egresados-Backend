# import os
# from dotenv import load_dotenv
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base

# archivo_encontrado = load_dotenv()

# print(f"¿Archivo .env encontrado?: {archivo_encontrado}")
# print(f"Ruta actual de trabajo: {os.getcwd()}")
# print(f"DATABASE_URL desde el env: {os.getenv('DATABASE_URL')}")

# USER = os.getenv("user")
# PASSWORD = os.getenv("password")
# HOST = os.getenv("host")
# PORT = os.getenv("port")
# DBNAME = os.getenv("dbname")

# DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"

# engine = create_engine(DATABASE_URL, connect_args={"sslmode": "require"})  #sin ssl los datos no "viajan" encriptados y es inseguro

# SessionLocal = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine
# )

# Base = declarative_base()
