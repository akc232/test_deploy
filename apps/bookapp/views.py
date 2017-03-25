from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User, Book, Review
from django.core.urlresolvers import reverse
# Create your views here.



def index(request):
    #displays main page
    if 'id' not in request.session:
        return redirect ('login:index')
    else:
        context={
        'reviews': Review.objects.all().order_by('-id'),
        'books': Book.objects.all().order_by('title'),

        }
        # print context
        return render (request, 'bookapp/index.html', context)

def new(request):
    if 'id' not in request.session:
        return redirect ('login:index')
    #displays add book page
    context = {
        'authors': Book.objects.all()
    }

    return render(request, 'bookapp/add_book.html', context)

def create(request):
    if 'id' not in request.session:
        return redirect ('login:index')
    else:
        book_process = Book.objects.book_create(request.POST)
        # review_process = Book.objects.create_book_review(request.POST)
        if book_process[0] == True:
            print book_process, "Process returns!"
            # print review_process
        # print process,"<---------"
        #creates new book
        return redirect('books:index')

def create_review(request):
    if 'id' not in request.session:
        return redirect ('login:index')

    else:
        create = Review.objects.review_create(request.POST)
        print 'testinggg'
        if create[0] == True:
            print "review created!"

        return redirect(reverse('books:books', kwargs={'id':create[1].book_id}))


#
def show(request, id):
    # print request.session['name']
    context = {
        'books': Book.objects.filter(id=id),
        'reviews':Review.objects.filter(book_id=id),
        'ids': Review.objects.filter(book_id=id),
    }

    session_id = request.session['id']
    book = Book.objects.filter(id=id)

    print session_id
    book_id= book[0].id

    # if session_id == review_user[0].user_id:
    #     remove= Review.objects.get(book_id=id)
    #     remove.delete()
    #     remove.save()
        #allowing session user to delete own reviews
    return render (request, 'bookapp/show_book.html', context)

def user(request,id):

    context = {
        'users': User.objects.filter(id=id),
        'reviews':Review.objects.filter(user_id=id).count(),
        'posts': Review.objects.filter(user_id=id).distinct(),

    }
    # print context

    return render(request, 'bookapp/user_review.html',context)














# index: Display all products
# show: Display a particular product
# new: Display a form to create a new product
# edit: Display a form to update a product
# create: Process information to create a new product
# update: Process information from the edit form and update the particular product
# destroy: Remove a product

# Action	HTTP Verb	Route Path	Function
# Retrieve all pets	GET	/pets	index
# Display form to create a new pet	GET	/pets/new	new
# Create a new pet	POST	/pets	create
# Display specific pet	GET	/pets/<id>	show
# Display form to update a specific pet	GET	/pets/<id>/edit	edit
# Update a specific pet	PUT or PATCH	/pets/<id>	update
# Delete a specific pet	DELETE	/pets/<id>	destroy
# For semi-RESTful architecture, you can append a /destroy to the destroy route.
