## DRF Overview
# DRF helps simplify the work we do to expose the models we create via an API. We use a single URL, 
# per resource that interprets the action based on the header method. (e.g. POST header calls a 
# save method).

# The URL for our "context" model in the "engagement" app looks like:
# mysidewalk.com/api/engagement/v1/context
# The above URL handles our List and Create style methods

# The URL below would handle a Delete or Update request:
# mysidewalk.com/api/engagement/v1/context/1
# Where "1" represents the ID of the context we are looking to update or delete.



## Basic View Sets
# A basic view set in our django apps inherits individually from each method type that we want to 
# expose (that is to say, the class inherits from the ListModelMixin to expose the list style
# request).

# We can define a simple view set by creating a new class following our naming convention of 
# "{model_name}ViewSet", where model_name is the PascalCase of the model.

# The view set below exposes a list and create method while not accepting update, delete or retrieve
from rest_framework import mixins as rf_mixins
from libs.viewset_mixins import MindMixerViewSet

class ExampleModelViewSet(rf_mixins.ListModelMixin, rf_mixins.CreateModelMixin, MindMixerViewSet):
    model = ExampleModel

# There is at least one important thing to note when using mixins for a view set. As we know from
# learning about our model audit mixins, we need to make sure the API helps us accomplish that.
# For every view set, we should be sure to inherit not from REST Frameworks's mixins for the create,
# modify, or delete actions. These have been wrapped by a class that handles updating the audit
# fields for each request.
from rest_framework import mixins as rf_mixins
from libs.viewset_mixins import CreateModelMixin, ModifyModelMixin, DeleteModelMixin,
    MindMixerViewSet

class ExampleModelTwoViewSet(rf_mixins.ListModelMixin, CreateModelMixin, ModifyModelMixin,
                             DeleteModelMixin, MindMixerViewSet):
    model = ExampleModelTwo



## Interacting with Angular.js
# DRF allows us to create a single endpoint per resource (model) that our Angular.js app can
# work with. In angular we can create a new "resource" which allows us to call standard methods
# on while it handles all of the http request information, including setting the headers, query
# parameters, and request body.

# Each resource then has the ability to make GET, POST, PUT/PATCH, DELETE requests. This is where
# DRF's single class based view handles the interpretation of that request into a method on the
# view set that it will call (e.g. get, list, save, update, delete)



## URLs
# We are going to focus on how MindMixer leverages URLs and therefore some basic permissions
# (covered more in depth later). In order to define a new API URL at MindMixer, we must do a few
# things. First, make sure we have created a view set that only exposes the needed methods. Second,
# is to specify that in the urls.py file of the app.

from django.conf.urls import url
from rest_framework import routers

from libs.components.permissions.resources import AppResources

from example import views

# Specify the version and app name
app_resources = AppResources(1, 'appname')
create_resource = app_resources.create_resource

# Creates a new resource url based on the property name you assign the resource to. For example, 
# the url for this resource for this would be:
# /api/appname/v1/example-models
# because, "appname" was the given string above since that is the name of the django app we are
# working in. "v1" because we gave it the argument "1". "example-models" because we gave it the 
# property name "example_models".


app_resources.example_models = create_resource(
    viewset=views.ExampleModelViewSet,
)

router = routers.DefaultRouter(trailing_slash=False)
for resource in app_resources.get_resources():
    router.register(resource.noun, resource.viewset)

urlpatterns = router.urls