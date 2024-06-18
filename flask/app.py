from flask import Flask, request, render_template, url_for, redirect
import psycopg2
from psycopg2 import sql
app = Flask(__name__)
# Configurações do banco de dados
DB_HOST = 'viaduct.proxy.rlwy.net'
DB_PORT = '46527'
DB_USER = 'postgres'
DB_PASSWORD = 'giUBHopOxjPBoyFiKrleHbNGGXCUPDga'
DB_NAME = 'railway'
@app.route('/')
def index():
    return render_template('index.html')



@app.route('/adm')
def adm():
    return render_template('adm.html')
@app.route('/noticia1')
def noticia1():
    return render_template('noticia1.html')
@app.route('/noticia2')
def noticia2():
    return render_template('noticia2.html')
@app.route('/evento1')
def evento1():
    return render_template('evento1.html')
@app.route('/evento2')
def evento2():
    return render_template('evento2.html')
@app.route('/vereventos')
def vereventos():
    return render_template('vereventos.html')
    
@app.route('/controlebanco')
def controlebanco():
    return render_template('controlebanco.html')
@app.route('/admin_login', methods=['POST'])
def admin_login():
    login = request.form['admin-login']
    password = request.form['admin-password']
    
    # Verifique as credenciais
    correct_login = 'adm'
    correct_password = 'senha123'
    
    if login == correct_login and password == correct_password:
        return redirect(url_for('controlebanco'))
    else:
        return redirect(url_for('adm'))
    
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
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
       
        # Verifica se todos os campos obrigatórios estão preenchidos quando menor de idade
        
        # Conecta ao banco de dados PostgreSQL
        connection = psycopg2.connect(host=DB_HOST,
                                      port=DB_PORT,
                                      user=DB_USER,
                                      password=DB_PASSWORD,
                                      database=DB_NAME)
        cursor = connection.cursor()
        try:
            # Insere os dados na tabela oficial
            query = sql.SQL("INSERT INTO oficial (cpf, name, tell, gender, email, idade, nameresp, cpfresp, tellresp, emailresp) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
            cursor.execute(query, (cpf, name, tell, gender, email, idade, nameresp, cpfresp, tellresp, emailresp))
            connection.commit()
            return "Cadastro realizado com sucesso!"
        
        except psycopg2.Error as e:
            # Em caso de erro, faz rollback e exibe uma mensagem de erro
            connection.rollback()
            return "Ocorreu um erro ao cadastrar: " + str(e)
        
        finally:
            # Fecha a conexão com o banco de dados
            cursor.close()
            connection.close()
    # Se o método for GET, renderiza o formulário de cadastro
    return render_template('cadastro.html')
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
        # Remove o cliente da tabela oficial
        query = sql.SQL("DELETE FROM oficial WHERE cpf = %s")
        cursor.execute(query, (cpf,))
        connection.commit()
        return "Cliente removido com sucesso!"
    
    except psycopg2.Error as e:
        # Em caso de erro, faz rollback e exibe uma mensagem de erro
        connection.rollback()
        return "Ocorreu um erro ao remover o cliente: " + str(e)
    
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
        # Verifica se o cliente está na tabela oficial
        query = sql.SQL("SELECT name FROM oficial WHERE cpf = %s")
        cursor.execute(query, (cpf,))
        result = cursor.fetchone()
        name = result[0] if result else ""
        return render_template('controlebanco.html', verificarName=name, verificarCpf=cpf)
    
    except psycopg2.Error as e:
        # Em caso de erro, faz rollback e exibe uma mensagem de erro
        connection.rollback()
        return "Ocorreu um erro ao verificar o cliente: " + str(e)
    
    finally:
        # Fecha a conexão com o banco de dados
        cursor.close()
        connection.close()
if __name__ == '__main__':
    app.run(debug=True)