from django.shortcuts import render
from blog.data import posts

from typing import Any
from django.http import HttpRequest, Http404
# Create your views here.


def blog(request):
    print('blog')

    context = {
        #    'text': 'WE ARE AT BLOG',
           'tittle': 'BLOG',
           'posts': posts
    }

    return render(
        request,
        'blog/index.html',
        context
    )

def post(request: HttpRequest, post_id: int):
    found_post: dict[str, Any] | None = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Http404('Post não existe!')


    context = {
        #    'text': 'WE ARE AT BLOG',
           'tittle': found_post['title'] + ' - ',
           'post': found_post
    }

    return render(
        request,
        'blog/post.html',
        context
    )

    
def example(request):
    print('example')

    context = {
           'text': 'WE ARE AT EXAMPLE',
           'tittle': 'EXAMPLE'

    }

    return render(
        request,
        'blog/example.html',
        context
    )
    
