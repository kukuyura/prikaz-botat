FROM python:3.10

RUN pip install pyTelegramBotAPI && pip install aiohttp && pip install asyncio

COPY ./main.py ./

CMD ["python",  "./main.py"]
