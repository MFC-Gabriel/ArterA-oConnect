from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector


conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='TDE8'
)

cursor = conexao.cursor()

cursor.execute("ALTER TABLE cliente ADD COLUMN IF NOT EXISTS MaiorIdade VARCHAR(10)")
cursor.execute("ALTER TABLE cliente ADD COLUMN IF NOT EXISTS RespNome VARCHAR(255)")
cursor.execute("ALTER TABLE cliente ADD COLUMN IF NOT EXISTS RespCpf VARCHAR(255)")
cursor.execute("ALTER TABLE cliente ADD COLUMN IF NOT EXISTS RespTell VARCHAR(255)")
cursor.execute("ALTER TABLE cliente ADD COLUMN IF NOT EXISTS RespEmail VARCHAR(255)")
cursor.execute("ALTER TABLE cliente ADD COLUMN IF NOT EXISTS RespSexo VARCHAR(10)")


def validar_sexo(entrada):
    return len(entrada) == 0 or (len(entrada) == 1 and entrada.isalpha())

def get_validar_sexo_wrapper(entry):
    return i.register(lambda s: validar_sexo(s)), '%P'


def CadastrarCliente():
    Nome = e_Nome.get()
    Cpf = e_Cpf.get()
    Sexo = e_Sexo.get()
    Tell = e_Tell.get()
    Email = e_Email.get()
    
    MaiorIdade = idade_status.get()

    if Nome == '' or Cpf == '' or Sexo == '' or Tell == '' or Email == '' or MaiorIdade == '':
        messagebox.showinfo('STATUS CADASTRAR!', 'ERRO ao CADASTRAR cliente: Campos obrigatórios estão vazios.')
        return

    if not validar_sexo(Sexo):
        messagebox.showinfo('STATUS CADASTRAR!', 'ERRO ao CADASTRAR cliente: O campo Sexo deve conter apenas uma letra.')
        return
    try:
        if MaiorIdade == "0":  # Menor de idade
            RespNome = e_RespNome.get()
            RespCpf = e_RespCpf.get()
            RespTell = e_RespTell.get()
            RespEmail = e_RespEmail.get()
            RespSexo = e_RespSexo.get()
            
            if RespNome == '' or RespCpf == '' or RespTell == '' or RespEmail == '' or RespSexo == '':
                messagebox.showinfo('STATUS CADASTRAR!', 'ERRO ao CADASTRAR cliente: Campos do responsável legal estão vazios.')
                return

            if not validar_sexo(RespSexo):
                messagebox.showinfo('STATUS CADASTRAR!', 'ERRO ao CADASTRAR cliente: O campo Sexo do Responsável deve conter apenas uma letra.')
                return
            query = 'INSERT INTO cliente (Cpf, Nome, Tell, Sexo, Email, MaiorIdade, RespNome, RespCpf, RespTell, RespEmail, RespSexo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            val = (Cpf, Nome, Tell, Sexo, Email, MaiorIdade, RespNome, RespCpf, RespTell, RespEmail, RespSexo)
        else:
            query = 'INSERT INTO cliente (Cpf, Nome, Tell, Sexo, Email, MaiorIdade) VALUES (%s, %s, %s, %s, %s, %s)'
            val = (Cpf, Nome, Tell, Sexo, Email, MaiorIdade)

        cursor.execute(query, val)
        conexao.commit()
        messagebox.showinfo('STATUS INSERIR!', 'Cliente inserido com sucesso')
    except mysql.connector.Error as err:
        messagebox.showerror('Erro no Banco de Dados', f'Erro: {err}')
    finally:
        limpar_campos()


def limpar_campos():
    e_Nome.delete(0, END)
    e_Cpf.delete(0, END)
    e_Sexo.delete(0, END)
    e_Tell.delete(0, END)
    e_Email.delete(0, END)
    var1.set(0)
    var2.set(0)
    idade_status.set("")  # Limpa o status da idade
    
    # Limpa os campos do responsável legal
    e_RespNome.delete(0, END)
    e_RespCpf.delete(0, END)
    e_RespTell.delete(0, END)
    e_RespEmail.delete(0, END)
    e_RespSexo.delete(0, END)
    esconder_campos_responsavel()


