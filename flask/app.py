from flask import Flask, redirect, request, render_template, url_for, flash
import psycopg2

app = Flask(__name__)

# Configurações do banco de dados
DB_HOST = 'viaduct.proxy.rlwy.net'
DB_PORT = '46527'
DB_USER = 'postgres'
DB_PASSWORD = 'giUBHopOxjPBoyFiKrleHbNGGXCUPDga'
DB_NAME = 'railway'

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/adm')
def index():
    return render_template('adm.html')

@app.route('/noticia1')
def index():
    return render_template('notica1.html')

@app.route('/noticia2')
def index():
    return render_template('noticia2.html')

@app.route('/evento1')
def index():
    return render_template('evento1.html')

@app.route('/evento2')
def index():
    return render_template('evento2.html')

@app.route('/vereventos')
def index():
    return render_template('vereventos.html')

@app.route('/cadastro')
def index():
    return render_template('cadastro.html')
    
@app.route('/teste', methods=['POST'])
def teste():
    email = request.form['emailEntrada']

            # Conecta ao banco de dados PostgreSQL
    connection = psycopg2.connect(host=DB_HOST,
                                  port=DB_PORT,
                                  user=DB_USER,
                                  password=DB_PASSWORD,
                                  database=DB_NAME)
    cursor = connection.cursor()

    try:
        # Insere o email na tabela contatoemail
        query = "INSERT INTO oficial (cpf, name, tell, gender, email, idade, nameresp, cpfresp, tellresp, emailresp) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (cpf, name, tell, gender, email, idade, nameresp, cpfresp, tellresp, emailresp ))
        connection.commit()
        return render_template(url_for('oficial'))  # Redireciona para a página inicial após o envio bem-sucedido
    except Exception as e:
        # Em caso de erro, faz rollback e exibe uma mensagem de erro
        connection.rollback()
        return "Ocorreu um erro ao enviar o email: " + str(e)
    finally:
        # Fecha a conexão com o banco de dados
        cursor.close()
        connection.close()


@app.route('/cadastro', methods=['POST'])
def cadastro():
    # Obtém informações do formulário enviado pelo formulário
    email = request.form['registerEmail']
    cpf = request.form['registerCpf']
    name = request.form['registerName']
    tell = request.form['registerTell']
    gender = request.form['registerGender']
    idade = request.form['idade']
    nameresp = request.form['registerNameResp']
    cpfresp = request.form['registerCpfResp']
    tellresp = request.form['registerTellResp']
    emailresp = request.form['registerEmailResp']
    genderresp = request.form['registerGenderResp']
   
    # Conecta ao banco de dados PostgreSQL
    connection = psycopg2.connect(host=DB_HOST,
                                  port=DB_PORT,
                                  user=DB_USER,
                                  password=DB_PASSWORD,
                                  database=DB_NAME)
    cursor = connection.cursor()

    try:
        # Insere o email na tabela contatoemail
        query = "INSERT INTO oficial (cpf, name, tell, gender, email, idade, nameresp, cpfresp, tellresp, emailresp) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (cpf, name, tell, gender, email, idade, nameresp, cpfresp, tellresp, emailresp ))
        if(idade == "Menor" and (nameresp =="" or cpfresp =="" or tellresp=="" or emailresp=="")):
            return "Existem campos obrigatórios imcompletos"
        else:
            

            connection.commit()
            


        
        return render_template(url_for('oficial'))  # Redireciona para a página inicial após o envio bem-sucedido
    except Exception as e:
        # Em caso de erro, faz rollback e exibe uma mensagem de erro
        connection.rollback()
        return "Obrigado por se Cadastrar! "
    finally:
        # Fecha a conexão com o banco de dados
        cursor.close()
        connection.close()

@app.route('/remocao', methods=['POST'])
def remocao():
    # Obtém informações do formulário enviado pelo formulário
    cpf = request.form['excludeCpf']
   
    # Conecta ao banco de dados PostgreSQL
    connection = psycopg2.connect(host=DB_HOST,
                                  port=DB_PORT,
                                  user=DB_USER,
                                  password=DB_PASSWORD,
                                  database=DB_NAME)
    cursor = connection.cursor()

    try:
        query = "DELETE FROM oficial WHERE cpf = %s"
        cursor.execute(query, (cpf,))
        connection.commit()
        return "Cliente removido com Sucesso "  # Redireciona para a página inicial após o envio bem-sucedido
    except Exception as e:
        # Em caso de erro, faz rollback e exibe uma mensagem de erro
        connection.rollback()
        return "Cliente removido com Sucesso "
    finally:
        # Fecha a conexão com o banco de dados
        cursor.close()
        connection.close()


@app.route('/verificar', methods=['POST'])
def verificar():
    # Obtém informações do formulário enviado
    cpf = request.form['verificarCpf']
   
    # Conecta ao banco de dados PostgreSQL
    connection = psycopg2.connect(host=DB_HOST,
                                  port=DB_PORT,
                                  user=DB_USER,
                                  password=DB_PASSWORD,
                                  database=DB_NAME)
    cursor = connection.cursor()

    try:
        query = "SELECT name FROM oficial WHERE cpf = %s"
        cursor.execute(query, (cpf,))
        result = cursor.fetchone()
        name = result[0] if result else ""
        return render_template('controlebanco.html', verificarName=name, verificarCpf=cpf)
    except Exception as e:
        # Em caso de erro, faz rollback e exibe uma mensagem de erro
        connection.rollback()
        return "Ocorreu um erro ao verificar cliente: " + str(e)
    finally:
        # Fecha a conexão com o banco de dados
        cursor.close()
        connection.close()














if __name__ == '__main__':
    app.run(debug=True)


