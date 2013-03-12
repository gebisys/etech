from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField("Titulo", max_length=60)
	slug = models.SlugField(unique_for_date='pub_date')
	pub_date = models.DateTimeField("Fecha de edicion", auto_now_add=True)
	body = models.TextField()
	author = models.ForeignKey(User, verbose_name="Autor")

	# Para generar la url de cada entrada
	def get_absolute_url(self):
		return '/%(id)d/%(slug)s/' % ({'id' : self.id, 'slug' : self.slug})

	class Meta:
		ordering = ['-pub_date']
		verbose_name_plural = 'Noticias'
		verbose_name = 'Noticia'
