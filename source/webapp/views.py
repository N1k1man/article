from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Article, STATUS_CHOICES
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404
from django.urls import reverse
from webapp.validate import article_validate
from webapp.forms import ArticleForm



def index_view(request):
    articles = Article.objects.order_by('-created_at')
    context = {'articles':articles}
    return render(request, 'index.html', context)


def article_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_view.html', {'article':article})

def create_article(request):
    if request.method == 'GET':
        form = ArticleForm()
        
        return render(request, 'create.html', {'form':form})
    
    else:
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            author = form.cleaned_data.get('author')
            content = form.cleaned_data.get('content')
            status = form.cleaned_data.get('status')
            publish_date = form.cleaned_data.get('publish_date', None)
            new_article = Article.objects.create(title=title, author=author, content=content, status=status, publish_date=publish_date)    
            return redirect('article_view', pk=new_article.pk)
        
        
        return render(request, 'create.html', {'form':form})
        
        
        

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