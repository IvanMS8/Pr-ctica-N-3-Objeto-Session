from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Clave secreta para usar sesiones

@app.route('/')
def index():
    return render_template('base.html')

# Inicializar la lista de inscritos en cada petición si no existe
def init_session():
    if 'inscritos' not in session:
        session['inscritos'] = []

# Ruta para el formulario de registro de seminarios
@app.route('/registro_seminario', methods=['GET', 'POST'])
def registro_seminario():
    init_session()  # Inicializar la sesión si es necesario

    if request.method == 'POST':
        # Obtener los datos del formulario
        fecha = request.form['fecha']
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        turno = request.form['turno']
        seminarios = request.form.getlist('seminarios')

        # Crear un diccionario para los datos
        inscrito = {
            'fecha': fecha,
            'nombre': nombre,
            'apellidos': apellidos,
            'turno': turno,
            'seminarios': ', '.join(seminarios)
        }

        # Guardar los datos en la sesión
        session['inscritos'].append(inscrito)
        session.modified = True

        return redirect(url_for('listado_inscritos'))

    return render_template('registro_seminario.html')

# Ruta para mostrar el listado de inscritos
@app.route('/listado_inscritos')
def listado_inscritos():
    init_session()  # Inicializar la sesión si es necesario

    return render_template('listado_inscritos.html', inscritos=session['inscritos'])

if __name__ == '__main__':
    app.run(debug=True)
