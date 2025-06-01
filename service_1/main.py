from fastapi import FastAPI, HTTPException
import uvicorn
import requests
import pika

import config


app = FastAPI()
app.title = 'Service 1'


def check_service_availability(url: str) -> bool:
    ok = False
    try:
        req = requests.get(url)
        if req.status_code == 200:
            ok = True
    except requests.exceptions.RequestException as e:
        print(e)
    return ok

def callback(ch, method, properties, body):
    print(f" [x] Received '{body.decode()}'")

def putCallandWaitForResponse(service: str) ->  str:

    connection = pika.BlockingConnection(pika.ConnectionParameters(host=config.service_rabbit.host))

    channel = connection.channel()
    #
    channel.queue_declare(queue=config.service.queue)

    message = "call to service"
    channel.basic_publish(exchange=config.service.exchange, routing_key='rkey', body=message)

    channel.basic_consume(queue=config.service1.queue, on_message_callback=callback, auto_ack=True)
    #
    connection.close()


@app.get('/')
def root():
    return {'msg': 'Service 1 root'}

@app.post('/to-service-2')
def to_service_2():
    if not check_service_availability(config.service2["host"] + ':' + config.service2["port"]):
        raise HTTPException(status_code, detail='Service 2 is unavailable')
    
    response = requests.post(config.service2["host"] + ':' + config.service2["port"] + '/response-from-service-2')
    return response.json()

@app.post('/to-service-3')
def to_service_3():
    if not check_service_availability(config.service3["host"] + ':' + config.service3["port"]):
        raise HTTPException(status_code, detail='Service 3 is unavailable')
    
    response = requests.post(config.service3["host"] + ':' + config.service3["port"] + '/response-from-service-3')
    return response.json()

@app.post('/to-service-4')
def to_service_4():
    if not check_service_availability(config.service4["host"] + ':' + config.service4["port"]):
        raise HTTPException(status_code, detail='Service 4 is unavailable')
    
    response = requests.post(config.service4["host"] + ':' + config.service4["port"] + '/response-from-service-4')
    return response.json()

@app.post('/to-service-2-queue')
def to_service_2():
    if not check_service_availability(config.service2["host"] + ':' + config.service2["port"]):
        raise HTTPException(status_code, detail='Service 2 is unavailable')
    
    response = requests.post(config.service2["host"] + ':' + config.service2["port"] + '/response-from-service-2')
    return response.json()


if __name__ == "__main__":
    uvicorn.run(app, port=config.service1["port"])