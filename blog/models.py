from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  text = models.TextField()
  created_date = models.DateTimeField(
    default=timezone.now
  )
  published_date = models.DateTimeField(
    blank=True, null=True
  )

  def publish(self):
    self.published_date = timezone.now()
    self.save()
  
  def __str__(self):
    return self.title

class Posting(models.Model):
  location_id = models.CharField(max_length=50) # graphql.location.id
  name = models.CharField(blank=True, null=True, max_length=100) # graphql.location.name
  lat = models.FloatField(blank=True, null=True) # graphql.location.lat
  lng = models.FloatField(blank=True, null=True) # graphql.location.lon
  link = models.CharField(max_length=300)
  country_code = models.CharField(blank=True, null=True, max_length=3) # graphql.directory.country.id
  country_name = models.CharField(blank=True, null=True, max_length=30) # graphql.directory.country.name
  city_id = models.CharField(blank=True, null=True, max_length=20) # graphql.directory.city.id
  city_name = models.CharField(blank=True, null=True, max_length=100) # graphql.directory.city.name
  phone = models.CharField(blank=True, null=True, max_length=20) # graphql.location.phone
  website = models.CharField(blank=True, null=True, max_length=300) # graphql.location.website
  picture_url = models.CharField(blank=True, null=True, max_length=500) # graphql.location.profile_pic_url
  posting_cnt = models.IntegerField(blank=True, null=True) # edge_location_to_media.count
  created_time = models.DateTimeField( # models.DateTimeField(default=timezone.now)
    default=timezone.now
  )

  published_date = models.DateTimeField(
    blank=True, null=True
  )
  
  def publish(self):
    self.published_date = timezone.now()
    self.save()
  
  def __str__(self):
    return self.location_id
