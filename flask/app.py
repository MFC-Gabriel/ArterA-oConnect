from flask import Flask, redirect, request, render_template, url_for, flash
import psycopg2

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necessário para usar flash messages

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
def adm():
    return render_template('adm.html')

@app.route('/noticia1')
def noticia1():
    return render_template('notica1.html')

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

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/cadastro', methods=['POST'])
def cadastro_post():
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

    if idade == "Menor" and (nameresp == "" or cpfresp == "" or tellresp == "" or emailresp == ""):
        flash("Existem campos obrigatórios incompletos", "error")
        return redirect(url_for('cadastro'))

    connection = psycopg2.connect(host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
    cursor = connection.cursor()

    try:
        query = "INSERT INTO oficial (cpf, name, tell, gender, email, idade, nameresp, cpfresp, tellresp, emailresp) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (cpf, name, tell, gender, email, idade, nameresp, cpfresp, tellresp, emailresp))
        connection.commit()
        flash("Cadastro realizado com sucesso!", "success")
    except Exception as e:
        connection.rollback()
        flash("Ocorreu um erro ao cadastrar: " + str(e), "error")
    finally:
        cursor.close()
        connection.close()

    return redirect(url_for('index'))

@app.route('/remocao', methods=['POST'])
def remocao():
    cpf = request.form['excludeCpf']

    connection = psycopg2.connect(host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
    cursor = connection.cursor()

    try:
        query = "DELETE FROM oficial WHERE cpf = %s"
        cursor.execute(query, (cpf,))
        connection.commit()
        flash("Cliente removido com sucesso!", "success")
    except Exception as e:
        connection.rollback()
        flash("Ocorreu um erro ao remover: " + str(e), "error")
    finally:
        cursor.close()
        connection.close()

    return redirect(url_for('index'))

@app.route('/verificar', methods=['POST'])
def verificar():
    cpf = request.form['verificarCpf']

    connection = psycopg2.connect(host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
    cursor = connection.cursor()

    try:
        query = "SELECT name FROM oficial WHERE cpf = %s"
        cursor.execute(query, (cpf,))
        result = cursor.fetchone()
        name = result[0] if result else ""
        return render_template('controlebanco.html', verificarName=name, verificarCpf=cpf)
    except Exception as e:
        connection.rollback()
        flash("Ocorreu um erro ao verificar cliente: " + str(e), "error")
    finally:
        cursor.close()
        connection.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
