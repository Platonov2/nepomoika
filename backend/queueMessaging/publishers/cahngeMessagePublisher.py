import json
import pika

from backend.queueMessaging.connector import Connector


class ChangeMessagePublisher:
    def __init__(self):
        self.connector = Connector()

    def publish_task(self, message_in_json: {}, only_for_catalog: bool):
        message_json = json.dumps(message_in_json)

        self.connector.connect()
        self.connector.perform_setup_queue_infrastructure()
        if only_for_catalog:
            self.connector.channel.basic_publish(
                exchange='',
                routing_key='message_queue_document_db',
                body=message_json,
                properties=pika.BasicProperties(
                    delivery_mode=2,  # make message persistent
                ))
        else:
            self.connector.channel.basic_publish(
                exchange='CUDMessages',
                routing_key='',
                body=message_json,
                properties=pika.BasicProperties(
                    delivery_mode=2,  # make message persistent
                ))
        self.connector.connection.close()