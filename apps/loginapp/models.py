from __future__ import unicode_literals
from django.forms import extras
from django.db import models
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned, ValidationError
import re, bcrypt
from django_counter_field import CounterField

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[a-zA-Z\-]+$')
# BIRTHDAY_REGEX= re.compile(r'^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[1,3-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$')

# Create your models here.
class UserManager(models.Manager):
    def create_new_user(self, data):
        flash=[]

        if len(data['first_name'])< 2:
            flash.append('First Name must be greater than 2 letters')

        elif not NAME_REGEX.match(data['first_name']):
            flash.append('First name can not contian numbers or special characters!')

        if len(data['last_name']) < 2:
            flash.append('Last name must be at least 2 characters!')

        elif not NAME_REGEX.match(data['last_name']):
            flash.append('Last name can not contian numbers or special characters!')

        if not EMAIL_REGEX.match(data['email']):
            flash.append('Email Format is Invalid!')

        if data['password'] != data['confirm']:
            flash.append('Passwords do not match!')

        elif len(data['password']) <8:
            flash.append('Password Must be 8 or more characters long!')

        try:
            double=User.objects.get(email=data['email'])
            form= data['email']
            if form == double.email:
                flash.append('User is already registered. Please Log In or Create New User. ')

        except ObjectDoesNotExist:
            print "does not exist"
            pass

        if flash:
            return (False, flash)

        else:
            try:
                secret= data['password'].encode()
                hashed = bcrypt.hashpw(secret, bcrypt.gensalt())

                create= User.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                password=hashed,
                )
                # print "Birthday data ---->", data['birthday']
                # flash.append("Succesful! User Registered!!")
                return (True, flash, create)
            except ValidationError:
                flash.append('Invalid Date Format! Please enter Date!')
                return(False, flash)


    def check_user(self, data):
        flash=[]
        try:
            registered=User.objects.get(email=data['email'])
            # print registered.id,"from models"
            if bcrypt.checkpw(data['password'].encode(), registered.password.encode()) != True:
                flash.append('Email or Password is Incorrect')
                return (False,flash, registered)
            else:
                return (True,registered)

        except ObjectDoesNotExist:
            print "not a user"
            pass
            flash.append('Email or Password in Incorrect')
        return (False, flash)

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
    def __unicode__(self):
        return "user_ID:"+str(self.id)+ " First:"+self.first_name+" Last:"+ self.last_name+" Email:"+ self.email
