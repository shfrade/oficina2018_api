# oficina2018_api
API em DJANGO (+django rest framework)
Aos alunos,
Preparação:
Criar UMA pasta, dentro dela clonar:
1. Clonar a API (django) e testar: 
https://github.com/shfrade/oficina2018_api
2. Clonar o APP (angular)
https://github.com/shfrade/oficina2018_app
comandos:
cd c:\projetos 
mkdir oficina
cd oficina
git clone https://github.com/shfrade/oficina2018_api api
git clone https://github.com/shfrade/oficina2018_app app
cd api
py -m venv myvenv
myvenv\scripts\activate
pip install -r requirements.txt
py manage.py makemigrations produtos
py manage.py migrate

É opcional criar um usuário admin. 
py manage.py createsuperuser

# Rodando o servidor
py manage.py runserver 


# testando a API, no navegador acessar a url:
http://127.0.0.1:8000/api/

# Agora passando para a API
Instalar o NPM ( https://nodejs.org/en/download/ )
e executar o comando no console (reabrir o mesmo)
node -v
Entrar na pasta do APP (clonado lá em cima)
e digitar no console:
npm install 
npm install -g @angular/cli
ng serve
acessar na url: http://localhost:4200/ (garantindo que AMBOS SERVIDORES ESTÃO RODANDO AO MESMO TEMPO API E APP)
