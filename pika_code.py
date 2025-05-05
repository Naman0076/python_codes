#publisher.py
import pika

class Publisher:
    def __init__(self, config):
        self.config = config

    def publish(self, routing_key, message):       
        connection = self.create_connection()
        # Create a new channel
        channel = connection.channel()
        # Creates an exchange if it does not already exist
        channel.exchange_declare(exchange=self.config['exchange'],
                                 exchange_type='topic')
        # Publishes message to the exchange with the given routing key
        channel.basic_publish(exchange=self.config['exchange'],
                              routing_key=routing_key, body=message)
        print(" [x] Sent message %r for %r" % (message, routing_key))

    # Create new connection
    def create_connection(self):
        param = pika.ConnectionParameters(
            host=self.config['host'],
            port=self.config['port']
        )
        return pika.BlockingConnection(param)

config = {'host': 'localhost', 'port': 5672, 'exchange': 'my_exchange'}
publisher = Publisher(config)
publisher.publish('nse.nifty', 'New Data')


#subscriber.py
import pika
import sys

class Subscriber:
    def __init__(self, queueName, bindingKey, config):
        self.queueName = queueName
        self.bindingKey = bindingKey
        self.config = config
        self.connection = self._create_connection()

    def __del__(self):
        self.connection.close()

    def _create_connection(self):
        parameters = pika.ConnectionParameters(
            host=self.config['host'],
            port=self.config['port']
        )
        return pika.BlockingConnection(parameters)

    def on_message_callback(self, channel, method, properties, body):
        binding_key = method.routing_key
        print("received new message for - " + binding_key)

    def setup(self):
        channel = self.connection.channel()
        channel.exchange_declare(exchange=self.config['exchange'],
                                 exchange_type='topic')
        # This method creates or checks a queue
        channel.queue_declare(queue=self.queueName)
        # Binds the queue to the specified exchange
        channel.queue_bind(queue=self.queueName,
                           exchange=self.config['exchange'],
                           routing_key=self.bindingKey)
        channel.basic_consume(queue=self.queueName,
                              on_message_callback=self.on_message_callback,
                              auto_ack=True)
        print(' [*] Waiting for data for ' + self.queueName + '. To exit press CTRL+C')
        try:
            channel.start_consuming()
        except KeyboardInterrupt:
            channel.stop_consuming()

config = {'host': 'localhost', 'port': 5672, 'exchange': 'my_exchange'}

if len(sys.argv) < 3:
    print('Usage: ' + __file__ + ' <QueueName> <BindingKey>')
    sys.exit()
else:
    queueName = sys.argv[1]
    key = sys.argv[2]  # key in the form exchange.*
    subscriber = Subscriber(queueName, key, config)
    subscriber.setup()
