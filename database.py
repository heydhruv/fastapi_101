from sqlmodel import create_engine, SQLModel, Session

DATABASE_URL = "postgresql+psycopg2://dhruv:admin@127.0.0.1:5432/fastapi"

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session
