## Exceptions, Permissions

### Preparation
[Exceptions](http://www.django-rest-framework.org/api-guide/exceptions/)
[HTTP Status Codes](http://httpstatus.es/)
[Throttling](http://www.django-rest-framework.org/api-guide/throttling/)
[Permissions](http://www.django-rest-framework.org/api-guide/permissions/)

### Exercise
1. Add permissions to the checkout view set to only allow creating a checkout if the request's
    user matches the specified member
2. Return the HTTP status code 420 for a create checkout request that contains more than the member's
    limit allows
3. Create a custom exception for status code 418
