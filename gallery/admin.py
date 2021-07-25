from django.contrib import admin

from django.utils.safestring import mark_safe

from .models import Gallery


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'preview']
	list_display_links = ['__str__', 'preview']
	
	search_fields = ['id',]

	readonly_fields = ['preview',]

	def preview(self, obj):
		return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')
	preview.short_description = 'Просмотр изображения'
