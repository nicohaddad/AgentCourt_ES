import json
from pathlib import Path
import openai

openai.api_key = "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"

def cargar_agente(nombre_archivo):
    with open(nombre_archivo, encoding='utf-8') as f:
        data = json.load(f)
    return {
        "nombre": data["name"],
        "sistema": data["system_prompt"],
        "historial": [{"role": "system", "content": data["system_prompt"]}]
    }

def hablar(agente, mensaje):
    agente["historial"].append({"role": "user", "content": mensaje})
    respuesta = openai.ChatCompletion.create(
        model="gpt-4",
        messages=agente["historial"]
    )
    contenido = respuesta.choices[0].message.content
    agente["historial"].append({"role": "assistant", "content": contenido})
    return contenido

# Cargar agentes
ruta_config = Path("configs")
juez = cargar_agente(ruta_config / "juez.json")
fiscal = cargar_agente(ruta_config / "fiscal.json")
defensa = cargar_agente(ruta_config / "defensa.json")

# Cargar caso
with open("cases/caso_001.json", encoding="utf-8") as f:
    caso = json.load(f)

# Simulación
print("🎙️ JUEZ:")
print(hablar(juez, f"Se abre la audiencia. El delito es: {caso['delito']}. Los hechos son: {caso['hechos']}"))
print("\n👨‍⚖️ MINISTERIO PÚBLICO:")
print(hablar(fiscal, caso["argumento_fiscal"]))
print("\n👩‍💼 DEFENSA:")
print(hablar(defensa, caso["argumento_defensa"]))
print("\n🧑‍⚖️ JUEZ - FALLO:")
print(hablar(juez, "Con base en lo expuesto, emite tu fallo."))