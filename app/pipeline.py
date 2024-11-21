from django.shortcuts import redirect

def verificar_datos_adicionales(backend, user, response, *args, **kwargs):
    if not user.birth_date or not user.gender or not user.phone_number:
        return redirect('completar_datos')
