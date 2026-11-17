from flask import Flask, jsonify, render_template, request, redirect, url_for, flash
import pymysql
import pymysql.cursors
from flask_cors import CORS




app = Flask(__name__)
CORS(app)

CORS(app, origins=["http://localhost:3000"])

def connect_to_db(): 

    return pymysql.connect( 

        host='localhost', 

        user='root', 

        password='', 

        database='elian', 

        cursorclass=pymysql.cursors.DictCursor, 

        ssl_disabled=True 

    ) 

@app.route ('/')
def home():
    return render_template("index.html")


@app.route ('/sesion')
def sesion(): 
    return render_template("sesion.html") 
  
# pacientes

@app.route ('/pacientes', methods=["GET","POST"])
def pacientes():
     if request.method=="POST": 

        pac_id =request.form["pac_id "] 

        pac_nombres=request.form["pac_nombres"] 

        pac_apellidos=request.form["pac_apellidos"] 
        
        pac_fechanacimiento=request.form["pac_fechanacimiento"]
        
        pac_sexo=request.form["pac_sexo"]

        try: 

            conn = connect_to_db() 

            cur = conn.cursor()  

            cur.execute("INSERT INTO pacientes (pac_id, pac_nombres, pac_apellidos, pac_fechanacimiento, pac_sexo ) VALUES (%s, %s, %s, %s, %s)", 

                        (pac_id, pac_nombres, pac_apellidos, pac_fechanacimiento, pac_sexo)) 

            conn.commit() 

            cur.close() 

            conn.close() 

            return redirect(url_for('pacientes')) 

        except Exception: 

            return redirect(url_for('pacientes')) 
     return render_template("pacientes.html")
 
 
 # consulta pacientes
 
@app.route('/conpacientes') 

def conpacientes(): 

    try: 

        conn = connect_to_db() 

        cur = conn.cursor() 

        cur.execute("SELECT * FROM pacientes") 

        data = cur.fetchall() 

        cur.close() 

        conn.close() 

        return render_template('conpacientes.html', pacientes=data) 

    except Exception as e: 

        return render_template('index.html', pacientes=[]) 
    

# Editar Pacientes

@app.route('/edit/<id>', methods=['GET', 'POST']) 
def edit_pacientes(id): 
    try: 
        conn = connect_to_db() 
        cur = conn.cursor() 
        
        cur.execute("SELECT * FROM pacientes WHERE pac_id=%s", (id,)) 
        pacientes = cur.fetchone() 
        cur.close() 
        conn.close() 
    except Exception as e: 
        print("Error en SELECT:", e)
        
        return redirect(url_for('pacientes')) 

    if request.method == 'POST': 
        pac_id = request.form["pac_id"]
        pac_nombres = request.form["pac_nombres"] 
        pac_apellidos = request.form["pac_apellidos"] 
        pac_fechanacimiento = request.form["pac_fechanacimiento"]
        pac_sexo = request.form["pac_sexo"] 

        try: 
            conn = connect_to_db() 
            cur = conn.cursor() 
            
            cur.execute("""UPDATE pacientes 
                           SET pac_id=%s, pac_nombres=%s, pac_apellidos=%s, pac_fechanacimiento=%s, pac_sexo=%s 
                           WHERE pac_id=%s""",  
                        (pac_id, pac_nombres, pac_apellidos, pac_fechanacimiento, pac_sexo, id)) 
            conn.commit() 
            cur.close() 
            conn.close() 
            
            
            return redirect(url_for('conpacientes')) 
        except Exception as e: 
           
            return redirect(url_for('conpacientes')) 

    return render_template('editar.html', pacientes=pacientes)


# Borrar Pacientes


@app.route('/delete/<int:pac_id>', methods=['POST']) 

def delete_pacientes(pac_id): 

    try: 

        conn = connect_to_db() 

        cur = conn.cursor() 

        cur.execute("DELETE FROM pacientes WHERE pac_id=%s", (pac_id,)) 

        conn.commit() 

        cur.close() 

        conn.close() 

        return redirect(url_for('conpacientes')) 

    except Exception as e: 

        return redirect(url_for('conpacientes')) 





@app.route('/conmedicos') 

