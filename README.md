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
<a href="https://dev.mysql.com/downloads/installer">MySQL Server</a> _(para ejecutar localmente, por defecto, user: root / password: root)_

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
URL local: <a href="http://127.0.0.1:5000/">http://127.0.0.1:5000/</a>

### Tecnología usada
API construida en Python3 + Flask. <br>
Base de datos MySQL.<br>
Hosting API en Google App Engine con instancia MySQL 5.7.<br>

