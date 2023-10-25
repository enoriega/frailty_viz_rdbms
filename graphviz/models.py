from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel, create_engine
from datetime import date
from pydantic import condecimal

class Journal(SQLModel, table=True):
    id: str = Field(primary_key=True)
    name: str
    impact_factor: float
    
    articles: List["Article"] = Relationship(back_populates="journal")

class Article(SQLModel, table=True):
    id: str = Field(primary_key=True)
    provenance: str
    url: str
    name: str
    publish_date: date

    journal_id: Optional[str] = Field(default=None, foreign_key="journal.id")
    journal: Optional[Journal] = Relationship(back_populates="articles")

    significances: List["Significance"] = Relationship(back_populates="article")
    evidences: List["Evidence"] = Relationship(back_populates="evidence")

class Significance(SQLModel, table=True):
    id: int = Field(primary_key=True)
    type: str
    value: condecimal()
    secondary_value: Optional[condecimal()] = Field(default=None)

    article_id: str = Field(foreign_key="article.id")
    article: "Article" = Relationship(back_populates="significances")

class Evidence(SQLModel, table=True):
    id: str = Field(primary_key=True)
    text: str
    markup: str

    article_id: str = Field(foreign_key="article.id")
    article: "Article" = Relationship(back_populates="significances")

class Participant(SQLModel, table=True):
    id: str = Field(primary_key=True,index=True)
    kb_name: str
    kb_id: str
    Name: str

    descriptions: List["Participant_Description"] = Relationship(back_populates="participant")

class Participant_Description(SQLModel, table=True):
    id: str = Field(primary_key=True)
    description: str
    participant_id: str = Field(foreign_key="participant.id")

    participant: "Participant" = Relationship(back_populates="descriptions")

class Interaction(SQLModel, table=True):
    id: str = Field(primary_key=True)
    controller: str = Field(foreign_key="participant.id")
    controlled: str = Field(foreign_key="participant.id")
    polarity: bool
    directed: bool
