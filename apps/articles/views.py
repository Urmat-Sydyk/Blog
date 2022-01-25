from django.http import Http404
from django.shortcuts import render
from django.views import generic
from apps.articles.models import Article

class ArticleListView(generic.TemplateView):
    """Представления для получения всех публикации"""
    template_name = 'article-list.html'

    def get_context_data(self, **kwargs):
        context = dict()
        context['article_list']=Article.objects.all()
        return context



class ArticleDetailView(generic.TemplateView):
    """Представления для получения детальной страницы публикации"""

    template_name = 'article-detail.html'

    def get_context_data(self, **kwargs):
        context = dict()
        article_pk = kwargs['pk']
        try:
            context['article'] = Article.objects.get(id=article_pk)
        except Article.DoesNotExits:
            raise Http404
        return context