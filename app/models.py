# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    birth_date = models.DateField(blank=True, null=True)
    phone_number = models.CharField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Autor(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'autor'


class Carrito(models.Model):
    id = models.IntegerField(primary_key=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    metodo_pago = models.CharField(max_length=50, blank=True, null=True)
    referencia_pago = models.CharField(max_length=100, blank=True, null=True)
    direccion_envio = models.CharField(max_length=255, blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carrito'


class Carritoitem(models.Model):
    id = models.IntegerField(primary_key=True)
    carrito = models.ForeignKey(Carrito, models.DO_NOTHING, blank=True, null=True)
    libro = models.ForeignKey('Libro', models.DO_NOTHING, blank=True, null=True)
    cantidad = models.FloatField(blank=True, null=True)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    descuento = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    imagen = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carritoitem'


class Categoria(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categoria'


class ChatRoom(models.Model):
    nombre = models.CharField(unique=True, max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chat_room'


class ChatRoomParticipants(models.Model):
    chat_room = models.ForeignKey(ChatRoom, models.DO_NOTHING)
    auth_user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'chat_room_participants'
        unique_together = (('chat_room', 'auth_user'),)


class Comentarios(models.Model):
    id = models.IntegerField(primary_key=True)
    libro = models.ForeignKey('Libro', models.DO_NOTHING, blank=True, null=True)
    usuario = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    calificacion = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comentarios'


class Comuna(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    region = models.ForeignKey('Region', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comuna'


class Direccion(models.Model):
    usuario = models.AutoField(primary_key=True)
    region = models.ForeignKey('Region', models.DO_NOTHING, db_column='region', blank=True, null=True)
    comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='comuna', blank=True, null=True)
    destinatario = models.CharField(max_length=100, blank=True, null=True)
    calle = models.CharField(max_length=100, blank=True, null=True)
    numero = models.CharField(max_length=10, blank=True, null=True)
    datos_adicionales = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direccion'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class LIntercambio(models.Model):
    id = models.IntegerField(primary_key=True)
    isbn = models.FloatField(blank=True, null=True)
    titulo = models.CharField(max_length=255, blank=True, null=True)
    autor = models.ForeignKey(Autor, models.DO_NOTHING, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stock = models.FloatField(blank=True, null=True)
    estado = models.CharField(max_length=25, blank=True, null=True)
    descripcion = models.CharField(max_length=4000, blank=True, null=True)
    usuario = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    solicitud = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'l_intercambio'


class LVentaU(models.Model):
    id = models.IntegerField(primary_key=True)
    isbn = models.FloatField(blank=True, null=True)
    titulo = models.CharField(max_length=255, blank=True, null=True)
    autor = models.ForeignKey(Autor, models.DO_NOTHING, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stock = models.FloatField(blank=True, null=True)
    estado = models.CharField(max_length=25, blank=True, null=True)
    descripcion = models.CharField(max_length=4000, blank=True, null=True)
    solicitud = models.CharField(max_length=50, blank=True, null=True)
    usuario = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    tipo_registro = models.CharField(blank=True, null=True)
    imagen_url = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'l_venta_u'


class Libro(models.Model):
    id = models.IntegerField(primary_key=True)
    isbn = models.FloatField(blank=True, null=True)
    titulo = models.CharField(max_length=255, blank=True, null=True)
    autor = models.ForeignKey(Autor, models.DO_NOTHING, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.IntegerField(blank=True, null=True)
    stock = models.FloatField(blank=True, null=True)
    formato = models.CharField(max_length=50, blank=True, null=True)
    idioma = models.CharField(max_length=50, blank=True, null=True)
    anio = models.IntegerField(blank=True, null=True)
    num_paginas = models.FloatField(blank=True, null=True)
    encuadernacion = models.CharField(max_length=50, blank=True, null=True)
    dimensiones = models.CharField(max_length=50, blank=True, null=True)
    imagen_url = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'libro'


class Message(models.Model):
    chat_room = models.ForeignKey(ChatRoom, models.DO_NOTHING)
    sender = models.ForeignKey(AuthUser, models.DO_NOTHING)
    content = models.TextField()
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message'


class Pedido(models.Model):
    id = models.IntegerField(primary_key=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    completado = models.CharField(max_length=1, blank=True, null=True)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    usuario = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    n_orden_despacho = models.IntegerField()
    direccion_envio = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedido'


class Pedidoitem(models.Model):
    id = models.IntegerField(primary_key=True)
    pedido_id = models.IntegerField(blank=True, null=True)
    libro = models.ForeignKey(Libro, models.DO_NOTHING, blank=True, null=True)
    cantidad = models.FloatField(blank=True, null=True)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    direccion_envio = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedidoitem'


class Problema(models.Model):
    id = models.IntegerField(primary_key=True)
    usuario = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'problema'


class Region(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'region'


class Respuesta(models.Model):
    id = models.IntegerField(primary_key=True)
    problema = models.ForeignKey(Problema, models.DO_NOTHING, blank=True, null=True)
    respuesta = models.TextField(blank=True, null=True)
    fecha_respuesta = models.DateTimeField(blank=True, null=True)
    respondido_por = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'respuesta'


class SocialAuthAssociation(models.Model):
    id = models.BigAutoField(primary_key=True)
    server_url = models.CharField(max_length=255)
    handle = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)
    issued = models.IntegerField()
    lifetime = models.IntegerField()
    assoc_type = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'social_auth_association'
        unique_together = (('server_url', 'handle'),)


class SocialAuthCode(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(max_length=254)
    code = models.CharField(max_length=32)
    verified = models.BooleanField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'social_auth_code'
        unique_together = (('email', 'code'),)


class SocialAuthNonce(models.Model):
    id = models.BigAutoField(primary_key=True)
    server_url = models.CharField(max_length=255)
    timestamp = models.IntegerField()
    salt = models.CharField(max_length=65)

    class Meta:
        managed = False
        db_table = 'social_auth_nonce'
        unique_together = (('server_url', 'timestamp', 'salt'),)


class SocialAuthPartial(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.CharField(max_length=32)
    next_step = models.SmallIntegerField()
    backend = models.CharField(max_length=32)
    timestamp = models.DateTimeField()
    data = models.JSONField()

    class Meta:
        managed = False
        db_table = 'social_auth_partial'


class SocialAuthUsersocialauth(models.Model):
    id = models.BigAutoField(primary_key=True)
    provider = models.CharField(max_length=32)
    uid = models.CharField(max_length=255)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    extra_data = models.JSONField()

    class Meta:
        managed = False
        db_table = 'social_auth_usersocialauth'
        unique_together = (('provider', 'uid'),)


class Solicitudintercambio(models.Model):
    solicitante = models.ForeignKey(AuthUser, models.DO_NOTHING)
    destinatario = models.ForeignKey(AuthUser, models.DO_NOTHING, related_name='solicitudintercambio_destinatario_set')
    libro = models.ForeignKey(LVentaU, models.DO_NOTHING)
    estado = models.TextField(blank=True, null=True)
    libro_intercambio = models.ForeignKey(LVentaU, models.DO_NOTHING, related_name='solicitudintercambio_libro_intercambio_set', blank=True, null=True)
    mensaje = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_limite = models.DateTimeField(blank=True, null=True)
    calificacion_solicitante = models.SmallIntegerField(blank=True, null=True)
    calificacion_propietario = models.SmallIntegerField(blank=True, null=True)
    confirmado_solicitante = models.BooleanField(blank=True, null=True)
    confirmado_destinatario = models.BooleanField(blank=True, null=True)
    devolucion_confirmada_solicitante = models.BooleanField(blank=True, null=True)
    devolucion_confirmada_destinatario = models.BooleanField(blank=True, null=True)
    libro_destinatario = models.ForeignKey(LVentaU, models.DO_NOTHING, related_name='solicitudintercambio_libro_destinatario_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'solicitudintercambio'


class Usuarios(models.Model):
    id = models.IntegerField(primary_key=True)
    birth_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    auth_user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios'
