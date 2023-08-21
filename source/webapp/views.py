from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Article, STATUS_CHOICES
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404
from django.urls import reverse
from webapp.validate import article_validate



def index_view(request):
    articles = Article.objects.order_by('-created_at')
    context = {'articles':articles}
    return render(request, 'index.html', context)


def article_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_view.html', {'article':article})

def create_article(request):
    if request.method == 'GET':
        
        return render(request, 'create.html')
    
    else:

        title = request.POST.get('title')
        author = request.POST.get('author')
        content = request.POST.get('content')
        new_article = Article(title=title, author=author, content=content)    
        errors =  article_validate(title, author, content)
        
        if errors:
            return render(request, 'create.html', {'errors':errors, 'article':new_article})
        new_article.save()
        return redirect('article_view', pk=new_article.pk)
        

def update_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "GET":
        return render(request, 'update.html', {'article':article})
    else:
        article.title = request.POST.get('title')
        article.author = request.POST.get('author')
        article.content = request.POST.get('content')
        article.save()
        return redirect('article_view', pk=article.pk)

def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('index')