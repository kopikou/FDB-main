from fastapi import FastAPI
from sqladmin import Admin

from app.database import async_db

from app.views import UserView, FileTypeView, StorageFileView, GroupView

app = FastAPI()
admin = Admin(app, async_db.engine)


for model in [UserView, FileTypeView, StorageFileView, GroupView]:
    admin.add_view(model)

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # В production укажите конкретные домены
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
