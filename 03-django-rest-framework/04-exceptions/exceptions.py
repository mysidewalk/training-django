## Overriding default view set methods
# We can of course define a custom view set method by hand rather than rely on the default behavior.
# We have done this in a number of places, two notably ones are the login view set and the media
# view set.
from rest_framework.mixins import mixins as rf_mixins
from libs import viewset_mixins as mm_mixins

class ExampleOneViewSet(rf_mixins.ListModelMixin, mm_mixins.CreateModelMixin,
                        mm_mixins.MindMixerViewSet):
    model = ExampleOneViewSet
    queryset = model.objects.all()

    # We can specify a list, create, retrieve, update, partial_update, or destroy method in a view
    # set which will override existing default behavior from a mixin.
    def list(self, request):
        pass

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

    # There are several more methods to note that we can hook into and modify, they are called
    # before and after actions
    def pre_save(self, obj):
        pass
    
    def post_save(self, obj, created=False):
        pass

    def pre_delete(self, obj):
        pass

    def post_delete(self, obj):
        pass

    # When overriding one of the above methods to add a small custom piece of functionality, it 
    # generally makes sense not to have to re-write the existing functionality. In Python, we can
    # do this by calling something using the "super" function which allows us to call the inherited
    # method rather than the one we defined.

    # We could for example, update the pre_save or pre_delete, but in general it makes sense not to
    # eliminate the default behavior, see an example of how to accomplish that below:
    def pre_save(self, obj, created=False):
        created == obj.id
        super(ExampleOneViewSet, self).pre_save(obj, created)



## Permissions
# We can assign a more specific set of permissions than just role based permissions on a view set.
# Adding a permission_classes property to the view set allows us to specify any number of classes
# that can help determine if a user should be able to make a certain request.
from rest_framework.permissions import BasePermission
from rest_framework.mixins import mixins as rf_mixins
from libs import viewset_mixins as mm_mixins

class ExampleTwoPermission(BasePermission):
    def has_permission(self, request, view):
        has_permissions = True
        if request.method.lower() == 'get' and not request.user.staff:
            has_permissions = False
        return has_permissions


class ExampleTwoViewSet(rf_mixins.ListModelMixin, mm_mixins.MindMixerViewSet):
    model = ExampleTwo
    queryset = model.objects.all()
    # We can add a tuple of permissions classes where each permission class defines a has_permission
    # method that returns a boolean value of if the request should be allowed. One returned false
    # value fails the request.
    permission_classes = (
        ExampleTwoPermission,
        ResourcePermissions,
    )



## Exceptions
# We can define custom exceptions by inheriting from APIException and specifying a status code and
# optionally a default detail. Alternatively we can use many of the default status errors and 
# exceptions provided by Django/DRF.
from rest_framework.exceptions import APIException
from rest_framework.response import Response

# We can create custom exceptions by inheriting from APIException and defining several properties,
# status_code and optionally default_detail. When creating an instance of the exception we can 
# pass in something to replace the default detail.
class UhOh(APIException):
    status_code = 503
    default_detail = "Ruh Ro, we aren't sure what happened, #classic"


class ExampleThreeViewSet(rf_mixins.ListModelMixin, mm_mixins.CreateModelMixin,
                          mm_mixins.MindMixerViewSet):
    model = ExampleThree
    queryset = model.objects.all()

    # Override the create method to check if the requesting user has exceeded or met their checkout
    # limit, if so raise an UhOh exception. If they had not exceeded the limit, continue creating
    # by calling super on create (default behavior)
    def list(self, request):
        if (request.user.checkouts.count() >= request.user.checkout_limit) {
            raise UhOh('Custom detail')
        }
        super(ExampleOneViewSet, self).list(request)



## Throttling
# Reading through their documentation should be a good introduction to it. We do not currently have
# any instance in our product where we throttle any requests. Knowing that you can set a limit
# or a rate is good to know for the future when this becomes something we may actually use in house.