import os
from io import BytesIO

from PIL import Image

from django.core.files.base import ContentFile
from django.db import models


def convert_to_webp(image_field, quality=90, resize=None):
    """
    Конвертирует изображение в WebP формат
    :param image_field: Поле ImageField из модели
    :param quality: Качество сжатия (1-100)
    :param resize: Кортеж (width, height) для изменения размера
    :return: Имя файла и ContentFile в WebP формате
    """
    # Открываем изображение
    img = Image.open(image_field)
    # Конвертируем в RGB, если это PNG с прозрачностью
    if img.mode in ('RGBA', 'LA'):
        img = img.convert('RGB')
    # Изменяем размер если нужно
    if resize:
        img.thumbnail(resize)
    # Создаем буфер в памяти
    buffer = BytesIO()
    # Сохраняем в WebP с указанным качеством
    img.save(buffer, format='WEBP', quality=quality)
    # Получаем только имя файла без пути
    original_name = os.path.basename(image_field.name)
    # Меняем расширение на .webp
    filename = os.path.splitext(original_name)[0] + '.webp'
    # Создаем Django-совместимый файловый объект
    webp_file = ContentFile(buffer.getvalue())
    return filename, webp_file


class WebPImageField(models.ImageField):
    """
    Поле для автоматической конвертации изображений в WebP
    """

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 255)
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        file = super().pre_save(model_instance, add)
        if file and not file.name.lower().endswith('.webp'):
            # Конвертируем только если это не WebP
            filename, webp_file = convert_to_webp(file)
            # Сохраняем в той же директории, что указана в upload_to
            file.save(filename, webp_file, save=False)
        return file
