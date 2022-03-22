import pika

credentials = pika.PlainCredentials('test', 'test')
connection = pika.BlockingConnection(pika.ConnectionParameters(
   host='localhost', 
   virtual_host='vhost',
   credentials=credentials   
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