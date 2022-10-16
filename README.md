# alura_webapp_flask
Criando uma aplicação web Flask - Alura

## Versões utilizadas:
Python: ~~3.9.9~~ 3.9.2   
Flask: 2.0.2  
PyCharm: ~~2021.3.2~~ 2022.2.3  
Bootstrap: ~~5.1.x~~ 5.2.2  

### pyenv

  - [tutorial install pyenv](https://gist.github.com/luzfcb/ef29561ff81e81e348ab7d6824e14404)

```bash
  cd alura_webapp_flask/
  pyenv install --list
  pyenv versions  
  pyenv install 3.9.2
  pyenv virtualenv 3.9.2 alura_webapp_flask  
  pyenv virtualenvs
  pyenv activate alura_webapp_flask
  pyenv local alura_webapp_flask
```

#### Libs
```bash
  pip install flask~=2.0.0
```


 - obs.:
   - ~= : versão compatível - pode ser qualquer versão mais atual que não quebre compatibilidade com a definida.
   - == : versão exata - define uma versão fixa que deve ser instalada (como vimos no vídeo).
   - != : exclusão de versão - define a versão que não é para instalar, pegando assim a mais atual sem ser a definida.
   - <= , >= : versão maior ou igual e menor ou igual - ajuda a restringir versões, inclusive a definida.
   - < , > : versão maior ou menor - ajuda a restringir versões, excluindo a definida.

##### Requeriments
```bash
flask==2.0.2  
```


## Apresentação da proposta

o Flask é um framework que foi lançado em 2010  
principais características: é a sua simplicidade, a sua rapidez e a sua eficiência.  

[documentação do Flask](https://flask.palletsprojects.com/en/2.1.x/)  

[Artigo Django ou Flask: Características, semelhanças e diferenças](https://www.alura.com.br/artigos/django-ou-flask)  


## Jogoteca

### A primeira aplicação

 Nosso projeto vai ser um site chamado Jogoteca, uma aplicação chamada Jogoteca, e vai se tratar de um site que exibe lista de jogos, então vai exibir lá nome do jogo, a plataforma o qual o jogo pertence, o console o qual o jogo pertence, vai possibilitar também que cadastremos novos jogos e que façamos login, e só quem tiver login vai conseguir acessar as páginas de lista de jogos de criar um novo jogo.


 - vamos ter o Flask, framework Flask, como o servidor.
 - criar um novo arquivo.py que é aonde vamos deixar o projeto


 - ⚠️Só que tem um problema, porque o Flask ele não é uma biblioteca embutida do Python, é uma biblioteca que temos que baixar, temos que fazer o download disso, então vamos fazer o download.  
vamos usar o instalador pip:
   - pip install flask==2.0.2


- para fazer rodar essa aplicação temos que terminar isso daqui com **app.run()**
  - vamos fazer isso a partir do `@app.routee vamos criar uma nova rota, e daí precisamos nomear essa rota, então eu vou colocar’/inicio’`


### Rotas

 - **/**
   - lista os jogos  
   
      
 - **/novo**
   - formulario para adicionar novos dados  

 
 - **/criar**
   - recebe o post com os dados do **/novo** e depois redireciona para **/** novamente


### Estilização
 - utilizado [bootstrap](https://getbootstrap.com/) v5.2.2
 - 