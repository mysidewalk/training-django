## Introduction to DRF

### Preparation
- [ViewSets](http://www.django-rest-framework.org/api-guide/viewsets/)
- [Routers](http://www.django-rest-framework.org/api-guide/routers/)
- [Endpoint Correctness](https://docs.google.com/a/mindmixer.com/presentation/d/1bdlV-7HVQaxLgceHDTNwWfNtpj8xm2sPDce9moytahw/edit#slide=id.p)
- [Self documenting](http://localhost:8080/api/v1/engagement)

### Exercises
1. Create a view set for the Book model in the library app
    - Restrict the API to list style requests
2. Create a view set for the Checkout model in the library app
    - Allow the view set to handle list, retrieve, create, and modify requests 
3. Expose the view sets at `/api/library/v1/{plural_model_name}`

#### Links
Next: [Filtering, Ordering, and Searching](../02-filtering/filtering.md)