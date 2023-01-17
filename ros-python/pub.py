#!usr/bin/env python
# -*- coding: utf-8 -*- 

import paho.mqtt.client as mqtt     # MQTTのライブラリをインポート
from time import sleep              # 3秒間のウェイトのために使う
import rospy
from std_msgs.msg import *

# ブローカーに接続できたときの処理
def on_connect(client, userdata, flag, rc):
  print("Connected with result code " + str(rc))

# ブローカーが切断したときの処理
def on_disconnect(client, userdata, rc):
  if rc != 0:
     print("Unexpected disconnection.")

# publishが完了したときの処理
def on_publish(client, userdata, mid):
  print("publish: {0}".format(mid))

def mqtt_pub(msg):
  global client
  client.publish("aaa/bbb",msg)    # トピック名とメッセージを決めて送信

def data_callback(msg):
  print(msg)

# メイン関数   この関数は末尾のif文から呼び出される
client = mqtt.Client()                 # クラスのインスタンス(実体)の作成
client.on_connect = on_connect         # 接続時のコールバック関数を登録
client.on_disconnect = on_disconnect   # 切断時のコールバックを登録
client.on_publish = on_publish         # メッセージ送信時のコールバック

client.connect("localhost", 1883, 60)  # 接続先は自分自身

# 通信処理スタート
client.loop_start()    # subはloop_forever()だが，pubはloop_start()で起動だけさせる

rospy.init_node("ros_mqtt_bridge")
rospy.Subscriber("data", UInt8MultiArray, data_callback)

# 永久に繰り返す
msg = "255" * 4000

r = rospy.Rate(100)

while True:
  r.sleep()
