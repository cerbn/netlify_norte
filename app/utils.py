import os
from supabase import create_client
from django.conf import settings

# Inicializar el cliente de Supabase
supabase = create_client(settings.SUPABASE_URL, settings.SECRET_KEY)

def upload_image_to_supabase(file, path):
    # Leer el contenido del archivo en memoria
    file_content = file.read()

    # Acceder al bucket de almacenamiento correctamente
    response = supabase.storage.from_('libros').upload(
        path,
        file_content,
        file_options={'content-type': file.content_type}  # Especificar el tipo de contenido
    )

    # Verificar si la subida fue exitosa
    if response.status_code == 200:
        # Construir la URL de acceso público
        return f"{settings.SUPABASE_URL}/storage/v1/object/public/libros/{path}"
    else:
        raise Exception(f"Error al subir la imagen: {response.json()}")
    

