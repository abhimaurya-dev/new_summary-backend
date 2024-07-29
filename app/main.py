from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from starlette.middleware.cors import CORSMiddleware
import numpy as np
import pickle
import nltk
from app.utils.data_cleaning import data_cleaning
from app.routers.get_summary import get_summary
import uvicorn


app = FastAPI()

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

get_summary()

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
