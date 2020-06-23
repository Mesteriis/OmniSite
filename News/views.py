from django.shortcuts import render
from .models import News
from django.views.generic import  ListView, DetailView
from .forms import newsFormAdd
# Create your views here.

class newsListView(ListView):
    model = News
    template_name = 'News/news.html'
    context_object_name = 'list_news'
    ordering = ['-id']

class detailNewsView(DetailView):
    model = News
    template_name = 'News/detail.html'
    context_object_name = 'get_news'


# class adminNews(ListView):
#     model = News
#     template_name = 'News/adminNews.html'
#     context_object_name = {'list_news', newsFormAdd}

def admNews(request):
    saveSuccess = False
    if request.method == 'POST':
        form = newsFormAdd(request.POST)
        if form.is_valid():
            form.save()
            saveSuccess = True


    list_news = News.objects.all ().order_by('-id')
    template = 'News/adminNews.html'
    content = {
        'list_news': list_news,
        'form': newsFormAdd(),
        'saveSuccess' : saveSuccess
    }
    return render ( request, template, content )




# def detail(request,id):
#     get_news = News.objects.all().get(id=id)
#     template = 'News/detail.html'
#     content = {
#         'get_news': get_news
#     }
#     return render ( request, template, content )