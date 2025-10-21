# Flask-Mini-API

## 📖 Descrição
Este projeto é uma Mini API em Python com Flask, criada para o TDE — Módulo 1: Organização e Versionamento.

## ⚙️ Instalação
```bash
git clone https://github.com/MarvioSants/Flask-Mini-API.git
cd Flask-Mini-API
python -m venv marvio
source marvio/Script/activate                               
pip install -r requirements.txt

#adcionar usuário
Invoke-WebRequest -Uri "http://127.0.0.1:5000/users" -Method POST -Body '{"name":"Marvio","email":"marvio@example.com"}' -ContentType "application/json"

#editar usuario
Invoke-WebRequest -Uri "http://127.0.0.1:5000/users/1" -Method PUT -Body '{"name":"Marvio Santos","email":"marvio.santos@example.com"}' -ContentType "application/json"

#deletar usuário
Invoke-WebRequest -Uri "http://127.0.0.1:5000/users/1" -Method DELETE




