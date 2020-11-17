from django.shortcuts import render
from articles.models import Article

def homepage(request):

    featured = Article.objects.filter(featured='Y')[0]
    three_articles = Article.objects.all().order_by('-date')[:3]


    context = {'featured': featured, 'three_articles': three_articles}
    return render(request, 'homepage/index.html', context)