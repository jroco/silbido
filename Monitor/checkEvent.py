#!/usr/bin/env python3
import asyncio
import os
import time
from panoramisk import Manager
from google.cloud import pubsub_v1
import json

# AMI connection details
AMI_HOST = 'localhost'
AMI_PORT = 5038
AMI_USER = 'your_username'
AMI_SECRET = 'your_secret_password'

# Google Cloud Pub/Sub settings
#PROJECT_ID = 'your-google-cloud-project-id'
#TOPIC_ID = 'asterisk-events'

# Initialize Pub/Sub publisher
#publisher = pubsub_v1.PublisherClient()
#topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)

async def handle_ami_event(manager, event):
    """Process AMI event and send to Google Cloud Pub/Sub"""
    # Convert event to dictionary
    event_dict = dict(event)

    time01 = time.time()

    # Convert to JSON
    event_json = json.dumps(event_dict).encode('utf-8')

    # Publish to Google Cloud Pub/Sub
#    future = publisher.publish(topic_path, event_json)
#    print(f"Published message ID: {future.result()}")
    print(f"{time01} Event: {event_dict}")

async def main():
    manager = Manager(
        host=AMI_HOST,
        port=AMI_PORT,
        username=AMI_USER,
        secret=AMI_SECRET,
        ping_delay=5,  # Seconds between pings
    )

    # Register event handler for all events
    manager.register_event('*', handle_ami_event)

    # Connect to AMI
    await manager.connect()

    # Keep the connection alive
    while True:
        await asyncio.sleep(1)

if __name__ == '__main__':
    # Set Google Cloud credentials
    #os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/path/to/your/service-account-key.json"

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()