from django.shortcuts import render , render_to_response
from django.http import HttpResponse
from .models import imdb
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request,'index.html',{})

@csrf_exempt
def search_titles(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
    else:
        search_text = ''

    articles = imdb.objects.order_by('raing').filter(moviename__icontains=str(search_text))[:5]
    return render_to_response('ajax_search.html',{'articles':articles})

def result(request,num=0):
    data = imdb.objects.get(id=num)
    return render(request,'search_result.html',{'data':data})