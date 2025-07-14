# 🧑‍⚖️ AgentCourt_ES – Simulador de Juicio Oral Penal 🇲🇽

[![Abrir en Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/nicohaddad/AgentCourt_ES/HEAD?filepath=AgentCourt_ES_Binder_OK.ipynb)

Este proyecto simula una audiencia penal con IA en español, usando agentes tipo juez, fiscal y defensa basados en GPT.

---

## 📁 Estructura del Proyecto

```
AgentCourt_ES/
├── configs/                       # Prompts del juez, fiscal y defensa
├── cases/                         # Casos reales simulados
├── AgentCourt_ES_Binder_OK.ipynb # Notebook funcional para Binder (versión web)
├── requirements.txt              # Dependencias para Binder
```

---

## 🟢 Ejecutar en la Web (Binder)

1. Haz clic en el botón "Abrir en Binder"
2. Espera 1–2 minutos mientras se carga el entorno
3. Ejecuta las celdas paso a paso (Shift+Enter)
4. Observa cómo se desarrolla un juicio oral automático

> ⚠️ Esta versión contiene una API key preinsertada para pruebas. Usa solo con fines demostrativos.

---

## 🟡 Ejecutar Localmente (opcional)

1. Crea un archivo `.env` con tu API Key de OpenAI:
```
OPENAI_API_KEY=sk-xxxxx
```

2. Ejecuta localmente con `AgentCourt_ES_simulador_ENV.ipynb`

3. Instala dependencias:
```bash
pip install openai python-dotenv
```

---

## 📚 Créditos

- Basado en [AgentCourt (relic-yuexi)](https://github.com/relic-yuexi/AgentCourt)
- Adaptado en español y estructurado por [nicohaddad]

---

⚖️ Este simulador tiene fines educativos y de exploración legal con IA.
