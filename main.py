from fastapi import FastAPI
from database import Base, engine
# команда для создания всех таблиц в дб
Base.metadata.create_all(bind=engine)
app = FastAPI(docs_url="/")

