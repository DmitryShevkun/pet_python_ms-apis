from fastapi import FastAPI
import uvicorn
import pika

from config import service3

app = FastAPI()
app.title = 'Service 3'

@app.get('/')
def root():
    return {'msg': 'Service 3 root'}

@app.post('/response-from-service-3')
def response_from_service_3():
    return {'msg': 'response from service 3'}

if __name__ == "__main__":
    uvicorn.run(app, port=service3["port"])