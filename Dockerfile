FROM python:3.12.7-slim
WORKDIR .
COPY . . 
RUN pip install fastapi uvicorn sqlalchemy aiosqlite
CMD ["uvicorn", "api:app", "--port", "3400"]