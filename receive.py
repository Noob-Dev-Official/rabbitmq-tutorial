import pika, sys, os

def main():
   credentials = pika.PlainCredentials('test', 'test')
   connection = pika.BlockingConnection(pika.ConnectionParameters(
      host='localhost', 
      virtual_host='vhost',
      credentials=credentials
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
   channel.start_consuming()


if __name__ == '__main__':
   try:
      main()
   except KeyboardInterrupt:
      print('Interrupted')

      try:
         sys.exit(0)
      except SystemExit:
         os._exit(0)

