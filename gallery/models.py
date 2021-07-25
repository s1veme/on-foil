from django.db import models

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Gallery(models.Model):
	image = ProcessedImageField(
		verbose_name='Картинка',
		upload_to='gallery',
		processors=[ResizeToFill(400, 300)],
		format='JPEG',
		options={'quality': 80}
	)

	def __str__(self):
		return f'Фото-{self.id}'

	class Meta:
		verbose_name = 'галерея'
		verbose_name_plural = 'галерея'