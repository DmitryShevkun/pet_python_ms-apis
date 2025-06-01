from fastapi import FastAPI
import uvicorn
import pika

from config import service2

app = FastAPI()
app.title = 'Service 2'

@app.get('/')
def root():
    return {'msg': 'Service 2 root'}

@app.post('/response-from-service-2')
def response_from_service_2():
    return {'msg': 'response from service 2'}

if __name__ == "__main__":
    uvicorn.run(app, port=service2["port"])