# RUNOS CUSTOM

CUSTOM RUNOS CONFIG BY hakenlaken 

Добавлены следующие метрики:
- pkt_out_of_packets_ (Тип OpenFlow msg – of13::OFPT_PACKET_OUT)
- flow_mod_packets_ (Тип OpenFlow msg – of13::OFPT_FLOW_MOD)
- flow_removed_packets_ (Тип OpenFlow msg – of13::OFPT_FLOW_REMOVED)
- echo_reply_packets_ (Тип OpenFlow msg – of13::OFPT_ECHO_REPLY)
- echo_request_packets_ (Тип OpenFlow msg – of13::OFPT_ECHO_REQUEST)

запуск:
```
nix-shell 
cd build
cmake ..
make
cd ..
```
mininet:
```
sudo mn --topo=tree,depth=2,fanout=5 --switch=ovsk,protocols=OpenFlow13 --controller=remote
```

REST запрос для проверки, что все метрики считаются:
```
watch -n 1 "curl -X GET http://127.0.0.1:8000/of-server/info/"
```
Пример вывода:
<img width="1023" alt="Снимок экрана 2022-04-21 в 21 30 58" src="https://user-images.githubusercontent.com/70706464/164531483-ee3d5f3e-0455-4a01-ac6c-da01ce76b7aa.png">
