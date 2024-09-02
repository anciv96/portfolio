from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqladmin import Admin

from admin.feedback_admin import FeedbackAdmin
from admin.order_admin import OrderAdmin
from admin.project_admin import ProjectAdmin
from admin.user_admin import UserAdmin
from depends import create_user_repository
from models.database import engine, Base
from routing import feedbacks, projects, order
from config import JWT_KEY, ORIGINS
from services.user_services import AdminAuth


def init_cors(app):

    app.add_middleware(
        CORSMiddleware,
        allow_origins=ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def create_app() -> FastAPI:
    app = FastAPI(title='Portfolio')
    init_cors(app)

    app.include_router(feedbacks.router)
    app.include_router(projects.router)
    app.include_router(order.router)
    return app


async def init_admin(app):

    user_repository = await create_user_repository()
    authentication_backend = AdminAuth(secret_key=JWT_KEY, user_repository=user_repository)
    admin = Admin(app=app, engine=engine, authentication_backend=authentication_backend)

    admin.add_view(FeedbackAdmin)
    admin.add_view(UserAdmin)
    admin.add_view(ProjectAdmin)
    admin.add_view(OrderAdmin)

    return admin


async def init_db() -> None:
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)


app = create_app()


@app.on_event('startup')
async def startup():
    await init_admin(app)
    await init_db()
