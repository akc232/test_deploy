from django.conf.urls import url

from . import views

app_name= 'books'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add$', views.new, name='add_book'),
    url(r'^create$', views.create, name='create'),
    url(r'^create_review$', views.create_review, name='create_review'),
    url(r'^books/(?P<id>\d+)$', views.show, name='books'),
    url(r'^user/(?P<id>\d+)$', views.user, name='user'),
    # url(r'^$', edit, name='edit'),
    # url(r'^$', update, name='update'),
    # url(r'^destroy/(?P<id>\d+)$', destroy, name='destroy'),

]



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
