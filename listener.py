import pusherclient
import time

# Pusher credentials
app_key = '3c16203f5e43994b9acf'
cluster = 'eu'


# Define a callback for connection success
def connect_handler(data):
    channel = pusher.subscribe('my-channel')
    channel.bind('my-event', event_handler)


# Define a callback for receiving events
def event_handler(data):
    print('Received event with data:', data)


# Define a function to handle Pusher connection
def connect_pusher():
    # Initialize Pusher with the app key
    pusher = pusherclient.Pusher(app_key)

    # Set the connection URL to include the cluster
    pusher.connection.url = f"wss://ws-{cluster}.pusher.com:443/app/{app_key}?client=pusher-python&version=0.1&protocol=7"

    # Bind to connection established event
    pusher.connection.bind('pusher:connection_established', connect_handler)

    # Connect to Pusher
    pusher.connect()

    return pusher


# Initialize and connect to Pusher
pusher = connect_pusher()

# Keep the script running
while True:
    time.sleep(1)
