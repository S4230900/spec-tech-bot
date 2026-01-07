from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .core.config import settings
from .api import users, orders

app = FastAPI(title="SpecTech Bot API")

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем роутеры
app.include_router(users.router, prefix="/api/users", tags=["users"])
app.include_router(orders.router, prefix="/api/orders", tags=["orders"])

@app.get("/")
def read_root():
    return {"message": "SpecTech Bot API работает!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
