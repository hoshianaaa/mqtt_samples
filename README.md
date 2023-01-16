# mqtt_samples

## mqttとは

- TCP/IPによるPub/Sub型データ配信モデルの軽量なデータ配信プロトコル
- brokerを介してクライアント同士がデータをやり取り

## mqtt使用の流れ

- ブローカ立ち上げ(`mosquitto`をインストールでブローカが自動で立ち上がる)
- mosquitto-clientでコマンドラインから,mqttの相互通信ができる
- ブラウザからmqttのデータを通信する場合`MQTT.js`を使用(Websocketでデータをやり取りする,ブローカにWebSocket受信設定が必要)

