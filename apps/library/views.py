from django.http import Http404
from django.shortcuts import render
from django.views import generic
from apps.library.models import Book


class BookListView(generic.TemplateView):
    """Представления для получения всех публикации"""
    template_name = 'book-list.html'

    def get_context_data(self, **kwargs):
        context = dict()
        context['book_list']=Book.objects.all()
        return context



class BookDetailView(generic.TemplateView):
    """Представления для получения детальной страницы публикации"""

    template_name = 'book-detail.html'

    def get_context_data(self, **kwargs):
        context = dict()
        book_pk = kwargs['pk']
        try:
            context['book'] = Book.objects.get(id=book_pk)
        except Book.DoesNotExits:
            raise Http404
        return context
