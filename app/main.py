import uvicorn
from fastapi import FastAPI

from urls import router
from crud import add_forms


app = FastAPI()
app.include_router(router)

@app.on_event("startup")
async def startup_event():
    await add_forms()

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8000)