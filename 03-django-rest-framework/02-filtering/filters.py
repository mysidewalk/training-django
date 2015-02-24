## Filter Query Sets
# We can create two different methods that help us filter a queryset; "get_queryset()" and 
# "filter_queryset()". We use "filter_queryset()" way more frequently then the "get_queryset()".
# We do this because, we do not frequently modify the default queryset based on a piece of
# information from the request, we do however modify a request based on explicit filters passed in.

# We can take a look at the two methods below:
from rest_framework import mixins as rf_mixins
from libs import viewset_mixins as mm_mixins


class ExampleOneViewSet(rf_mixins.ListModelMixin, rf_mixins.CreateModelMixin,
                        rf_mixins.GenericViewSet):
    # We can specify the model for this resource
    model = ExampleOne
    # We should define the starting queryset for every viewset
    queryset = model.objects.all()

    # We could by default filter the queryset so that you could only see checkouts for the member
    # (user) that made the request or prevent checkouts that have been returned from being included
    def get_queryset(self):
        return self.queryset

    # A filter_queryset works as a great one-off way to filter a endpoint, for something that is 
    # more generic or reusable, it makes more sense to be created as a filter backend (below).
    # IMPORTANT NOTE: You cannot user a "filter_queryset()" method AND "filter_backends", you are 
    # almost guaranteed to run into this. You should probably use "filter_backends" by default.
    def filter_queryset(self, request, queryset, view):
        # Do some filter stuff before returning the queryset
        return queryset



## Filter Backends
# Filter backends let us create a custom "filter_queryset()" method, in the same way the
# "filter_queryset()" method lets us from the view set. The difference being we can list multiple
# filter backends on a single view set which then run in order.

# A filter backend is a class that inherits directly or indirectly from BaseFilterBackend. The
# filter backend can use the "filter_queryset()" method including the 4 standard arguments. It is 
# important that every filter backend return a queryset

# We could create a filter backend that prevents members from seeing checkouts of other members
# unless they were marked as "staff".
from rest_framework import filters
from libs.parsers import parameters


class ExampleTwoFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        # Using the internal parameter parsing, we can transform things in the QUERY_PARAMS
        # dictionary into more specific values, like a boolean, geometry, list, etc.
        qs_parser = parameters.ParseConfiguration()
        params = qs_parser.parse_to_dict(request.QUERY_PARAMS)

        # If the request did not specify a member, and the requesting user is not a staff member
        # filter the queryset to match only the requesting user
        if not params['member'] and not request.user.staff:
            queryset = queryset.filter(member=request.user)

        return queryset


class OtherFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        # Do some random filtering here
        return queryset


class ExampleTwoViewSet(rf_mixins.ListModelMixin, rf_mixins.GenericViewSet):
    model = ExampleTwo
    # We can specify the list of filter_backends here, and note that they do execute in the order we
    # have included them by. So ExampleTwoFilterBackend will filter it before OtherFilterBackend
    filter_backends = (
        ExampleTwoFilterBackend,
        OtherFilterBackend,
    )



## Ordering
# We can change the default ordering of any resource to be by any property. MindMixer has created a 
# class that any viewset can use in its filter_backends list to allow/modify ordering. It allows
# you to specify something other then the defaults at the view level.

# The defaults for the MindMixerSortBackend listed at the top of the class in
# libs.filter_backends.MindMixerSortBackend.
class ExampleThreeViewSet(rf_mixins.ListModelMixin, rf_mixins.GenericViewSet):
    model = ExampleThree
    filter_backends = (
        MindMixerSortBackend,
    )
    # We can also update the default ordering if no specific sort is specified in the request body 
    # or query params. (Adding a negative inverts the search).
    ordering = '-id'
    # We have updated the MindMixerSortBackend to accept ordering by the id or name properties of 
    # the model. It will sort/order by default unless something is specified in the request
    ordering_fields = (
        'id',
        'name',
    )



## Pagination
# We require almost all API read requests to use pagination to prevent easy scrapping of our API.
# Any viewset inheriting from the MindMixerViewSet mixin has it's requests paginated by 10 items 
# per page. The MindMixerViewSet also sets the param that allows any request to change the page 
# size. The param by default is "items_per_page".
class ExampleFourViewSet(rf_mixins.ListModelMixin, mm_mixins.MindMixerViewSet):
    model = ExampleFour
    # Boom, it was that easy



## Searching
# We can expose search functionality for the API by leveraging DRF's built in SearchFilter and
# specifying which fields we would like to search within.
from rest_framework import filters


class ExampleFiveViewSet(rf_mixins.ListModelMixin, mm_mixins.MindMixerViewSet):
    model = ExampleFive
    # You will need to include the DRF SearchFilter in order to allow searching via the key 'search'
    filter_backends = (
        filters.SearchFilter,
    )
    # We can set the fields which search is allowed on by including the following list, we could
    # even extend our reach into a object.
    search_fields = (
        'name',
        'description',
        'created_by__first_name'
    )