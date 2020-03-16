from django.shortcuts import render, get_object_or_404, redirect

from django.core import serializers
from django.http import HttpResponse, JsonResponse

from django.utils import timezone
from .models import Post, Posting
from .forms import PostForm, PostingForm
import requests
import json


def post_list(request):
  # queryset
  posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
  return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
  post = Post.objects.get(pk=pk)
  return render(request, 'blog/post_detail.html', {'post': post})

# form 을 통한 body는 request.POST에 있음
def post_new(request):
  if request.method == "POST":
    form = PostForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      post.author = request.user
      post.published_date = timezone.now()
      post.save()
      return redirect('post_detail', pk=post.pk)

  else:
    form = PostForm()  
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
  post = get_object_or_404(Post, pk=pk)
  if request.method == 'POST':
    form = PostForm(request.POST, instance=post)
    if form.is_valid():
      post = form.save(commit=False)
      post.author = request.user
      post.published_date = timezone.now()
      post.save()
      return redirect('post_detail', pk=post.pk)
  else:
    form = PostForm(instance=post)
  
  return render(request, 'blog/post_edit.html', {'form': form})

def posting_detail(request, pk):
  posting = Posting.objects.get(pk=pk)
  return render(request, 'blog/posting_detail.html', {'posting': posting})

def posting_list(request):
  if request.method == 'POST':
    body = json.loads(request.body.decode("utf-8"))
    data = json.loads(requests.get(body["url"]).text)

    posting_instance = Posting(
      location_id = data["graphql"]["location"]["id"],
      name = data["graphql"]["location"]["name"],
      link = 'https://www.instagram.com/explore/locations/' + data["graphql"]["location"]["id"],
      lat = data["graphql"]["location"]["lat"],
      lng = data["graphql"]["location"]["lng"],
      country_code = data["graphql"]["location"]["directory"]["country"]["id"],
      country_name = data["graphql"]["location"]["directory"]["country"]["name"],
      city_id = data["graphql"]["location"]["directory"]["city"]["id"],
      city_name = data["graphql"]["location"]["directory"]["city"]["name"],
      phone = data["graphql"]["location"]["phone"],
      website = data["graphql"]["location"]["website"],
      picture_url = data["graphql"]["location"]["profile_pic_url"],
      posting_cnt = data["graphql"]["location"]["edge_location_to_media"]["count"],
      published_date = timezone.now(),
      created_time = timezone.now(),
    )
    posting_instance.save()
    
    return redirect('posting_detail', pk=posting_instance.pk)
  else:
    postings = Posting.objects.filter(created_time__lte=timezone.now()).order_by('created_time')
    return render(request, 'blog/postings_list.html', {'postings': postings})

def map(request):
  postings = Posting.objects.filter(created_time__lte=timezone.now()).order_by('created_time')
  postings_list = list()
  for posting in postings:
    each = {}
    each["location_id"] = posting.location_id
    each["name"] = posting.name
    each["link"] = posting.link
    each["lat"] = posting.lat
    each["lng"] = posting.lng
    each["country_code"] = posting.country_code
    each["country_name"] = posting.country_name
    each["city_id"] = posting.city_id
    each["city_name"] = posting.city_name
    each["phone"] = posting.phone
    each["website"] = posting.website
    each["picture_url"] = posting.picture_url
    each["posting_cnt"] = posting.posting_cnt
    # each["published_date"] = posting.published_date
    # each["created_time"] = posting.created_time
    postings_list.append(each)

  print('postings', postings_list)
  return render(request, 'blog/map.html', {'postings': postings_list})