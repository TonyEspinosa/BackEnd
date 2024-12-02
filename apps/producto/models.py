from django.db import models

# Create your models here.
class m_producto(models.Model):
    id_producto = models.AutoField(primary_key = True, db_column='id_producto')

    nombre = models.CharField(max_length=250, null=True, verbose_name = "Nombre")
    descripcion = models.TextField(max_length=500, null=True, verbose_name = "Descripción")
    
    date_created = models.DateTimeField(auto_now_add=True, null=True, verbose_name = "Creación")

    class Meta:
        db_table = 'producto'
        verbose_name = "producto"
        verbose_name_plural = "productos"
        ordering = ["nombre"]

    def __str__(self) -> str:
        return self.nombre  # type: ignoree
