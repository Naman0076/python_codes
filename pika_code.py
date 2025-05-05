import pika
import sys
 
def publish_message(routing_key, message, config):
    # Establish connection and channel
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=config['host'],
        port=config['port']
    ))
    channel = connection.channel()
 
    # Declare the exchange
    channel.exchange_declare(
        exchange=config['exchange'],
        exchange_type='topic'
    )
 
    # Publish message to exchange with routing key
    channel.basic_publish(
        exchange=config['exchange'],
        routing_key=routing_key,
        body=message
    )
 
    print(f" [x] Sent '{message}' with routing key '{routing_key}'")
 
    connection.close()
 
# === MAIN EXECUTION ===
config = {
    'host': 'localhost',
    'port': 5672,
    'exchange': 'my_exchange'
}
 
if len(sys.argv) < 3:
    print(f"Usage: python {sys.argv[0]} <RoutingKey> <Message>")
    sys.exit(1)
 
routing_key = sys.argv[1]
message = ' '.join(sys.argv[2:])
 
publish_message(routing_key, message, config)