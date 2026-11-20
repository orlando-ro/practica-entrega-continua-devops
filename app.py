from flask import Flask

app = Flask(__name__)


@app.route("/")
def hola_mundo():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hola Mundo - DevOps</title>
        <style>
            body {
                font-family: system-ui, -apple-system, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background: #0f172a;
                color: #f8fafc;
            }
            .card {
                text-align: center;
                padding: 2.5rem 3.5rem;
                background: #1e293b;
                border-radius: 1rem;
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
            }
            h1 { color: #38bdf8; margin-bottom: 0.5rem; }
            p { color: #94a3b8; margin: 0; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>¡Hola Mundo!</h1>
            <p>Aplicación web en Python + Flask corriendo en Docker</p>
        </div>
    </body>
    </html>
    """


@app.route("/health")
def health():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
