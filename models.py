from opt_einsum.backends import torch
import numpy as np
import textwrap
import torch

model_news = torch.load('/home/alexandr/bot_text/model_new.pt', map_location=torch.device('cpu'))
model_congr = torch.load('/home/alexandr/bot_text/model_congr.pt', map_location=torch.device('cpu'))
device = 'cuda' if torch.cuda.is_available() else 'cpu'
# Загружаем токенайзер модели
from transformers import GPT2Tokenizer



# model_news = torch.load('/home/alexandr/bot_text/model_new.pt')
# model_congr = torch.load('/home/alexandr/bot_text/model_congr.pt')


# Функции для генерации

def get_congr(prompt):
    tokenizer = GPT2Tokenizer.from_pretrained('sberbank-ai/rugpt3small_based_on_gpt2')

    prompt = tokenizer.encode(prompt, return_tensors='pt').to(device)
    out = model_congr.generate(
        input_ids=prompt,
        max_length=25,
        num_beams=15,
        do_sample=True,
        temperature=3.,
        top_k=50,
        top_p=0.7,
        no_repeat_ngram_size=2,
        num_return_sequences=7,
    ).cpu().numpy()
    return textwrap.fill(tokenizer.decode(out[0]) + '!', 120)


def get_news(prompt):
    tokenizer = GPT2Tokenizer.from_pretrained('sberbank-ai/rugpt3small_based_on_gpt2')

    prompt = tokenizer.encode(prompt, return_tensors='pt').to(device)
    out = model_news.generate(
        input_ids=prompt,
        max_length=25,
        num_beams=15,
        do_sample=True,
        temperature=3.,
        top_k=50,
        top_p=0.6,
        no_repeat_ngram_size=2,
        num_return_sequences=7,
    ).cpu().numpy()
    return textwrap.fill(tokenizer.decode(out[0]) + '...', 120)

# print(get_congr('привет'))
# print(get_news('привет'))