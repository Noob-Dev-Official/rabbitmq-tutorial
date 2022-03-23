import pika, sys, os

RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', default='localhost')
RABBITMQ_PORT = os.getenv('RABBITMQ_PORT', default=5672)
RABBITMQ_USER = os.getenv('RABBITMQ_USER', default='test')
RABBITMQ_PASS = os.getenv('RABBITMQ_PASS', default='test')

print(type(RABBITMQ_HOST))

def main():
   credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
   connection = pika.BlockingConnection(pika.ConnectionParameters(
      host=RABBITMQ_HOST, 
      credentials=credentials,
      port=RABBITMQ_PORT
   ))
   channel = connection.channel()

   # create queue
   channel.queue_declare(queue='hello')

   def callback(ch, method, properties, body):
      print(" [x] Received %r" % body)

   channel.basic_consume(
      queue='hello',
      auto_ack=True,
      on_message_callback=callback
   )

   print(' [*] Waiting for messages. To exit press CTRL+C')
   # channel.start_consuming()


if __name__ == '__main__':
   main()
   # try:
   # except KeyboardInterrupt:
   #    print('Interrupted')

   #    try:
   #       sys.exit(0)
   #    except SystemExit:
   #       os._exit(0)

