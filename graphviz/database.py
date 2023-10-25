from sqlmodel import SQLModel, create_engine

host = "localhost"
port = "5432"
database = "graphviz_sampledb"
user = "postgres"
password = "postgres"

sql_url = f"postgresql://{user}:{password}@{host}:{port}/{database}"

engine = create_engine(sql_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)