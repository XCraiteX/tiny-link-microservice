FROM python:3.12.7-slim
WORKDIR .
COPY . . 
RUN pip install fastapi
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "3400"]