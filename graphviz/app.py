from sqlmodel import Session
from .database import create_db_and_tables
from .models import *
import os
import json

def create_interactions():
    sample_data_path = os.getcwd() + '/graphviz/sample_data/'
    for filename in os.listdir(sample_data_path):
        with open(os.path.join(sample_data_path, filename), 'r') as f:
            data = json.load(f)
            # create interaction
            # create related entities
            


def main():
    create_db_and_tables()
    create_interactions()

if __name__ == "__main__":
    main()

