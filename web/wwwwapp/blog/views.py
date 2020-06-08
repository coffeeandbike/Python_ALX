from django.http import HttpResponse, Http404
from django.shortcuts import render
from blog.models import Post
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

def test(request, imie, wiek):
    # imie = request.GET.get('imie')
    # return HttpResponse(f'<html><body><h1>Hello {imie}!!!</h1></body></html>')
    # http://127.0.0.1:8000/test?imie=ziomek
    template_data = {
        't_imie': imie,
        't_wiek': wiek,
    }
    return render(request, 'blog/test.html', template_data)


def homepage(request):
    # posts = Post.objects.all() #to powoduje wziecie takze nieopublikowanych postow
    posts = Post.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'blog/homepage.html', {'posts': posts})


def post_show(request, slug):
    try:
        post = Post.objects.filter(is_published=True).get(slug=slug)
        return render(request, 'blog/post_show.html', {'post': post})
    except ObjectDoesNotExist:
        raise Http404('Nie ma takiego postu')
