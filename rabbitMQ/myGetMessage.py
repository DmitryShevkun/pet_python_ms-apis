import pika

# Connection parameters
rabbitmq_host = 'localhost'
queue_name = 'q3'

# Establish a connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
channel = connection.channel()

# Declare the queue (it ensures the queue exists before consuming)
channel.queue_declare(queue=queue_name)

print(f" [*] Waiting for messages in '{queue_name}'. To exit, press CTRL+C.")

# Define a callback function to process received messages
def callback(ch, method, properties, body):
    print(f" [x] Received '{body.decode()}'")

# Set up the consumer
channel.basic_consume(queue=queue_name,
                      on_message_callback=callback,
                      auto_ack=True)

# Start consuming messages
channel.start_consuming()