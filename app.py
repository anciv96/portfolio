from fastapi import FastAPI
from sqladmin import Admin

from admin.feedback_admin import FeedbackAdmin
from admin.order_admin import OrderAdmin
from admin.project_admin import ProjectAdmin
from admin.user_admin import UserAdmin
from depends import create_user_repository
from models.database import engine, Base
from routing import feedbacks, projects, order
from config import JWT_KEY
from services.user_services import AdminAuth


app = FastAPI(title='Portfolio')
app.include_router(feedbacks.router)
app.include_router(projects.router)
app.include_router(order.router)


async def init_admin():
    user_repository = await create_user_repository()
    authentication_backend = AdminAuth(secret_key=JWT_KEY, user_repository=user_repository)
    admin = Admin(app=app, engine=engine, authentication_backend=authentication_backend)

    admin.add_view(FeedbackAdmin)
    admin.add_view(UserAdmin)
    admin.add_view(ProjectAdmin)
    admin.add_view(OrderAdmin)

    return admin


@app.on_event('startup')
async def startup():
    await init_admin()

    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
