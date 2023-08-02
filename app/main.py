from fastapi import FastAPI
from api.menu.routes import router as menu_router

app = FastAPI()

app.include_router(menu_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0", port=8000)
