import pika

# Connection parameters
rabbitmq_host = 'localhost'
queue_name    = 'hello_queue'

# Establish a connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
channel = connection.channel()

# Declare a queue (it ensures the queue exists before publishing)
channel.queue_declare(queue=queue_name)

# The message to send
message = "Hello, RabbitMQ!"

# Publish the message to the queue
channel.basic_publish(exchange='fanout',
                      routing_key='rkey',
                      body=message)

# Close the connection
connection.close()