def Checar():
    if var1.get() == 1 and var2.get() == 0:
        idade_status.set("0")  # Menor de idade
        MaiorIdade.config(text='NÃO, sou Menor de Idade')
        mostrar_campos_responsavel()
    elif var1.get() == 0 and var2.get() == 1:
        idade_status.set("1")  # Maior de idade
        MaiorIdade.config(text='SIM, sou Maior de Idade')
        esconder_campos_responsavel()
    elif var1.get() == 0 and var2.get() == 0:
        idade_status.set("")
        MaiorIdade.config(text='Você é Maior de Idade? :')
        esconder_campos_responsavel()
    else:
        idade_status.set("")
        MaiorIdade.config(text='Resposta Incoerente:')
        esconder_campos_responsavel()

def esconder_campos_responsavel():
    lbl_RespNome.place_forget()
    lbl_RespCpf.place_forget()
    lbl_RespTell.place_forget()
    lbl_RespEmail.place_forget()
    lbl_RespSexo.place_forget()
    e_RespNome.place_forget()
    e_RespCpf.place_forget()
    e_RespTell.place_forget()
    e_RespEmail.place_forget()
    e_RespSexo.place_forget()


def mostrar_campos_responsavel():
    lbl_RespNome.place(x='30', y='270')
    lbl_RespCpf.place(x='30', y='300')
    lbl_RespTell.place(x='30', y='330')
    lbl_RespEmail.place(x='30', y='360')
    lbl_RespSexo.place(x='30', y='390')
    e_RespNome.place(x='180', y='270')
    e_RespCpf.place(x='180', y='300')
    e_RespTell.place(x='180', y='330')
    e_RespEmail.place(x='180', y='360')
    e_RespSexo.place(x='180', y='390')


def DeletarCliente():
    Cpf = e_Cpf.get()

    if Cpf == '':
        messagebox.showwarning("Campo obrigatório", "O CPF do Cliente deve ser preenchido.")
        return

    confirmacao = messagebox.askyesno("Confirmação", f"Tem certeza de que deseja excluir o cliente com CPF {Cpf}?")
    if not confirmacao:
        return
    
    try:
        query = 'DELETE FROM cliente WHERE Cpf = %s'
        val = (Cpf,)
        cursor.execute(query, val)
        conexao.commit()
            
        if cursor.rowcount > 0:
            messagebox.showinfo("Sucesso", "Cliente excluído com sucesso!")
        else:
            messagebox.showwarning("Erro", "CPF do Cliente não encontrado.")
    
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao tentar excluir o cliente: {e}")
    
    finally:
        e_Cpf.delete(0, END)

def abrir_janela_consulta():
    janela_consulta = tk.Toplevel(i)
    janela_consulta.title("Consulta de Clientes")
    janela_consulta.geometry("2000x400")

    label_nome = tk.Label(janela_consulta, text="Nome do Cliente:")
    label_nome.pack(pady=10)
    
    entrada_nome = tk.Entry(janela_consulta)
    entrada_nome.pack(pady=5)
    
    botao_buscar = tk.Button(janela_consulta, text="Buscar", command=lambda: buscar_clientes(entrada_nome.get()))
    botao_buscar.pack(pady=10)

    colunas = ("CPF", "Nome", "Telefone", "Email", "Sexo", "MaiorIdade", "RespNome", "RespCpf", "RespTell", "RespEmail", "RespSexo")

    # Adicionando estilo para a Treeview
    style = ttk.Style()
    style.configure("Treeview", rowheight=30)
    style.configure("Treeview.Heading", font=("Arial", 10, "bold"))
    style.configure("Treeview", font=("Arial", 10), padding=5)

    tabela_resultados = ttk.Treeview(janela_consulta, columns=colunas, show='headings')
    tabela_resultados.pack(expand=True, fill=tk.BOTH, pady=20, padx=20)

    for col in colunas:
        tabela_resultados.heading(col, text=col)
        tabela_resultados.column(col, anchor=tk.CENTER, width=100)

    # Adicionando barra de rolagem
    scrollbar = ttk.Scrollbar(janela_consulta, orient=tk.VERTICAL, command=tabela_resultados.yview)
    tabela_resultados.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def buscar_clientes(parte_nome):
        for item in tabela_resultados.get_children():
            tabela_resultados.delete(item)

        if parte_nome == '':
            messagebox.showwarning("Campo obrigatório", "Você deve inserir parte do nome do cliente.")
            return
        
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='TDE8'
            )
            cursor = conn.cursor()

            query = "SELECT Cpf, Nome, Tell, Email, Sexo, MaiorIdade, RespNome, RespCpf, RespTell, RespEmail, RespSexo FROM cliente WHERE Nome LIKE %s"
            valor = (f"%{parte_nome}%",)
            cursor.execute(query, valor)
            
            for row in cursor.fetchall():
                tabela_resultados.insert('', tk.END, values=row)

            cursor.close()
            conn.close()

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao buscar clientes: {e}")


