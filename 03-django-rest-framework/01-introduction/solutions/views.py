# These includes the solutions to the first and second exercises for creating viewsets

# Importing DRF's mixins and alias them as rf_mixins
from rest_framework import mixins as rf_mixins

# Importing MindMixer's mixins which we use for Create, Modify, and Delete
from libs import viewset_mixins as mm_mixins

# Import the models from this app
from library import models as library_models


# Declare a new ViewSet for Books class by inheriting from GenericViewSet or anything that inherits
# from that. We have included only the ListModelMixin, meaning we have restricted the functionality
# of this API view to only returning a set of Books.
class BookViewSet(rf_mixins.ListModelMixin, rf_mixins.GenericViewSet):
    # At a bare minimum we need to define the model for the ViewSet, which we have done by
    # referencing the imported models
    model = library_models.Book


# This is very similar to the BookViewSet, except that it has more ViewSet mixins, which further
# expand it's functionality. We have included the _MindMixer_ mixins for Create and Modify, and the
# standard DRF ones for List and Retrieve
class CheckoutViewSet(mm_mixins.CreateModelMixin, mm_mixins.ModifyModelMixin,
                      rf_mixins.ListModelMixin, rf_mixins.RetrieveModelMixin,
                      rf_mixins.GenericViewSet):
    # Again specifying our model from the imported models
    model = library_models.Checkout