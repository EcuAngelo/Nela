from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField()
    descripcion = models.TextField()
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    url = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['-created']
    
    def __str__(self):
        return self.title