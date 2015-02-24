from rest_framework import routers

from libs.components.permissions.resources import AppResources

from library.v1 import views as library_views

# Declare version 1 resources for our app 'library'
app_resources = AppResources(1, 'library')
create_resource = app_resources.create_resource

# Define a resource for books using the BookViewSet
app_resources.books = create_resource(
    viewset=library_views.BookViewSet,
)

# Define a resource for books using the CheckoutViewSet
app_resources.checkouts= create_resource(
    viewset=library_views.CheckoutViewSet,
)

# Default router configuration and iteration that occurs at the bottom of each urls.py file
# This handles registering each resource from above with their specified viewset
router = routers.DefaultRouter(trailing_slash=False)
for resource in app_resources.get_resources():
    router.register(resource.noun, resource.viewset)

urlpatterns = router.urls