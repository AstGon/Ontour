from django.http import JsonResponse
from django.shortcuts import render
from .models import Contrato


def cargaArchivos(request):
    numero_contrato = request.POST.get("contrato", "")
    contrato_encontrado = None
    contrato_encontrado_valido = (
        False  # Variable para indicar si se ha encontrado un contrato válido
    )

    if numero_contrato:
        try:
            contrato_encontrado = Contrato.objects.get(id_contrato=numero_contrato)
            contrato_encontrado_valido = True
        except Contrato.DoesNotExist:
            contrato_encontrado = None

    context = {
        "numero_contrato": numero_contrato,
        "contrato_encontrado": contrato_encontrado,
        "contrato_encontrado_valido": contrato_encontrado_valido,  # Variable para indicar si se ha encontrado un contrato válido
    }

    return render(request, "modulos/cargaArchivos.html", context)
