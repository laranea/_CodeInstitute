# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from django.http import HttpResponseRedirect


# Create your views here.
def redirect_root(request):
    return HttpResponseRedirect('/blog/')


def post_list(request):
    """
    Create a view that will return a list of
    Posts that were published prior to 'now' and
    render them to the 'blogposts.html' template
    :param request:
    :return:
    """

    posts = Post.objects.filter(published_date__lte=timezone.now()
                                ).order_by('-published_date')
    return render(request, "blogposts.html", {'posts': posts})


def post_detail(request, id):
    """
    Create a view that return a single
    Post object based on the post ID and
    and render it to the 'postdetail.html'
    template. Or return a 404 error if the
    post is not found
    """
    post = get_object_or_404(Post, pk=id)
    post.views += 1  # clock up the number of post views
    post.save()
    return render(request, "postdetail.html", {'post': post})


def display_top_five_posts(request):
    """
    we wnat to get and list the top five most popular
    blog posts and display them in blogpost.html on clicking the
    link in the navigation menu
    :param request:
    :return:
    """
    top_posts = Post.objects.filter(published_date__lte=timezone.now()
                                    ).order_by('-views')[:5]
    return render(request, "blogposts.html", {'posts': top_posts})