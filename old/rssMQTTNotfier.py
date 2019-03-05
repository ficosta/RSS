import paho.mqtt.client as mqtt
import sys
client = mqtt.Client("rssNotifier001")
host="Server01"
#Callback - conexao ao broker realizada
def on_connect(client, userdata, flags, rc):
    print("[STATUS] Conectado ao Broker.")


try:
        print("[STATUS] Inicializando MQTT...")
        #inicializa MQTT:

        client.on_connect = on_connect
        client.username_pw_set("news", "news")
        client.connect("157.230.58.241", port=1883, keepalive=60)
        client.publish("server/",host)

except KeyboardInterrupt:
        print("\nCtrl+C pressionado, encerrando aplicacao e saindo...")
        sys.exit(0)
