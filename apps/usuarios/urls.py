from django.urls import path
from . import views

urlpatterns = [
    # 🧑 Listar usuarios
    path('', views.lista_usuarios, name='lista_usuarios'),

    # 👤 Ver detalle de un usuario
    path('<int:id>/', views.detalle_usuario, name='detalle_usuario'),

    # 🆕 Registrar usuario
    path('registro/', views.registro_usuario, name='registro_usuario'),

    # 🔐 Login usuario
    path('login/', views.login_usuario, name='login_usuario'),

    # 🚪 Logout usuario (opcional)
    path('logout/', views.logout_usuario, name='logout_usuario'),
]