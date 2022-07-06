from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('home.html')

@app.route('/metodos')
def metodos():
  metodos = [
    {'titulo':'m1','nome':'Método Pomodoro','descricao':'Esta técnica consiste em 25 minutos de concentração, seguidos de 5 minutos de descanso: essa é a base do método Pomodoro de estudo. Com isso, é possível driblar distrações e ter mais foco para estudar, de forma simples e prática. Ou seja, basta dividir as tarefas em intervalos curtos, enquanto faz pausas frequentes para respirar e relaxar.'},
  {'titulo':'m2','nome':'Método Robinson (EPL2R)', 'descricao':'Esse método consiste em seguir cinco etapas. Na primeira, é necessário explorar todo o conteúdo. Depois, inicia-se a fase das perguntas. O terceiro passo consiste em uma leitura mais aprofundada do material. Feito isso, é a vez do primeiro R, de Rememorar. Por último, você deve repassar tudo o que estudou. '},
  {'titulo':'m3','nome':'Estudo intercalado', 'descricao':'Como o nome sugere, o estudo intercalado consiste em intercalar os conteúdos. Ou seja, em um dia, você estuda matemática. No outro, língua portuguesa. E assim por diante. Para isso, você deve fazer uma programação, porque é necessário dedicar mais de um dia para cada matéria. '}]
  return render_template('metodos.html', metodos=metodos)

@app.route('/aluno', methods=['POST'])
def aluno():
  usuario = request.form.get("usuario")
  senha = request.form.get("senha")
  tarefas = [
    {'titulo':'t1','nome':'Estudar a escravidão no Brasil', 'materia':'História', 'descricao':'Estudar o conteúdo dado pelo professor nos dias 23 e 30 de junho. Utilizar os slides disponibilizados por ele e ler as página do livro de 103 à 132.'},
     {'titulo':'t2','nome':'Atividade sobre análise combinatória', 'materia':'Matemática', 'descricao':'Atividade sobre os capítulos 2 e 3 do livro. Será disponibilizada no google sala de aula. deve-se copiar as questões e os cálculos no caderno e entregar para o professor no dia 06 de julho.'}]
  return render_template('aluno.html', tarefas=tarefas, usuario=usuario, senha=senha)


@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/cadastro')
def cadastro():
  return render_template('cadastro.html')

@app.route('/sugestoes')
def sugestoes():
  return render_template('sug.html')
  
@app.route('/recebe_sugestoes', methods=['GET'])
def dados():
  nome = request.args.get("nome")
  email = request.args.get("email")
  sugestao = request.args.get("sugestao")
  enviar = request.args.get("enviar")
  return render_template('sugr.html', nome=nome, email=email, sugestao=sugestao, enviar=enviar)

@app.route('/sobrenos')
def sobre():
  return render_template('sobre.html')


@app.route('/entrar', defaults={"id":"digite o valor 1 ou 2"})
@app.route('/entrar/<id>')
def dado(id):
  id = int(id)
  if id == 1:
    return render_template('cadastro.html', id=id)
  elif id == 2:
    return render_template('login.html', id=id)
  else:
    return render_template('entrar.html')
app.run(host='0.0.0.0', port=81)