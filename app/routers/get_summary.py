from transformers import pipeline

def get_summary():
  pipe = pipeline("summarization", model="t5-news/checkpoint-792", tokenizer="tokenizer")
  print(pipe("hello this is first line"))