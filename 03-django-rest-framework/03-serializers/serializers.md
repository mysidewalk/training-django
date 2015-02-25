## Serializers, Renderers, and Parsers

### Preparation
- [JSON API](http://jsonapi.org/)
- [Serializers](http://www.django-rest-framework.org/api-guide/serializers/)
- [Renderers](http://www.django-rest-framework.org/api-guide/renderers/)
- [Parsers](http://www.django-rest-framework.org/api-guide/parsers/)

### Exercise
For the library app:

1. Add the `DynamicModelSerializer` to the books view set and include the `created_by` and
    `checkouts` fields with the API response
2. Add the `SerializerOptions` to the checkout view set and by default include both book and member

#### Links
Next: [Exceptions and Permissions](../04-exceptions/exceptions.md)