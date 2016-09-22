# Eventex

Sistema de Eventos encomendado pela Morena.

[![Build Status](https://travis-ci.org/lays147/Eventex.svg?branch=master)](https://travis-ci.org/lays147/Eventex)

## Como desenvolver?
1.  Clone o Repositório
2. Crie um VirtualEnv com Python 3.5
3. Ative o seu VirtualEnv
4. Instale as dependências
5. Configure a instância com o .env
6. Execute os testes
```console
git clone git@github.com:lays147/Eventex.git wtt
cd python -m venv .wttd
source .wtt/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```
## Como fazer o deploy?
1. Crie uma instância no Heroku
2. Envie as configurações para o Heroku
3. Defina uma SECRET_KEY segura para a instância
4. Defina DEBUG=False
5. Configure o serviço de E-mail
6. Envie o código para o Heroku
```
heroku config myinstance
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
#configuro o email
git push heroku master
```