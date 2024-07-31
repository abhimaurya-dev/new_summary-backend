from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from starlette.middleware.cors import CORSMiddleware
import nltk
from app.utils.data_cleaning import data_cleaning
from app.routers import get_summary
import uvicorn
from app.routers import get_summary
from dotenv import load_dotenv
from contextlib import asynccontextmanager
from app.services.scheduler import start_scheduler

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await start_scheduler()
    yield

app = FastAPI(lifespan=lifespan)

nltk.download('wordnet')
nltk.download('punkt')
nltk.download('omw-1.4')


# origins = ["https://soft-klepon-49df2a.netlify.app", "*"]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


app.include_router(get_summary.router)


@app.get("/", response_class=HTMLResponse)
def root():
    return """<html>
              <head>
                <title>Home</title>
              </head>
              <body style='overflow:hidden; background-color:grey'>
                <h1 style='display:flex; align-items:center; color:white; justify-content:center; width:100vw; font-size:4rem; height:100vh'>Welcome To News Summarizer Backend API</h1>
              </body>
              </html>"""
