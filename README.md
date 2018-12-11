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


#testando a API, no navegador acessar a url:
http://127.0.0.1:8000/api/
