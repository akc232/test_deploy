from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
# from djangoratings.fields import RatingField
# from django.contrib.contenttypes.fields import GenericRelation
# from star_ratings.models import Rating
from ..loginapp.models import User
from django_counter_field import CounterMixin, connect_counter
from django.contrib.sessions.models import Session


from django.db import models

# Create your models here.

class BookManager(models.Manager):
    def book_create(self, data):
        flash=[]
        # form= [data['title'], data['add_author'], data['review']]
        # print form, "form"

        if data['author_list'] == "null":

            book = self.create(
            title = data['title'],
            author = data['add_author']
            )
            # print book.id, "here is the ID yoooo"
            book_review= Review.objects.create(
            review = data['review'],
            user_id= data['user'],
            rating = data['rating'],
            book_id= book.id,
            )

            flash.append('Post Succesful!')
            return (True, flash)
        else:
            book = self.create(
            title = data['title'],
            author = data['author_list']
            )
            # print book.id, "here is the ID yoooo"
            book_review= Review.objects.create(
            review = data['review'],
            user_id= data['user'],
            rating = data['rating'],
            book_id= book.id,
            )

            flash.append('Post Succesful!')
            return (True, flash)

#!!!!! need to validate for duplicate Authors and create rating stars!!-------------------------------------------------

class ReviewManager(models.Manager):
    def review_create(self, data):
        review = self.create(
        user_id= data['user_id'],
        book_id= data['book_id'],
        review = data['review'],
        rating = data['rating'],
        )
        print " review manager is here"
        return (True, review)




class Book (models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()
    def __unicode__(self):
         return "BookID: "+unicode(self.id)+"Title: "+self.title+"Author: "+unicode(self.author)

class Review (CounterMixin, models.Model):
    review = models.TextField()
    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()
    def __unicode__(self):
         return "Review:"+self.review+" Review_User_ID:"+unicode(self.user)+" Book: "+unicode(self.book)+" Rating: "+unicode(self.rating)
