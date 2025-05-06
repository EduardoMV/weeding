from flask import Flask, render_template, abort
import json, os

app = Flask(__name__)

with open("invitados_generados.json", "r", encoding="utf-8") as f:
    invitados = json.load(f)

mapa = {i["codigo"]: i["nombre"] for i in invitados}

@app.route("/")
def index():
    return "Escanea tu código QR para ver tu invitación personalizada."

@app.route("/invitacion/<codigo>")
def invitacion(codigo):
    nombre = mapa.get(codigo)
    if not nombre:
        abort(404)
    return render_template("invitacion.html", nombre=nombre)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)