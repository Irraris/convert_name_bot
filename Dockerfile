FROM python:3.10
ENV TOKEN='6495178154:AAGphbGupvvAuPwmouc2lZSlVkMJvaO9rJs'
COPY . .
RUN pip install -r req.txt
ENTRYPOINT [ "python", "bot.py" ]