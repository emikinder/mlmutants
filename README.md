# mlmutants
Stats
https://xmen-283720.rj.r.appspot.com/stats <br>
<br>
Mutants
https://xmen-283720.rj.r.appspot.com/mutants/
<br>
<br>
### Instrucciones
#### Instalaciones necesarias
<a href="https://www.python.org/downloads/release/python-385">Python 3.8.5</a> <br>
<a href="https://dev.mysql.com/downloads/installer">MySQL Server</a> (user: root / password: root)

Clonar repo https://github.com/emikinder/mlmutants.git <br>
```
pip3 install -r requirements.txt
```
En directorio mlmutants/api: <br>
```
python3 createDB.py
```
```
python3 main.py
```


### Tecnología usada
API construida en Python3 + Flask.
Base de datos MySQL.
Hosting API en Google App Engine con instancia MySQL 5.7.

