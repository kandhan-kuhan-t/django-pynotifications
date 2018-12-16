import os
from django.conf import settings
import json
import pynotifications

producer_dict = {
    
}


class ProducerProxy:
    def __init__(self, producer):
        self.success_callback_fn = None
        self.failure_callback_fn = None
        self.name = None
        self.producer = producer

    def register_success_callback(self, fn):
        self.success_callback_fn = fn

    def register_failure_callback(self, fn):
        self.failure_callback_fn = fn

    def get_producer(self) -> pynotifications.producer.Producer:
        return self.producer


def generate_callback_url(system) -> str:
    cb_url = f"http://localhost:8000/{settings.NOTIPY_NAMESPACE}/callback/{system}"
    return cb_url


def get_success_callback_function_for(system):
    return producer_dict[system].success_callback_fn


def get_failure_callback_function_for(system):
    return producer_dict[system].failure_callback_fn


def get_producer_proxy(system) -> ProducerProxy:
    return producer_dict[system]


def init():
    conf_file_path = os.path.join(settings.BASE_DIR, "notipy.conf.json")
    should_run_consumer = settings.NOTIPY_SHOULD_RUN_CONSUMER
    conf_file = open(conf_file_path, "r")
    confs = json.load(conf_file)
    for conf in confs:
        if should_run_consumer:
            print(f'{conf["name"]}: initializing consumer..')
        else:
            print(f'{conf["name"]}: consumer is not initialized')
        conf["callback_url"] = generate_callback_url(system=conf["name"])
        o = pynotifications.orchestrator.run(conf, should_create_consumer=should_run_consumer)
        producer = pynotifications.orchestrator.get_producer(conf["name"])
        producer_dict[conf["name"]] = ProducerProxy(producer=producer)
