from flask import Flask, render_template, abort
from generador import generar_invitados
import json, os

app = Flask(__name__)

if not os.path.exists("invitados_generados.json"):
    generar_invitados(base_url="https://juliaandcarlos.onrender.com")

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

if __name__ == "__main__":
    app.run()
