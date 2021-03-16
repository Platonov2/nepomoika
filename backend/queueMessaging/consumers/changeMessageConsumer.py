import threading
from backend.queueMessaging.connector import Connector


class ChangeMessageConsumer:
    def __init__(self):
        self.connector = Connector()

    def start_consuming_thread(self):
        threading.Thread(target=self.start_consuming).start()

    def start_consuming(self):
        self.connector.connect()
        self.connector.perform_setup_queue_infrastructure()
        self.connector.channel.basic_consume(queue='message_queue', on_message_callback=self.callback)
        self.connector.channel.start_consuming()

    def callback(self, ch, method, properties, body):
        print(body.decode())
        ch.basic_ack(delivery_tag=method.delivery_tag)
