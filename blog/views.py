from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from models import Post

def archive(request):
    posts = Post.objects.filter(status=Post.PUBLISHED)
    return render_to_response('blog.html', RequestContext(request, {
        'mediaPosts' : posts,
    }))

def year(request, year):
    # todo
    return render_to_response('blog/year.html', RequestContext(request, { }))

def month(request, year, month):
    # todo
    return render_to_response('blog/month.html', RequestContext(request, { }))

def post(request,  year, month, slug):
    post = get_object_or_404(Post, slug=slug)
    return render_to_response('blog/post.html', RequestContext(request, {
        'post' : post
    }))