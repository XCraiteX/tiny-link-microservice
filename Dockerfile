FROM python:3.12.7-slim
WORKDIR .
COPY . . 
RUN pip install fastapi uvicorn sqlalchemy aiosqlite
EXPOSE 3400
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "3400"]