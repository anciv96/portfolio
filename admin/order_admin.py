from sqladmin import ModelView

from models.order_model import Order


class OrderAdmin(ModelView, model=Order):
    column_list = [Order.id, Order.project_type, Order.budget, Order.customer_name]
