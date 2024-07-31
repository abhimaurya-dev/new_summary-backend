from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline

model_name = "abhimaurya-dev/t5-news"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)