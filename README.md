# RUNOS CUSTOM

CUSTOM RUNOS CONFIG BY hakenlaken 

Добавлены следующие метрики:
- pkt_out_of_packets_ (Тип OpenFlow msg – of13::OFPT_PACKET_OUT)
- flow_mod_packets_ (Тип OpenFlow msg – of13::OFPT_FLOW_MOD)
- flow_removed_packets_ (Тип OpenFlow msg – of13::OFPT_FLOW_REMOVED)

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
<img width="1013" alt="Снимок экрана 2022-04-04 в 16 14 53" src="https://user-images.githubusercontent.com/70706464/161556027-ac867ac1-005c-402f-94b8-1d76fe1dedf5.png">
