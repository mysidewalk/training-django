## Serializing - What it does
# Our serialization occurs in a multi-step process. THe first of which is converting every field
# and object into a primitive type that is acceptable in JSON. Those types include, but are not
# limited to: lists, dictionaries, booleans, strings, integers, floats, dates and datetimes.

# Serialization also keeps things as ordered dictionaries because order does matter. It ensures that
# our sorting/ordering of an API maintains itself as it goes through this process.

# The second piece here is converting Python's snake case property names into JavaScript's
# camelCase. And lastly, the whole thing is then converted into JSON before being included in an
# http response



## Old Style - Setting a "serializer_class" on the view set
# What I'll refer to as "old style" serialization is how many of our view sets have implemented 
# their serialization as of February 2015. The strategy here is to specify a queryset that has been
# optimized by hand (by specifying the select/prefetch related objects) as well as what goes in the
# object graph as far as fields and objects.

# This is done with the DynamicModelSerializerFactory. In almost every instance we use the default
# method, and specify the model and include_objects.

# Old style serialization of a view set exemplified tomorrow

from rest_framework import mixins as rf_mixins, viewsets as rf_viewsets
from libs import viewset_mixins as mm_mixins
from libs.serializers.dynamicmodel import DynamicModelSerializerFactory

class ExampleOneViewSet(rf_mixins.ListModelMixin, rf_viewsets.GenericViewSet):
    model = ExampleOne

    # The DynamicModelSerializer is in the libs. At a minimum we need to specify a model to use.
    # Additionally we can specify other objects that are related to that model to include, these 
    # are properties related to the model through forward or reverse relations (Checkout having a 
    # book vs. a book having checkouts)
    serializer_class = DynamicModelSerializerFactory.default(
        model=model,
        include_objects=[
            # An example would be for Comments to include the created_by and the avatar of the
            # the created_by
            'created_by.avatar',
        ]
    )

    # Previously we saw that at a bare minimum we need to add a queryset property on a view set.
    # What we should also be doing to increase efficiency is specify any included objects so they
    # are selected on the first DB pass rather then on subsequent ones.

    # When defining the queryset we should add a "select_related()" if we are including objects
    # from a forward relationship, (include the object from a foreign key rather than just the
    # primary key value. We should include "prefetch_related()" if we are including objects from
    # a backward relationship, (when another model specifies the current model with a foreign key
    # and gives it a related_name="")
    queryset = model.objects.all()\
        # Add forward relational objects here
        .select_related(
            'created_by__avatar',
        )\
        # Add backward relational objects here
        .prefetch_related(
            ''
        )



## New Style - Setting "serializer_options" on the view set
# This idea of new style serialization has many upsides including: not needing to specify the object
# graph in two places on a view set, no needing to specify a queryset and therefore its
# forward/reverse relations, and lastly, we can dynamically include additional fields or objects
# in the API request

from rest_framework import mixins as rf_mixins, viewsets as rf_viewsets
from libs import viewset_mixins as mm_mixins
from libs.serializers.dynamicmodel import SerializerOptions

# We need to inherit from MindMixerViewSet to rely on some pieces of functionality that are paired
# with the serializer options
class ExampleTwoViewSet(rf_mixins.ListModelMixin, mm_mixins.MindMixerViewSet):
    # Need to include the model on the view set, but not the queryset
    model = ExampleTwo

    # Rather then specifying a queryset, serializer, or serializer_class, we only need to specify
    # a serializer_options property on the view set. It most importantly takes 1 argument,
    # include_objects, and model it grabs from the view, so we will need to make sure we include
    # it in the view set as well
    serializer_options = SerializerOptions(
        # Specifying objects here will include them in all requests, specifying a "include" query
        # param will replace the existing specified ones here.
        include_objects=[
            'created_by.avatar',
        ],
    )



## JSON API
# According the spec, a JSON API response must have a top level JSON object, with a collection of
# data resources, or error attributes. Each resource object should have a type and id property.

# The dictionary of how objects should be nested and related is stored in the "links" property of 
# the top level, the "linked" object the unique objects that are not the primary resource stored
# by type.

# Our JSON API deserializer then moves to match the linked objects to the primary resource based
# on the definition provided in the links section. We use ID's to match objects and types to 
# indicate what resource it is. Each item also includes a "href" property which links to that unique
# object in the API. 