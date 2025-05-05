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