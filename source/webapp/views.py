from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Article, STATUS_CHOICES
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404
from django.urls import reverse



def index_view(request):
    articles = Article.objects.order_by('-created_at')
    context = {'articles':articles}
    return render(request, 'index.html', context)


def article_view(request, pk):
    # try:
    #     pk = request.GET.get('pk')
    #     article = Article.objects.get(pk=pk)
        
    # except Article.DoesNotExist:
    #     return HttpResponseNotFound('Страница не найдена')
    
    # return render(request, 'article_view.html', {'article':article})
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_view.html', {'article':article})

def create_article(request):
    if request.method == 'GET':
        return render(request, 'create.html', {'statuses': STATUS_CHOICES})
    
    else:
        title = request.POST.get('title')
        author = request.POST.get('author')
        content = request.POST.get('content')
        status = request.POST.get('status')
        new_article = Article.objects.create(title=title, author=author, content=content, status=status)
        # context = {'article':new_article}
        # return HttpResponseRedirect(reverse('article_view', kwargs={'pk': new_article.pk}))
        # return render(request, 'article_view.html', context)
        # return HttpResponseRedirect(f'/article/{new_article.pk}')
        return redirect('article_view', pk=new_article.pk)
        
