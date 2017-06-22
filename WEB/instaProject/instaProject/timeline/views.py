from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post
# Create your views here.


@login_required
def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:10]
    template = loader.get_template('timeline/index.html')
    context = {'latest_post_list': latest_post_list, }
    return HttpResponse(template.render(context, request))


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'timeline/detail.html', {'post': post})
