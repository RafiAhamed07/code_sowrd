from django.shortcuts import render, get_object_or_404
from .models import Article

# Create your views here.
def blog(request):
    return render(request, 'blog/blog.html')

# View to list all articles
def blog(request):
    articles = Article.objects.all().order_by('-pub_date')
    return render(request, 'blog/blog.html', {'articles': articles})

# View to display a single article
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/article_detail.html', {'article': article})