i = tk.Tk()
i.title('Administrar Clientes')
i.geometry('400x500')

Nome = Label(i, text='Nome:')
Nome.place(x='30', y='30')

Cpf = Label(i, text='Cpf:')
Cpf.place(x='30', y='60')

Sexo = Label(i, text='Sexo:')
Sexo.place(x='30', y='90')

Tell = Label(i, text='Telefone:')
Tell.place(x='30', y='120')

Email = Label(i, text='Email:')
Email.place(x='30', y='150')

MaiorIdade = Label(i, text='Você é Maior de Idade? :')
MaiorIdade.place(x='30', y='180')


var1 = tk.IntVar()
var2 = tk.IntVar()


idade_status = tk.StringVar()


c1 = tk.Checkbutton(i, text='NÃO', variable=var1, onvalue=1, offvalue=0, command=Checar)
c1.place(x='90', y='210')

c2 = tk.Checkbutton(i, text='SIM', variable=var2, onvalue=1, offvalue=0, command=Checar)
c2.place(x='150', y='210')


e_Nome = Entry(i)
e_Nome.place(x='180', y='30')

e_Cpf = Entry(i)
e_Cpf.place(x='180', y='60')

e_Sexo = Entry(i, validate='key', validatecommand=get_validar_sexo_wrapper(Sexo))
e_Sexo.place(x='180', y='90')

e_Tell = Entry(i)
e_Tell.place(x='180', y='120')

e_Email = Entry(i)
e_Email.place(x='180', y='150')


lbl_RespNome = Label(i, text='Nome do Responsável:')
lbl_RespCpf = Label(i, text='Cpf do Responsável:')
lbl_RespTell = Label(i, text='Telefone do Responsável:')
lbl_RespEmail = Label(i, text='Email do Responsável:')
lbl_RespSexo = Label(i, text='Sexo do Responsável:')

e_RespNome = Entry(i)
e_RespNome.place(x='180', y='270')

e_RespCpf = Entry(i)
e_RespCpf.place(x='180', y='300')

e_RespTell = Entry(i)
e_RespTell.place(x='180', y='330')

e_RespEmail = Entry(i)
e_RespEmail.place(x='180', y='360')


e_RespSexo = Entry(i, validate='key', validatecommand=get_validar_sexo_wrapper(Sexo))
e_RespSexo.place(x='180', y='390')


esconder_campos_responsavel()


CadastrarCliente = Button(i, text='Inserir', bg='darkgray', fg='white', command=CadastrarCliente)
CadastrarCliente.place(x='90', y='450')

DeletarCliente = Button(i, text='Deletar', bg='darkgray', fg='white', command=DeletarCliente)
DeletarCliente.place(x='150', y='450')

botao_consultar = tk.Button(i, text="Consultar Clientes", bg='darkgray', fg='white', command=abrir_janela_consulta)
botao_consultar.place(x='210', y='450')

i.mainloop()