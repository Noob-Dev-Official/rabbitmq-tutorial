import pika, os, requests

RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', default='localhost')
RABBITMQ_PORT = os.getenv('RABBITMQ_PORT', default=5672)
RABBITMQ_USER = os.getenv('RABBITMQ_USER', default='test')
RABBITMQ_PASS = os.getenv('RABBITMQ_PASS', default='test')

credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
connection = pika.BlockingConnection(pika.ConnectionParameters(
   host=RABBITMQ_HOST, 
   credentials=credentials,
   port=RABBITMQ_PORT 
))
channel = connection.channel()

# create queue
channel.queue_declare(queue='hello')

# publish message to a queue
channel.basic_publish(
   exchange='',
   routing_key='hello',
   body='Hello World!'
)

print("'Hello World!' sent")

# close connection
connection.close()