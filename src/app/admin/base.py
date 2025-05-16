from fastapi import FastAPI
from sqladmin import Admin

from app.admin.auth import AdminAuth
from app.admin.views.suppliers import SupplierAdminView
from app.admin.views.arrivals import ArrivalAdminView
from app.admin.views.products import ProductAdminView
from app.admin.views.categories import CategoryAdminView
from app.admin.views.employees import EmployeeAdminView
from app.admin.views.customers import CustomerAdminView
from app.admin.views.orders import OrderAdminView
from app.admin.views.warehouses import WarehouseAdminView
from app.connectors.pg_database import SQLAlchemyDatabaseConnector
from app.settings import Settings


def setup_admin(app: FastAPI, settings: Settings):
    database_dep = SQLAlchemyDatabaseConnector(settings)
    master_session_maker = database_dep.get_master_session_maker()
    authentication_backend = AdminAuth(secret_key=settings.admin_config.ADMIN_SECRET)
    admin = Admin(
        app,
        base_url="/",
        session_maker=master_session_maker,
        authentication_backend=authentication_backend,
        debug=settings.DEBUG,
    )

    views = [
        CategoryAdminView,
        WarehouseAdminView,
        SupplierAdminView,
        ArrivalAdminView,
        ProductAdminView,
        EmployeeAdminView,
        CustomerAdminView,
        OrderAdminView,
    ]

    for view in views:
        admin.add_view(view)
