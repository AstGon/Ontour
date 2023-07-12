import os
import shutil
from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from .models import Contrato, TipoServicio, Archivo


def cargaArchivos(request):
    numero_contrato = request.POST.get("contrato", "").upper()
    contrato_encontrado = None
    contrato_encontrado_valido = False
    contrato_mensaje = None
    mensaje_error = None
    archivo_carga = None

    tipo_servicios = TipoServicio.objects.all()

    if numero_contrato:
        try:
            contrato_encontrado = Contrato.objects.get(id_contrato=numero_contrato)
            contrato_encontrado_valido = True
            contrato_mensaje = "El contrato existe."
        except Contrato.DoesNotExist:
            contrato_encontrado = None
            contrato_mensaje = "El contrato no existe."

    print(contrato_encontrado)

    archivo = request.FILES.get("archivo")
    if request.FILES.get("archivo"):
        extension = archivo.name.split(".")[-1].lower()
        if extension in ["pdf", "jpg", "png"]:
            carpeta_archivos = "C:/Users/ASTRID/OneDrive/Desktop/archivos"
            archivo_carga = True
            if not os.path.exists(carpeta_archivos):
                os.makedirs(carpeta_archivos)

            print("aqui", contrato_encontrado)  # Aquí se utiliza contrato_encontrado

            nombre_archivo = archivo.name
            nombre_base, extension_original = os.path.splitext(nombre_archivo)
            ruta_archivo = os.path.join(carpeta_archivos, nombre_archivo)

            # Verificar si el archivo ya existe
            contador = 1
            while os.path.exists(ruta_archivo):
                nombre_archivo = f"{nombre_base}({contador}){extension_original}"
                ruta_archivo = os.path.join(carpeta_archivos, nombre_archivo)
                contador += 1

            with open(ruta_archivo, "wb") as f:
                for chunk in archivo.chunks():
                    f.write(chunk)

            nombre_tipo_servicio = request.POST.get("tipo_documento_seleccionado", "")
            tipo_servicio = None
            try:
                tipo_servicio = TipoServicio.objects.get(
                    Q(nombre__iexact=nombre_tipo_servicio)
                )
            except TipoServicio.DoesNotExist:
                tipo_servicio = None

            nuevo_archivo = Archivo(
                descripcion=archivo.name,
                ruta=ruta_archivo,
                tipo_servicio=tipo_servicio,
            )

            if contrato_encontrado is not None:
                nuevo_archivo.contrato = contrato_encontrado

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
        numero_contrato = request.POST.get("contrato").upper()
        contrato = None
        contrato_no_disponible = False
        busqueda_realizada = True

        if numero_contrato:
            try:
                contrato = Contrato.objects.get(id_contrato=numero_contrato)
            except Contrato.DoesNotExist:
                contrato_no_disponible = True

        if contrato:
            servicio_hotel = Servicio.objects.filter(
                contrato=contrato, tipo_servicio__nombre="Hotel"
            ).first()
            servicio_transporte = Servicio.objects.filter(
                contrato=contrato, tipo_servicio__nombre="Transporte"
            ).first()
            servicio_alimentacion = Servicio.objects.filter(
                contrato=contrato, tipo_servicio__nombre="Alimentacion"
            ).first()
            servicio_entretencion = Servicio.objects.filter(
                contrato=contrato, tipo_servicio__nombre="Actividades"
            ).first()
            servicio_seguro = Servicio.objects.filter(
                contrato=contrato, tipo_servicio__nombre="Seguro"
            ).first()

            context = {
                "contrato": contrato,
                "servicio_hotel": servicio_hotel,
                "servicio_transporte": servicio_transporte,
                "servicio_alimentacion": servicio_alimentacion,
                "servicio_entretencion": servicio_entretencion,
                "servicio_seguro": servicio_seguro,
                "contrato_encontrado_valido": True,
                "numero_contrato": numero_contrato,
                "contrato_no_disponible": contrato_no_disponible,
                "busqueda_realizada": busqueda_realizada,
            }
        else:
            context = {
                "contrato_encontrado_valido": False,
                "contrato_no_disponible": contrato_no_disponible,
                "busqueda_realizada": busqueda_realizada,
            }

        return render(request, "detalles.html", context)

    return render(request, "detalles.html")
