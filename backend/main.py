from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from tinyfish_integration import fetch_tinyfish_context

app = FastAPI(title="SignBridge Backend", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to SignBridge API - Kritical Hacks 2026"}

@app.get("/context")
def get_context(query: str):
    """Endpoint leveraging TinyFish API for live call context cards."""
    result = fetch_tinyfish_context(query)
    return result

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            response_text = f"Translated sign: [Echo] {data}"
            await websocket.send_text(response_text)
    except WebSocketDisconnect:
        print("Client disconnected")