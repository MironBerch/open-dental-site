from django import forms
from django.contrib import admin, messages
from django.contrib.auth.models import Group
from django.shortcuts import redirect, render
from django.urls import path
from django.utils.html import format_html

from clinic.models import (
    About,
    Contact,
    License,
    Photo,
    Policy,
    Price,
    PriceGroup,
    Review,
    Service,
    ServiceGroup,
    Staff,
    Work,
)
from clinic.services import parse_yandex_reviews

admin.site.unregister(Group)
admin.site.register(About)
admin.site.register(Policy)
admin.site.register(PriceGroup)


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'cost',
        'constant',
        'group__name',
        'published',
    )
    list_filter = ('group__name', 'constant')


class HTMLImportForm(forms.Form):
    html_content = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 20, 'cols': 100}),
        label='Вставьте HTML-код страницы с отзывами'
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'created_at', 'published')
    list_filter = ('rating', 'published')
    change_list_template = 'admin/reviews_change_list.html'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('parse-reviews/', self.admin_site.admin_view(self.parse_reviews_view)),
        ]
        return custom_urls + urls

    def parse_reviews_view(self, request):
        if request.method == 'POST':
            form = HTMLImportForm(request.POST)
            if form.is_valid():
                html_content = form.cleaned_data['html_content']
                try:
                    count = parse_yandex_reviews(html_content)
                    messages.success(request, f'Успешно обработано {count} отзывов')
                    return redirect('admin:clinic_review_changelist')
                except Exception as e:
                    messages.error(request, f'Ошибка: {str(e)}')
        else:
            form = HTMLImportForm()

        context = {
            **self.admin_site.each_context(request),
            'form': form,
            'opts': self.model._meta,
            'title': 'Импорт отзывов из HTML'
        }
        return render(request, 'admin/html_import.html', context)


@admin.register(License)
class LicenseAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'published',
        'view_image',
    )
    list_filter = ('published', )

    def view_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 160px; height: 230px;" />',
                obj.image.url,
            )
        return "Нет изображения"


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'address',
        'opening_hours',
        'phone_numbers',
        'email',
        'tg',
        'whatsapp',
        'vk',
    )


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = (
        'fio',
        'published',
        'view_image',
        'roles',
    )
    list_filter = ('published', )
    prepopulated_fields = {
        'slug': ('fio', ),
    }

    def view_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 160px; height: 230px;" />',
                obj.image.url,
            )
        return "Нет изображения"

    view_image.short_description = 'Фото'


@admin.register(ServiceGroup)
class ServiceGroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name', ),
    }


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name', ),
    }
    list_display = (
        'name',
        'group',
        'published',
    )
    list_filter = ('group', 'published', )


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name', ),
    }
    list_display = (
        'name',
        'published',
        'view_image',
    )
    list_filter = ('published', )
    inlines = (PhotoInline, )

    def view_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 100px; height: 75px;" />',
                obj.image.url,
            )
        return "Нет изображения"

    view_image.short_description = 'Превью'


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        'work__name',
        'view_image',
    )
    list_filter = ('work__name', )

    def view_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 100px; height: 75px;" />',
                obj.image.url,
            )
        return "Нет изображения"

    view_image.short_description = 'Фото'
