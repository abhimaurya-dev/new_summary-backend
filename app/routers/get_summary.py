from fastapi import APIRouter, HTTPException
from transformers import pipeline
from app.models.summary_model import SummaryInDB
from app.config.summary_model_loader import tokenizer, model
from bs4 import BeautifulSoup
from app.config.database import add_summary, get_summaries, delete_all_summaries
from typing import List, Optional
import asyncio
from fastapi.responses import JSONResponse
import requests
from app.news_scrapper.news_scrapper import news_scrapper

router = APIRouter()

news_urls = {
    'Budget News': 'https://www.moneycontrol.com/news/business/budget/',
    'Market News': 'https://www.moneycontrol.com/news/business/',
    'Markets News': 'https://www.moneycontrol.com/news/business/markets/',
    'World News': 'https://www.moneycontrol.com/news/world/',
    'Crypto News': 'https://www.moneycontrol.com/news/tags/cryptocurrency.html'
}

async def summarize_and_store(category: str, url: str):
    # for category, url in news_urls.items():
    news_data = news_scrapper(category,url)
    print(len(news_data))
    if news_data:
      pipe = pipeline("summarization", model=model, tokenizer=tokenizer)
      count = 1
      if(len(news_data) != 0):
          await delete_all_summaries()
          print("Summary Database is cleared")
      for article in news_data:
          count += 1
          news_text = article['text']
          # Truncate news_text if it's too long
          if len(news_text) > 2000:
              news_text = news_text[:2000]
          
          # Summarize the news text
          summary = pipe(news_text)[0]['summary_text']
          
          # Add summary to the database with date and category
          await add_summary(category, summary)
          print("Added " + str(count) + "article in db")

@router.get("/summary", response_model=SummaryInDB)
async def get_summary_endpoint(category: str):
    if category not in news_urls:
        raise HTTPException(status_code=400, detail="Invalid category")
    
    summaries = await get_summaries(category)
    if summaries:
        return JSONResponse(content=[summary.dict(by_alias=True) for summary in summaries])
    else:
        raise HTTPException(status_code=404, detail="No summary found")

async def update_summaries():
    tasks = [summarize_and_store(category, url) for category, url in news_urls.items()]
    await asyncio.gather(*tasks)
