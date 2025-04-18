#!/usr/bin/env python3
import asyncio
import os, logging
from datetime import datetime
from panoramisk import Manager
from google.cloud import pubsub_v1
import json

# AMI connection details
AMI_HOST = 'localhost'
AMI_PORT = 5038
AMI_USER = 'myuser'
AMI_SECRET = 'my_secret'

# Google Cloud Pub/Sub settings
PROJECT_ID = 'raicodev'
TOPIC_ID = 'asterisk-event-conn01'

os.environ['GOOGLE_APPLICATION_CREDENTIALS']='/root/google/raicodev-746779cb50f2.json'

# Initialize Pub/Sub publisher
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)

async def handle_ami_event(manager, event):
    """Process AMI event and send to Google Cloud Pub/Sub"""
    # Convert event to dictionary
    event_dict = dict(event)
    time01 = datetime.now()

    attributes = {}

    # Convert to JSON
    event_json = json.dumps(event_dict).encode('utf-8')
    event_tmp = json.loads(event_json)
    if "Event" in event_tmp:
        #print(event_tmp)
        attributes["Event"]=event_tmp.get("Event")
    attributes_json = json.dumps(attributes).encode('utf-8')
    #print(f"Attributes : {attributes}")

    # Publish to Google Cloud Pub/Sub
    future = publisher.publish(topic_path, event_json, **attributes)
    #print(f"Published message ID: {future.result()}")
    logging.info("%s Event: %s ",time01,event_json)

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
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/root/google/raicodev-746779cb50f2.json"
    logging.basicConfig(filename='/var/log/monitorAMI.log',format='%(asctime)s.%(msecs)03d %(threadName)s %(message)s', datefmt='%Y%m%d %H:%M:%S', level=logging.INFO)
    logging.info('**** Starting Application MonitorAMI Server (V1.0)')

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())