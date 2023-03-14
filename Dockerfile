FROM python:3.8

COPY requirements.txt .

RUN mkdir -p -m 0700 ~/.ssh && ssh-keyscan github.com >> ~/.ssh/known_hosts
RUN --mount=type=ssh pip install -r requirements.txt 

COPY . .

EXPOSE 9050
CMD ["python", "./app.py"]