import os
from django.http import JsonResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import Contrato, TipoServicio, Archivo


def cargaArchivos(request):
    numero_contrato = request.POST.get("contrato", "")
    contrato_encontrado = None
    contrato_encontrado_valido = False
    contrato_mensaje = None
    mensaje_error = None
    archivo_carga = None

    tipo_servicios = TipoServicio.objects.all()

    if request.method == "POST" and numero_contrato:
        try:
            contrato_encontrado = Contrato.objects.get(id_contrato=numero_contrato)
            contrato_encontrado_valido = True
            contrato_mensaje = "El contrato existe."
        except Contrato.DoesNotExist:
            contrato_encontrado = None
            contrato_mensaje = "El contrato no existe."

    if request.method == "POST" and request.FILES.get("archivo"):
        archivo = request.FILES["archivo"]
        extension = archivo.name.split(".")[-1].lower()
        if extension in ["pdf", "jpg", "png"]:
            carpeta_archivos = "C:/Users/ASTRID/OneDrive/Desktop/archivos"
            archivo_carga = True

            if not os.path.exists(carpeta_archivos):
                os.makedirs(carpeta_archivos)

            ruta_archivo = os.path.join(carpeta_archivos, archivo.name)
            with open(ruta_archivo, "wb") as f:
                for chunk in archivo.chunks():
                    f.write(chunk)

            tipo_servicio_id = request.POST.get("tipo_documento", "")

            tipo_servicio = None
            if tipo_servicio_id.isdigit():
                tipo_servicio_id = int(tipo_servicio_id)
                try:
                    tipo_servicio = TipoServicio.objects.get(
                        id_tipo_servicio=tipo_servicio_id
                    )
                except ObjectDoesNotExist:
                    tipo_servicio = None

            nuevo_archivo = Archivo(
                descripcion=archivo.name,
                ruta=ruta_archivo,
                contrato=contrato_encontrado,
                tipo_servicio=tipo_servicio,
            )

            nuevo_archivo.save()

        else:
            archivo_carga = False

    context = {
        "numero_contrato": numero_contrato,
        "contrato_encontrado": contrato_encontrado,
        "contrato_encontrado_valido": contrato_encontrado_valido,
        "contrato_mensaje": contrato_mensaje,
        "tipo_servicios": tipo_servicios,
        "mensaje_error": mensaje_error,
        "archivo_carga": archivo_carga,
    }

    return render(request, "modulos/cargaArchivos.html", context)


from django.shortcuts import render, get_object_or_404
from .models import Contrato, Servicio


def detalles(request):
    if request.method == "POST":
        numero_contrato = request.POST.get("contrato")
        contrato = get_object_or_404(Contrato, id_contrato=numero_contrato)

        servicio_hotel = Servicio.objects.filter(
            contrato=contrato, tipo_servicio__nombre="Hotel"
        ).first()
        servicio_transporte = Servicio.objects.filter(
            contrato=contrato, tipo_servicio__nombre="Transporte"
        ).first()
        servicio_alimentacion = Servicio.objects.filter(
            contrato=contrato, tipo_servicio__nombre="Alimentación"
        ).first()
        servicio_entretencion = Servicio.objects.filter(
            contrato=contrato, tipo_servicio__nombre="Entretención"
        ).first()

        context = {
            "contrato": contrato,
            "servicio_hotel": servicio_hotel,
            "servicio_transporte": servicio_transporte,
            "servicio_alimentacion": servicio_alimentacion,
            "servicio_entretencion": servicio_entretencion,
            "contrato_encontrado_valido": True,
            "numero_contrato": numero_contrato,
        }
    else:
        context = {"contrato_encontrado_valido": False}
    return render(request, "detalles.html", context)
