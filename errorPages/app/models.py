from django.db import models

class ErrorLog(models.Model):
    # es igual a poner varchar(10)
    codigo = models.CharField(max_length=10)
    # es igual a lontText
    mensaje = models.TextField()
    # es igual Date(now())
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"(codigo) - (mensaje)"#{codigo} - {mensaje}