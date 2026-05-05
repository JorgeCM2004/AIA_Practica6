from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from utils import Hybrid_Searcher
from utils.agent import Maternal_Agent, Medical_Agent

app = FastAPI(title="Maternal Health AI Server", version="1.0")
searcher = Hybrid_Searcher()
paciente_agent = Maternal_Agent(searcher=searcher)
medico_agent = Medical_Agent()


class PacienteRequest(BaseModel):
	query: str
	session_id: str


class MedicoRequest(BaseModel):
	query: str


@app.post("/api/paciente/chat")
async def chat_paciente(request: PacienteRequest):
	try:
		print(f"\n🚀 [BACKEND] Petición recibida del frontend: {request.query}")
		respuesta = paciente_agent.run(request.query)
		print("✅ [BACKEND] Respuesta de Groq generada con éxito")
		return {"respuesta": respuesta}
	except Exception as e:
		raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/medico/chat")
async def chat_medico(request: MedicoRequest):
	try:
		respuesta = medico_agent.run(request.query)
		return {"respuesta": respuesta}
	except Exception as e:
		print(e)
		raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
	import uvicorn

	uvicorn.run(app, host="0.0.0.0", port=8000)
