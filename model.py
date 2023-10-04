from typing import Optional
from sqlmodel import Field, SQLModel, create_engine
from datetime import date
from pydantic import condecimal

class Journal(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    impact_factor: float

class Article(SQLModel, table=True):
    id: int = Field(primary_key=True)
    provenance: str
    url: str
    name: str
    publish_date: date
    journal: int = Field(foreign_key="journal.id")

class Significance(SQLModel, table=True):
    id: int = Field(primary_key=True)
    type: str
    value: condecimal()
    secondary_value: Optional[condecimal()] = Field(default=None)

class Evidence(SQLModel, table=True):
    id: int = Field(primary_key=True)
    text: str
    markup: str
    article: int = Field(foreign_key="article.id")

class Participant(SQLModel, table=True):
    id: int = Field(primary_key=True,index=True)
    kb_name: str
    kb_id: str
    Name: str

class Participant_Description(SQLModel, table=True):
    id: int = Field(primary_key=True)
    description: str
    participant_id: int = Field(foreign_key="participant.id")

class Interaction(SQLModel, table=True):
    id: int = Field(primary_key=True)
    controller: int = Field(foreign_key="participant.id")
    controlled: int = Field(foreign_key="participant.id")
    polarity: bool
    directed: bool

def build_models():
    sql_url = "postgresql://postgres:postgres@localhost:5432/graphviz_sampledb"

    engine = create_engine(sql_url, echo=True)
    SQLModel.metadata.create_all(engine)