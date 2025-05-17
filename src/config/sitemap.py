from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from clinic.models import Service, ServiceGroup, Work


class MainStaticViewSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return [
            'main',
            'company',
            'reviews',
            'staff',
            'prices',
            'services_groups',
        ]

    def location(self, item):
        return reverse(item)


class StaticViewSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 4.0

    def items(self):
        return [
            'licenses',
            'contacts',
            'gallery',
            'site_map',
            'policy',
        ]

    def location(self, item):
        return reverse(item)


class ServiceGroupSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return ServiceGroup.objects.all()

    def location(self, obj: ServiceGroup):
        return reverse('services_group', kwargs={'slug': obj.slug})


class ServiceSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.7

    def items(self):
        return Service.objects.filter(published=True)

    def location(self, obj: Service):
        return reverse('service', kwargs={'slug': obj.slug})


class WorkSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.6

    def items(self):
        return Work.objects.all()

    def location(self, obj: Work):
        return reverse('work', kwargs={'slug': obj.slug})
