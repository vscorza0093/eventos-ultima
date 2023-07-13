# eventos-ultima

Projeto feito em aula

Até o momento estruturamos o front-end do site, podemos replicar a condição atual para ampliá-lo o quanto for necessário

Começaremos a estruturar uma modelagem do sistema, ou seja, representar diversos eventos, como categorias de um site, por exemplo, em um banco de dados.

É interessante que exista um trabalho inicial, posterior a criação dos bancos de dados, para definir sua estrutura de base, pensando com cuidado todas as necessidades e recursos disponíveis na nossa aplicação que devem transmitir ou receber informações do banco de dados.

No momento estamos criando as tabelas do banco de dados de maneira manual, mas utilizando Django existem classes disponíveis para que essa função de criar todo o banco de dados seja realizada de maneira automatizada e completamente integrada à nossa aplicação.

## Trabalhando com Django

Django é um framework para desenvolvimento web, baseado em Python, que utiliza o padrão Model-Template-View.

Para instalar ou atualizar o Django, usamos o pip, como uma biblioteca qualquer.

```
`pip install django` ou `pip install -U django`
```

A diferença é que podemos utilizar o comando `django-admin` para criar uma estrutura de projeto, que já contará com diretórios específicos para salvar outros diretórios, banco de dados, arquivos HTML, css, JavaScript entre outras questões de estrutura de projeto.

PS: Não podemos utilizar caracteres especiais no nome do projeto

Para iniciarmos o projeto, executamos o seguinte código

```
django-admin startproject nomedoprojeto .
```

Usamos o caractere `.` no final do comando para informar ao comando que queremos que todos os diretórios sejam criados dentro do diretório que estamos criando no momento de executar o comando django-admin

Nosso projeto foi inicializado. O único arquivo que ficou para fora da nova pasta criada foi o `manage.py`, que é justamente o arquivo principal para rodar nosso programa.
O arquivo `settings.py` é o coração da nossa aplicação Django, onde estão contidas todas as configurações do nosso projeto.

Django é uma biblioteca baseada em aplicações, que são os módulos do nosso sistema, no caso do sistema de Petshop, por exemplo, temos o módulo de agendamento, um módulo para salvar os Petshops que fazem parte da rede, um módulo de venda de outros serviços, cadastro de usuários, entre outras necessidades da aplicação.

O Django nos fornece diversos argumentos (subcomandos), alguns auto-explicativos, para a execução da nossa aplicação.
Se executarmos `python .\manage.py` receberemos a seguinte lista como retorno:

```
[auth]
    changepassword
    createsuperuser

[contenttypes]
    remove_stale_contenttypes

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    optimizemigration
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver

[sessions]
    clearsessions

[staticfiles]
    collectstatic
    findstatic
    runserver
```

O comando `runserver` é utilizado literalmente para criar um servidor local (servidor de desenvolvimento) para que possamos testar nossa aplicação web

`python .\manage.py runserver`

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
July 13, 2023 - 00:05:47
Django version 4.2.3, using settings 'masmorraGames.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

Se acessarmos a aplicação pelo endereço indicado pelo Django, receberemos o aviso e as respectivas respostas desse acesso.

```
[13/Jul/2023 00:07:16] "GET / HTTP/1.1" 200 10664
Not Found: /favicon.ico
Not Found: /products.json
[13/Jul/2023 00:07:16] "GET /favicon.ico HTTP/1.1" 404 2117
[13/Jul/2023 00:07:16] "GET /products.json?limit=250 HTTP/1.1" 404 2133
```

### Language Code & Time Zone

O Django possui um sistema de internacionalização, então é extremamente simples trabalhar com qualquer idioma e fuso horário em uma aplicação web construída com Django.

Por padrão, o Languace Code virá como `en-US` e o Time Zone `UTC`, basta mudarmos respectivamente para `pt-BR` e `America/Sao_Paulo` que o idioma da página e o fuso horário já serão automaticamente reconhecidos.

```python
LANGUAGE_CODE = "ja-JP"

TIME_ZONE = "America/Sao_Paulo"
```

### Debug

Quando estamos em modo de desenvolvimento, devemos deixar o Debug dentro do arquivo `settings.py` como _True_ pois qualquer erro que for pego no momento da execução, será exibido na tela com informações adicionais, ou seja, de maneira um pouco mais legível.

### Módulos

Para cada módulo django que precisarmos criar, devemos utilizar o comando `python .\manage.py startapp nomedomodulo`

Um novo diretório será criado e todos os seus arquivos de base também serão criados neste momento.
Uma breve explicação sobre os arquivos criados:

```
admin.py -> Dentro deste arquivo nós temos informações pré-configuradas de interface
apps.py -> Configurações gerais da aplicação. Cada módulo possui suas individualidades.
models.py -> Neste arquivo definimos que tabelas o nosso módulo terá.
tests.py -> Arquivo para automatização de testes. O código que irá testar nosso código.
views.py -> Este arquivo define o que o nosso usuário irá enxergar na tela.
urls.py -> Todo acesso à visualização será definido neste arquivo. Todos os caminhos e endereços são registrados neste arquivo.
templates.py -> Template é o HTML em si, onde trabalhamos a possibilidade da nossa página ser dinâmica.
```

### Criando um novo módulo

Após executarmos o comando `python .\manage.py startapp eventos` para criar um novo módulo chamado "eventos", iremos inserir o seguinte código no arquivo `views.py`

```python
from django.http import HttpResponse


def inicio(request):
    print("Página inicial")
```

Em seguida inicializaremos nosso servidor com o comando `python .\manage.py runserver`. Porém, ao abrir nossa aplicação, a página irá retornar um erro.

Toda página da web precisa indicar um HTTP Response.

Para configurar uma nova página em um site nós precisamos seguir os passos:

1. Criar uma URL;
2. A URL deverá apontar para uma função (view), dentro do arquivo `views.py`;
3. Esse arquivo deve ser uma função que recebe um parâmetro chamado `request` que representa a requisição atual do usuário que está acessando a página.
4. Retornar um HTTP Response

No arquivo `urls.py` temos o seguinte código:

```python
urlpatterns = [
    from django.contrib import admin
    from django.urls import path
    from eventos.views import inicio

    path('', inicio),
    path("admin/", admin.site.urls),
]
```

O primeiro `path` que está em branco, representa a página inicial, que, no caso, é uma função provida do arquivo viwes oriundo do módulo eventos. Deixaremos `admin` para depois.

Após atualizarmos nosso código, a página irá abrir sem erros e imprimirá um 'OK' na tela do usuário e o print irá aparecer no nosso terminal de desenvolvimento.

```python
from django.http import HttpResponse


def inicio(request):
    print("Página inicial")
    return HttpResponse('OK')
```

Acabamos de fazer a conexão entre nossa nova página e nossa aplicação django, configurando o caminho da nossa página após o domínio.
A URL é o caminho para acessar a página e a View é a função que será ativada quando esse caminho for acessado.

### Requests

VOLTAR AULA A PARTIR DOS 25 MINUTOS E 30 SEGUNDOS DE VÍDEO.
