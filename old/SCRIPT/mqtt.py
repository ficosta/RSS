import logging
import socket
import time
from threading import Thread

import paho.mqtt.client as paho


PAHO_CLIENT = "paho.client"
PAHO_HOSTNAME = "157.230.58.241"
PAHO_PORT = 1883

logger = logging.getLogger(__name__)


def on_connect(mqtt_client, userdata, flags, rc):
    if userdata:
        logger.info("%s connecting to %s:%s",
                    "Success" if rc == 0 else "Failure",
                    userdata[PAHO_HOSTNAME],
                    userdata[PAHO_PORT])
    else:
        logger.info("%s connecting to MQTT broker", "Success" if rc == 0 else "Failure")


def on_subscribe(mqtt_client, userdata, mid, granted_qos):
    logger.info("Subscribed with message id: %s QOS: %s", mid, granted_qos)


def on_publish(mqtt_client, userdata, mid):
    logger.debug("Published value with message id %s", mid)


def on_disconnect(mqtt_client, userdata, rc):
    if userdata:
        logger.info("Disconecting from %s:%s", userdata[PAHO_HOSTNAME], userdata[PAHO_PORT])
    else:
        logger.info("Disconecting from MQTT broker")


class MqttConnection(object):
    def __init__(self,
                 hostname,
                 userdata=None,
                 on_connect=on_connect,
                 on_disconnect=on_disconnect,
                 on_publish=on_publish,
                 on_subscribe=on_subscribe,
                 on_message=None,
                 on_message_filtered=None,
                 on_log=None):
        self.__hostname, self.__port = mqtt_broker_info(hostname)

        self.__retry = True
        self.__thread = None

        # Create Paho client
        self.client = paho.Client(userdata=userdata)

        if userdata is not None:
            userdata[PAHO_CLIENT] = self.client
            if not userdata.get(PAHO_HOSTNAME):
                userdata[PAHO_HOSTNAME] = self.__hostname
            if not userdata.get(PAHO_PORT):
                userdata[PAHO_PORT] = self.__port

        if on_connect:
            self.client.on_connect = on_connect
        if on_disconnect:
            self.client.on_disconnect = on_disconnect
        if on_subscribe:
            self.client.on_subscribe = on_subscribe
        if on_publish:
            self.client.on_publish = on_publish
        if on_message:
            self.client.on_message = on_message
        if on_message_filtered:
            self.client.on_message_filtered = on_message_filtered
        if on_log:
            self.client.on_log = on_log

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()
        return self

    def connect(self):
        def connect_to_mqtt():
            while self.__retry:
                try:
                    logger.info("Connecting to MQTT broker %s:%s...", self.__hostname, self.__port)
                    self.client.connect(self.__hostname, port=self.__port, keepalive=60)
                    self.client.loop_forever()
                except socket.error:
                    logger.error("Cannot connect to MQTT broker %s:%s", self.__hostname, self.__port)
                    time.sleep(1)
                except BaseException as e:
                    logger.error("Cannot connect to MQTT broker %s:%s [%s]", self.__hostname, self.__port, e,
                                 exc_info=True)
                    time.sleep(1)

        if self.__thread:
            logger.error("MqttConnection.connect() already called")
        else:
            self.__thread = Thread(target=connect_to_mqtt)
            self.__thread.start()
        return self

    def disconnect(self):
        self.__retry = False
        self.client.disconnect()
