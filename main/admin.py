from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe

from .models import Document, New, Block, License
from ckeditor.widgets import CKEditorWidget



class NewAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = New
        fields = '__all__'


class NewsModelAdmin(admin.ModelAdmin):
    form = NewAdminForm


class LicenseModelAdmin(admin.ModelAdmin):
    list_display = ('pk', "title",'image_tag')
    list_display_links = ('pk', 'title','image_tag')
    readonly_fields = ['img_image']

    def img_image(self, obj):
        return mark_safe(
            '<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.img.url,
            width=400,
            height=600,
        )
        )

    class Meta:
        model = License


class DocumentModelAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'
    list_display = ('pk', 'description', 'uploaded_at', )
    list_display_links = ('pk', 'description')


class BlockModelAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто'
    list_display = ('pk', 'type', 'text')
    list_display_links = ('pk', 'type', 'text')


admin.site.register(Document, DocumentModelAdmin)
admin.site.register(New, NewsModelAdmin)
admin.site.register(Block, BlockModelAdmin)
admin.site.register(License, LicenseModelAdmin)
