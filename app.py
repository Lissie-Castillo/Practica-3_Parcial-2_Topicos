from flask import Flask,render_template,request,redirect
import mysql.connector

app = Flask(__name__)
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user ="root",
        password="",
        database="control_tareas"

    )
@app.route('/')
def home():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tareas2")
    tareas = cursor.fetchall()
    conn.close()
    return render_template('index.html', actividades=tareas)

@app.route('/add', methods=['POST'])
def add():
    #se instancian dos variables para poder mandar dos datos sin probocar un null que cause error en la conexión 
    actividad = request.form['actividad']  
    fecha = request.form['fecha'] 
    estatus = request.form['estatus']  
    prioridad = request.form['prioridad'] 
    puntaje = request.form['puntaje'] 

    conn = get_db_connection()
    cursor = conn.cursor()
    #se insertan los valores 
    cursor.execute("INSERT INTO tareas2 (Nombre, Fecha, Estatus, Prioridad, Puntaje) VALUES (%s, %s, %s, %s,%s)", (actividad, fecha, estatus, prioridad, puntaje))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tareas2 WHERE ID = %s", (id,))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tareas2 SET Nombre = %s WHERE ID = %s", (request.form['actividad'], id))
    conn.commit()
    conn.close()
    return redirect('/')