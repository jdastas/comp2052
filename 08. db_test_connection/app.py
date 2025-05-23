from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)
# Configuración de la conexión
db = mysql.connector.connect(
 host="localhost",
 user="root",
 password="root",
 database="test_db"
)

cursor = db.cursor()

@app.route('/')
def index():
 return "Conexión exitosa con la base de datos"

# Crear datos
@app.route('/create', methods=['POST'])
def create_user():
    data = request.json
    sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
    values = (data['name'], data['email'])
    cursor.execute(sql, values)
    db.commit()
    return jsonify({"message": "Usuario creado"}), 201

 # Leer datos
@app.route('/users', methods=['GET'])
def get_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return jsonify(users)

if __name__ == "__main__":
    app.run(debug=True)