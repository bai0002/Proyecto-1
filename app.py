from flask import Flask, render_template_string
import webbrowser

app = Flask(__name__)

# Aquí puedes poner cualquier URL de YouTube que quieras redirigir
YOUTUBE_URL = "https://www.youtube.com/watch?v=hPr-Yc92qaY"  # Un enlace de YouTube de ejemplo

@app.route('/')
def index():
    html = '''
    <html>
        <head>
            <title>Boton Inutil</title>
        </head>
        <body>
            <h1>Pulsalo</h1>
            <p>¿A que esperas?</p>
            <a href="{{ youtube_url }}" target="_blank">
                <button>Boton</button>
            </a>
        </body>
    </html>
    '''
    return render_template_string(html, youtube_url=YOUTUBE_URL)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

