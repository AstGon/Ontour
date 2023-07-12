from django.db import models


class TipoArchivo(models.Model):
    id_tipo_archivo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)


class TipoServicio(models.Model):
    id_tipo_servicio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)


class Ejecutivo(models.Model):
    id_ejecutivo = models.AutoField(primary_key=True)
    nombre_eje = models.CharField(max_length=100)
    apellido_eje = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.IntegerField()


class RepresentanteLegal(models.Model):
    rut = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)


class Curso(models.Model):
    nombre_curso = models.CharField(max_length=100)
    cant_alumnos = models.IntegerField()


class Institucion(models.Model):
    nombre_colegio = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)


class Contrato(models.Model):
    id_contrato = models.CharField(max_length=100, primary_key=True)
    fecha_contrato = models.DateField()
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    representante_legal = models.ForeignKey(
        RepresentanteLegal, on_delete=models.CASCADE
    )
    ejecutivo = models.ForeignKey(Ejecutivo, on_delete=models.CASCADE)

    def valor_total(self):
        return self.precio * self.institucion.curso.cant_alumnos

    def add_service(self, servicio):
        self.servicios.add(servicio)

    def remove_service(self, servicio):
        self.servicios.remove(servicio)


class Archivo(models.Model):
    id_archivo = models.AutoField(primary_key=True)
    tipo_servicio = models.ForeignKey(
        TipoServicio, on_delete=models.CASCADE, null=True, blank=True
    )
    descripcion = models.CharField(max_length=100)
    ruta = models.CharField(max_length=100)
    contrato = models.ForeignKey(
        Contrato, on_delete=models.CASCADE, null=True, blank=True
    )


class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    tipo_servicio = models.ForeignKey(
        TipoServicio, on_delete=models.CASCADE, null=True, blank=True
    )
    descripcion = models.CharField(max_length=100)
    contrato = models.ForeignKey(
        Contrato, on_delete=models.CASCADE, null=True, blank=True
    )
