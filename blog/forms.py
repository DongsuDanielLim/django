from django import forms
from .models import Post, Posting

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'text',)

class PostingForm(forms.ModelForm):
  class Meta:
    model = Posting
    fields = ('location_id', 'name', 'lat', 'lng', 'link', 'country_code', 'country_name', 'city_id', 'city_name', 'phone', 'website', 'picture_url', 'posting_cnt', 'created_time')