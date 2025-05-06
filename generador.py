import os
import pandas as pd
import json
import hashlib
import qrcode
from datetime import datetime

def generar_invitados(excel_path="invitados.xlsx", output_json="invitados_generados.json", qr_dir="qr_codes", base_url="https://juliaandcarlos.onrender.com"):
    os.makedirs(qr_dir, exist_ok=True)
    df = pd.read_excel(excel_path)
    invitados = []

    for nombre in df["Nombre"]:
        codigo = hashlib.sha256((nombre + str(datetime.now())).encode()).hexdigest()[:8]
        url = f"{base_url}/invitacion/{codigo}"

        # Generar QR
        qr_img = qrcode.make(url)
        qr_path = os.path.join(qr_dir, f"{codigo}.png")
        qr_img.save(qr_path)

        invitados.append({"nombre": nombre, "codigo": codigo})

    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(invitados, f, indent=2, ensure_ascii=False)

    return invitados

if __name__ == "__main__":
    invitados = generar_invitados()
    print(f"Se generaron {len(invitados)} códigos QR en la carpeta 'qr_codes'")