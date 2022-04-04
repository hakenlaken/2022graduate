# RUNOS CUSTOM

CUSTOM RUNOS CONFIG BY hakenlaken 

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
<img width="1012" alt="from ubuntu" src="https://user-images.githubusercontent.com/70706464/161530073-7197ca55-b396-491c-a8aa-02768ea1a0c5.png">
