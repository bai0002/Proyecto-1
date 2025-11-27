from flask import Flask, render_template_string, request, redirect, session, url_for
import os

app = Flask(__name__)
app.secret_key = "cambia_esto"  # seguimos sin FLASK_SECRET_KEY

# --------------------------
# Datos de login y "secreto"
# --------------------------
USERNAME = os.environ.get("SECRET1", "admin")  # usuario desde secret
PASSWORD = "admin"                             # contraseña fija
SECRET_MESSAGE = os.environ.get("SECRET2", "este es tu secreto")  # secreto que se mostrará

# ====================================================
# LOGIN
# ====================================================
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form.get("username")
        pwd = request.form.get("password")

        # validar usuario y contraseña
        if user == USERNAME and pwd == PASSWORD:
            session["logged"] = True
            return redirect(url_for('index'))

        return "Usuario o contraseña incorrectos"

    html = """
    <html>
        <head><title>Login</title></head>
        <body>
            <h2>Iniciar sesión</h2>
            <form method="POST">
                Usuario: <input type="text" name="username"><br><br>
                Contraseña: <input type="password" name="password"><br><br>
                <button type="submit">Entrar</button>
            </form>
        </body>
    </html>
    """
    return render_template_string(html)

# ====================================================
# LOGOUT
# ====================================================
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# ====================================================
# PÁGINA PRINCIPAL PROTEGIDA
# ====================================================
@app.route('/')
def index():
    if not session.get("logged"):
        return redirect(url_for('login'))

    html = '''
    <html>
        <head>
            <title>Secreto</title>
        </head>
        <body>
            <h1>Botón secreto</h1>
            <p>Pulsa el botón para ver tu secreto:</p>

            <form method="POST" action="{{ secret_url }}">
                <button type="submit">Mostrar secreto</button>
            </form>

            <br><br>
            <a href="{{ logout_url }}">Cerrar sesión</a>
        </body>
    </html>
    '''
    return render_template_string(
        html,
        secret_url=url_for('show_secret'),
        logout_url=url_for('logout')
    )

# ====================================================
# RUTA QUE MUESTRA EL SECRETO
# ====================================================
@app.route('/secret', methods=["POST"])
def show_secret():
    if not session.get("logged"):
        return redirect(url_for('login'))

    html = f"""
    <html>
        <head><title>Tu Secreto</title></head>
        <body>
            <h1>Este es tu secreto:</h1>
            <p>{SECRET_MESSAGE}</p>
            <br><br>
            <a href="{url_for('index')}">Volver</a>
        </body>
    </html>
    """
    return html

# ====================================================
# EJECUCIÓN FLASK
# ====================================================
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
