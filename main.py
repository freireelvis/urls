from fastapi import FastAPI
import uvicorn

app = FastAPI(title="API de URLs")

@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Lista de URLs disponíveis"
    }

@app.get("/urls")
def listar_urls():
    return {
        "urls": [
            "https://www.google.com",
            "https://www.github.com",
            "https://www.youtube.com",
            "https://fastapi.tiangolo.com",
            "https://www.python.org"
        ]
    }
if __name__ == "__main__":
  uvicorn.run("main:app", host="0.0.0.0", port=5000)
