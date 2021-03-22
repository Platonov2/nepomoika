import pika
import os


class Connector:
    def __init__(self):
        self.credentials = pika.PlainCredentials(os.environ['RABBITMQ_DEFAULT_USER'], os.environ['RABBITMQ_DEFAULT_PASS'])
        self.connection = ""
        self.channel = ""

    def connect(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('rabbit', 5672, '/',
                                                                            credentials=self.credentials))
        self.channel = self.connection.channel()

    def perform_setup_queue_infrastructure(self):
        if self.channel == "":
            raise BaseException("First you need to use connect method")
        self.channel.exchange_declare(exchange='CUDMessages', exchange_type='fanout')

        self.channel.queue_declare(queue='message_queue_document_db', durable=True)
        self.channel.queue_declare(queue='message_queue_card', durable=True)

        self.channel.queue_bind(exchange='CUDMessages', queue='message_queue_document_db')
        self.channel.queue_bind(exchange='CUDMessages', queue='message_queue_card')
