from django.urls import path
from . import views
from .views import login_view, logout_view, registrar_direccion # Asegúrate de importar la vista
from django.contrib.auth.views import LoginView



urlpatterns = [
    path('', views.home, name='home'),

    path('login/', LoginView.as_view(template_name='app/login.html'), name='login'),

    path('registro', views.registro, name='registro'),

    path('base', views.base, name='base'),

    path('profile', views.profile_view, name='profile'),

    path('carrito', views.carrito, name='carrito'),

    path('Registrar_libro_usuario', views.Registrar_libro_usuario, name='Registrar_libro_usuario'),

    path('Registrar_libro_Intercambio', views.Registrar_libro_Intercambio, name='Registrar_libro_Intercambio'),

    path('administrador', views.administrador, name='administrador'),

    path('reportes', views.reportes, name='reportes'),

    path('seguimiento', views.seguimiento, name='seguimiento'),

    path('orden_compra', views.orden_compra, name='orden_compra'),

    path('confirmacion_pago', views.confirmacion_pago, name='confirmacion_pago'),

    path('libro_detalle', views.libro_detalle, name='libro_detalle'),
    
    path('recuperar_contraseña', views.recuperar_contraseña, name='recuperar_contraseña'),

    path('confirmacion_direccion', views.confirmacion_direccion, name='confirmacion_direccion'),

    path('iniciar_pago', views.iniciar_pago, name='iniciar_pago'),
    
    path('api/comunas/<int:region_id>/', views.obtener_comunas, name='obtener_comunas'),

    path('logout/', logout_view, name='logout'),  # Añadir la URL para logout

    path('registrar_direccion/', views.registrar_direccion, name='registrar_direccion'),

    path('registrar_direccion2/', views.registrar_direccion2, name='registrar_direccion2'),

    path('actualizar_user/', views.actualizar_user, name='actualizar_user'),

    path('actualizar_direccion/', views.actualizar_direccion, name='actualizar_direccion'),
    
    path('actualizar_direccion2/', views.actualizar_direccion2, name='actualizar_direccion2'),

    path('eliminar_del_carrito/<int:item_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),

    path('libro_detalle/<str:libro_id>/', views.libro_detalle, name='libro_detalle'),

    path('agregar_al_carrito/<str:libro_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),

    path('obtener_estado_seguimiento', views.obtener_estado_seguimiento, name="obtener_estado_seguimiento"),

    path('verificar-datos/', views.verificar_datos_adicionales, name='verificar_datos'),
    
    path('actualizar_perfil/', views.actualizar_perfil, name='actualizar_perfil'),

    path('confirmar_pago/', views.confirmar_pago, name='confirmar_pago'),

    path('actualizar_cantidad/', views.actualizar_cantidad, name='actualizar_cantidad'),

    path('pedidos/', views.pedidos, name='pedidos'),

    path('mesa_ayuda/', views.mesa_ayuda_usuario, name='mesa_ayuda_usuario'),

    path('mesa_ayuda_trabajador/', views.mesa_ayuda_trabajador, name='mesa_ayuda_trabajador'),
    
    path('crear_ticket/', views.crear_ticket, name='crear_ticket'),

    path('perfil/<int:user_id>/', views.biografia_usuario, name='perfil_usuario'),

    path('autor_detalle/<int:user_id>/', views.autor_detalle, name='autor_detalle'),
    
    path('categoria/<int:categoria_id>/', views.libros_por_categoria, name='libros_por_categoria'),

    path('libro/editar/<int:libro_id>/', views.actualizar_libro_con_imagen, name='editar_libro'),

    path('solicitar_intercambio/', views.solicitar_intercambio, name='solicitar_intercambio'),

    path('autor/<int:autor_id>/', views.autor_detalle, name='autor_detalle'),

    path('buscar-libro-open/', views.buscar_libro_open_library, name='buscar_libro_open_library'),

    path('eliminar_libro/<int:libro_id>/', views.eliminar_libro_usuario, name='eliminar_libro_usuario'),

    path('procesar-solicitud/<int:solicitud_id>/', views.procesar_solicitud, name='procesar_solicitud'),
    path('confirmar-intercambio/<int:solicitud_id>/', views.confirmar_intercambio, name='confirmar_intercambio'),
    path('confirmar-devolucion/<int:solicitud_id>/', views.confirmar_devolucion, name='confirmar_devolucion'),
    path('calificar-intercambio/<int:solicitud_id>/', views.calificar_intercambio, name='calificar_intercambio'),
    path('procesar-solicitud/<int:solicitud_id>/', views.procesar_solicitud, name='procesar_solicitud'),
    path('dashboard/', views.dashboard, name='dashboard'),



    path('trabajador/', views.trabajador, name='trabajador'),




    # otras URL
]

