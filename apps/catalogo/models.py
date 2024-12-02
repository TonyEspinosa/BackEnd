from django.db import models

# Create your models here.
class m_catalogo(models.Model):
    id_catalogo = models.AutoField(primary_key = True, db_column='id_catalogo')

    nombre = models.CharField(max_length=250, null=True, verbose_name = "Nombre")
    descripcion = models.TextField(max_length=500, null=True, verbose_name = "Descripción")
    date_created = models.DateTimeField(auto_now_add=True, null=True, verbose_name = "Creación")

    class Meta:
        db_table = 'catálogo'
        verbose_name = "catálogo"
        verbose_name_plural = "catálogos"
        ordering = ["nombre"]

    def __str__(self) -> str:
        return self.nombre  # type: ignoree
