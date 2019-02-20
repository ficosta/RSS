import paho.mqtt.client as mqtt
import sys
client = mqtt.Client("rssNotifier001")

#Callback - conexao ao broker realizada
def on_connect(client, userdata, flags, rc):
    print("[STATUS] Conectado ao Broker.")

try:
        print("[STATUS] Inicializando MQTT...")
        #inicializa MQTT:

        client.on_connect = on_connect
        client.connect("broker.hivemq.com", port=1883, keepalive=60)

except KeyboardInterrupt:
        print("\nCtrl+C pressionado, encerrando aplicacao e saindo...")
        sys.exit(0)
