from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import redirect
from django.views.generic import View
from django.views.generic.base import TemplateResponseMixin

from reviews.forms import ReviewForm
from reviews.services import get_published_reviews


class ReviewsView(TemplateResponseMixin, View):
    template_name = 'reviews/view.html'
    form_class = ReviewForm

    def get(self, request: HttpRequest, *args, **kwargs):
        return self.render_to_response(
            context={
                'form': self.form_class(),
                'active_page': 'reviews',
                'reviews': get_published_reviews().order_by('-id'),
            },
        )

    def post(self, request: HttpRequest, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            messages.add_message(
                request,
                messages.SUCCESS,
                'Отзыв успешно оставлен',
            )
            form.save()
            return redirect('reviews')
        return self.render_to_response(
            context={
                'form': self.form_class,
                'active_page': 'reviews',
                'reviews': get_published_reviews().order_by('-id'),
            },
        )
