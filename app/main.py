from fastapi import FastAPI
from app.routers.notes import router as note_router

app = FastAPI(title='Markdown Note Taking App')

app.include_router(note_router, prefix='/notes', tags=['Notes']) 