def conmedicos(): 

    try: 

        conn = connect_to_db() 

        cur = conn.cursor() 

        cur.execute("SELECT * FROM medicos") 

        data = cur.fetchall() 

        cur.close() 

        conn.close() 

        return render_template('conmedicos.html', medicos=data) 

    except Exception as e: 

        return render_template('index.html', medicos=[])



 
 
 
@app.route ('/citas')
def citas(): 
    if request.method=="POST": 
    
    
            fecha_citas=request.form["fecha_citas"] 
    
            hora_citas=request.form["hora_citas"] 
            
            estado_cita=request.form["estado_cita"]
    
            try: 
    
                conn = connect_to_db() 
    
                cur = conn.cursor()  
    
                cur.execute("INSERT INTO pacientes ( pac_nombres, pac_apellidos, pac_fechanacimiento, pac_sexo ) VALUES (%s, %s, %s, %s)", 
    
                            ( fecha_citas, hora_citas, estado_cita)) 
    
                conn.commit() 
    
                cur.close() 
    
                conn.close() 
    
                return redirect(url_for('citas')) 
    
            except Exception: 
    
                return redirect(url_for('citas')) 
    
    return render_template("citas.html")


@app.route ('/medicos', methods=["GET","POST"])
def medicos():
    if request.method=="POST": 
    
            idMed=request.form["idMed"] 
    
            nombresMed=request.form["nombresMed"] 
    
            apellidosMed=request.form["apellidosMed"] 
            

    
            try: 
    
                conn = connect_to_db() 
    
                cur = conn.cursor()  
    
                cur.execute("INSERT INTO medicos (idMed , nombresMed, apellidosMed ) VALUES (%s, %s, %s )", 
    
                            (idMed, nombresMed, apellidosMed )) 
    
                conn.commit() 
    
                cur.close() 
    
                conn.close() 
    
                return redirect(url_for('medicos')) 
    
            except Exception: 
    
                return redirect(url_for('medicos'))
    return render_template("medicos.html")



@app.route ('/crearcuenta')
def crearcuenta():
    return render_template("crearcuenta.html")


@app.route ('/tratamientos')
def tratamientos():
    
    if request.method=="POST": 
        
                id_tra=request.form["id_tra"] 
        
                fecha_tra=request.form["fecha_tra"] 
        
                descripcion_tra=request.form["descripcion_tra"]
                
                fechaIn_tra=request.form["fechaIn_tra"]
                
                fechaFin_tra=request.form["fechaFin_tra"]
                
                obsevaciones_tra=request.form["obsevaciones_tra"]
                
    
        
                try: 
        
                    conn = connect_to_db() 
        
                    cur = conn.cursor()  
        
                    cur.execute("INSERT INTO tratamientos (id_tra , fecha_tra, descripcion_tra, fechaIn_tra, fechaFin_tra, obsevaciones_tra  ) VALUES (%s, %s, %s, %s, %s, %s )", 
        
                                (id_tra, fecha_tra, descripcion_tra, fechaIn_tra, fechaFin_tra, obsevaciones_tra )) 
        
                    conn.commit() 
        
                    cur.close() 
        
                    conn.close() 
        
                    return redirect(url_for('tratamientos')) 
        
                except Exception: 
        
                    return redirect(url_for('tratamientos'))
    
    return render_template("tratamientos.html") 

 # consulta pacientes
 
@app.route('/api/conpacientes', methods=['GET']) 

def apiconpacientes(): 

    try: 

        conn = connect_to_db() 

        cur = conn.cursor() 

        cur.execute("SELECT * FROM pacientes") 

        data = cur.fetchall() 

        cur.close() 

        conn.close() 
        
        return jsonify(data)

    except Exception as e: 

        return jsonify({'error':str(e)}),500 
    


@app.route('/api/conmedicos', methods=['GET']) 

def apiconmedicos(): 

    try: 

        conn = connect_to_db() 

        cur = conn.cursor() 

        cur.execute("SELECT * FROM medicos") 

        data = cur.fetchall() 

        cur.close() 

        conn.close() 

        return jsonify(data) 

    except Exception as e: 

        return jsonify({'error':str(e)}),500









if __name__ == '__main__':
    
   
    app.run(debug=True)
