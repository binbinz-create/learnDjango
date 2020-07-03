from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
from blog.models import Article

def hello_world(request):
    return HttpResponse("Hello world")

def article_content(request):
    article = Article.objects.all()[0]
    title = article.title
    brief_content = article.brief_content
    content= article.content
    return_str = "title: %s ,brief_content: %s, content:%s " % (title,brief_content,content)
    return HttpResponse(return_str)

def get_index_page(request):
    all_article = Article.objects.all()
    return render(request,"blog/index.html",{
        'article_list':all_article
    })

def get_detail_page(request,article_id):
    all_article = Article.objects.all()
    curr_article = None
    for article in all_article:
        if article.article_id == article_id:  #匹配指定id的article
            curr_article = article
            break

    content_list = curr_article.brief_content.split('\n')
    return render(request,"blog/detail.html",{
        'curr_article':curr_article,
        'content_list':content_list
    })

