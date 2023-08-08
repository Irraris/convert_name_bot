FROM python:3.10
COPY . .
RUN pip install -r req.txt
ENTRYPOINT [ "python", "bot.py" ]