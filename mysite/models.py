from django.db import models
from django.urls import reverse
import datetime
from django.utils import timezone
import pytz
utc=pytz.UTC

class Member(models.Model):
    roll_number = models.CharField(max_length=8, primary_key=True)
    member_name = models.CharField(max_length=25)
    post = models.CharField(max_length=50, blank=True, help_text='Enter for past postholders also. ex, <batch> Convener for a past batch convener')
    insta = models.URLField(verbose_name="Instagram profile URL", blank=True)
    email = models.EmailField(max_length = 50,default=" ")
    batch = models.CharField(verbose_name='Batch', max_length=4, help_text="passing year")
    curr_core = models.BooleanField(default=False, help_text="Is this member current core member?")
    testimonial = models.TextField(default=" ", blank=True)
    member_img = models.ImageField(upload_to='images/members')
    active = models.BooleanField(verbose_name="member status", default=True)
    class Meta:
        ordering = ['-batch', '-member_name']
    def __str__(self):
        return self.member_name
    @property
    def alumni_filter(self):
        curr_year = datetime.datetime.now().year
        return self.batch + 4 < curr_year and self.batch < curr_year
    @property
    def core_filter(self):
        return self.curr_core and self.active

class Event(models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField(default=" ")
    date = models.DateTimeField(auto_now_add=False, default=timezone.now())
    resources = models.CharField(verbose_name='Event Resources', max_length=100, blank=True)
    @property
    def is_past(self):
        utc_date = utc.localize(datetime.datetime.now())
        return utc_date < self.date

    def __str__(self):
        return self.title


class Art(models.Model):
    SKT = 'Sketches'
    DDL = 'Doodles'
    ABS = 'Abstract'
    ANIM = 'Anime'
    PRT = 'Portrait'
    NTR = 'Nature'
    DGT = 'Digital'
    OTR = 'Other'
    art_choices = [
        (SKT, 'Sketches'),
        (DDL, 'Doodles'),
        (ANIM, 'Anime'),
        (ABS, 'Abstract'),
        (PRT, 'Portrait'),
        (NTR, 'Nature'),
        (DGT, 'Digital'),
        (OTR, 'Other')
    ]
    art_image = models.ImageField(upload_to='images/art')
    title = models.CharField(max_length=20)
    author = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='art_posts')
    created_on = models.DateTimeField(auto_now_add=True)
    art_type = models.CharField(verbose_name='Type', max_length=20, choices=art_choices)
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=30)
    blog_filter = models.IntegerField(default=0)
    author = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    blog_img = models.ImageField(upload_to='images/blog')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class EventImage(models.Model):
    img = models.ImageField(upload_to='images/event')
    title = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_posts')

    def __str__(self):
        return self.title.title


#Udaan model
class Udaan_static(models.Model):
    main_description= models.TextField()
    date= models.DateTimeField( auto_now=False, auto_now_add=False, null = True)
    def __str__(self):
        return self.main_description


class Udaan_image(models.Model):
    img_name = models.CharField( max_length=50)
    img = models.ImageField( upload_to='images/udaan/carousel', height_field=None, width_field=None, max_length=None)
    alt_text = models.CharField( max_length=50)
    display_on_caurosel = models.BooleanField(default = False)

    def __str__(self):
        return self.alt_text

class Udaan_event(models.Model):
    event_name= models.CharField( max_length=50)
    event_description= models.TextField()
    event_img= models.ImageField( upload_to='images/udaan/events', height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return self.event_name   

class Gallery(models.Model):
    description = models.TextField(default=" ")
    image = models.ImageField(upload_to='images/gallery')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

class Comment(models.Model):
    post = models.ForeignKey(to=Blog, on_delete=models.CASCADE, related_name='post_comment')
    author = models.CharField(verbose_name='author', max_length=30, blank=False)
    body = models.TextField(verbose_name='Post Comment')
    email = models.EmailField(verbose_name='email')
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['-created_on']

    def __str__(self):
        return self.body
