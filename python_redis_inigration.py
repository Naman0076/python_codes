import redis

# Connect to a local Redis server
redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

# Test the connection
try:
    redis_client.ping()
    print("Connected to Redis!")
except redis.ConnectionError:
    print("Unable to connect to Redis.")

# Set a key-value pair
redis_client.set('example_key', 'Hello, Redis!')

# Get the value for a key
value = redis_client.get('example_key')
print(value)  # Output: Hello, Redis!

# Push elements to a list
redis_client.rpush('my_list', 'item1', 'item2', 'item3')

# Retrieve elements from the list
items = redis_client.lrange('my_list', 0, -1)
print(items)  # Output: ['item1', 'item2', 'item3']

# Set values in a hash
redis_client.hset('my_hash', 'field1', 'value1')
redis_client.hset('my_hash', 'field2', 'value2')

# Get values from the hash
field_value = redis_client.hget('my_hash', 'field1')
print(field_value)  # Output: value1

# Create a publisher
pubsub = redis_client.pubsub()

# Subscribe to a channel
pubsub.subscribe('my_channel')

# Publish a message to the channel
redis_client.publish('my_channel', 'Hello, subscribers!')

# Read messages from the channel
for message in pubsub.listen():
    print(message)