import json
import pika

from queueMessaging.connector import Connector


class OrderPublish:
    def __init__(self):
        self.connector = Connector()

    def publish_task(self, message_in_json: {}):
        message_json = json.dumps(message_in_json)

        self.connector.connect()
        self.connector.perform_setup_queue_infrastructure()
        self.connector.channel.basic_publish(
            exchange='',
            routing_key='message_queue_order',
            body=message_json,
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
            ))
        self.connector.connection.close()