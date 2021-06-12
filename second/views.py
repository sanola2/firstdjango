from django.shortcuts import render
from django.http import HttpResponseRedirect
from second.models import Post, Comment
from .forms import PostForm, CommentForm


def list(request):
  context = {
    'items' : Post.objects.all()
  }
  return render(request, 'second/list.html', context)


def create(request):
  if request.method == 'POST':
    form = PostForm(request.POST)
    if form.is_valid():
      form.save()
    return HttpResponseRedirect('/second/list/')

  form = PostForm()
  return render(request, 'second/create.html', {'form': form})


def confirm(request):
  form = PostForm(request.POST)
  if form.is_valid():
    return render(request, 'second/confirm.html', {'form': form} )
  return HttpResponseRedirect('/second/create/')


def post(request, post_id):
  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
      form.save()
    return HttpResponseRedirect('/second/post/' + str(post_id))

  form = CommentForm()
  context = {
    'post': Post.objects.get(id=post_id),
    'post_id': post_id,
    'comments': Comment.objects.all()
  }
  return render(request, 'second/post.html', { 'context': context, 'form': form })
