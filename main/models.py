from django.contrib.auth import get_user_model
from django.db import models
from django.utils.safestring import mark_safe
from pytils.translit import slugify, translify
from ckeditor.fields import RichTextField

User = get_user_model()


class New(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="posts")
    text = RichTextField()
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    url = models.SlugField(verbose_name='URL', null=True,
                            blank=True, unique=True)

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.url:
            self.url = slugify(self.title)
        return super().save(*args, **kwargs)


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True,
                                   verbose_name='Описание')
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')
    url = models.SlugField(verbose_name='Путь', null=True,
                           blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.url:
            self.url = slugify(self.description)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'


def get_image_filename(instance, filename):
    title = instance.title
    id_image = instance.id
    slug = slugify(title)
    convert_filename = translify(filename)
    return "license_images/%s/%s-%s" % (id_image, slug, convert_filename)


class License(models.Model):
    title = models.CharField(max_length=200, verbose_name='Наименование')
    img = models.ImageField(upload_to='license_images/',
                            verbose_name='Изображение',
                            default='license_images/no-img.jpg')

    class Meta:
        verbose_name = 'Лицензия'
        verbose_name_plural = 'Лицензии'

    def image_tag(self):
        if self.img:
            return mark_safe(
                '<img src="%s" style="width: 150px; height:150px;" /license_images/>'
                % self.img.url)
        else:
            return 'No Image Found'

    image_tag.short_description = 'Image'


class Block(models.Model):
    type = models.CharField(max_length=50, verbose_name='Тип блока')
    text = models.CharField(max_length=300, verbose_name='текст блока')

    class Meta:
        verbose_name = 'Блок сайта'
        verbose_name_plural = 'Блоки сайта'


