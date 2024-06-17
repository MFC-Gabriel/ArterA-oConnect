import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host='viaduct.proxy.rlwy.net',
        user='postgres',
        password='giUBHopOxjPBoyFiKrleHbNGGXCUPDga',
        database='railway',
        port='46527'
    )


    
def add_client(data):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    query = """
        INSERT INTO oficial (cpf, name, tell, gender, email, idade, nameresp, cpfresp, tellresp, emailresp, genderresp)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, data)
    
    connection.commit()
    cursor.close()
    connection.close()
    
def delete_client(cpf):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    query = "DELETE FROM oficial WHERE cpf = %s"
    cursor.execute(query, (cpf,))
    
    connection.commit()
    cursor.close()
    connection.close()
    
def search_clients(name):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    query = "SELECT name FROM oficial WHERE cpf LIKE %s"
    cursor.execute(query, (f"%{cpf}%",))
    
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    
    return results