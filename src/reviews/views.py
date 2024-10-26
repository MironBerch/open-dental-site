from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import redirect
from django.views.generic import View
from django.views.generic.base import TemplateResponseMixin

from reviews.forms import ReviewForm
from reviews.services import get_published_reviews

#  from django.core.paginator import Paginator


class ReviewsView(TemplateResponseMixin, View):
    template_name = 'reviews/view.html'
    form_class = ReviewForm
    #  paginate_by = 10

    def get(self, request: HttpRequest, *args, **kwargs):
        #  paginator = Paginator(get_published_reviews().order_by('id'), self.paginate_by)
        #  page_number = request.GET.get('page')
        #  page_object = paginator.get_page(page_number)
        return self.render_to_response(
            context={
                #  'page_object': page_object,
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
