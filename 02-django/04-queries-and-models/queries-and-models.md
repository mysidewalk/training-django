## Queries and Advanced Django ORM

### Preparation
- [Q & F](https://docs.djangoproject.com/en/1.7/ref/models/queries/)
- [Performance](http://www.yilmazhuseyin.com/blog/dev/django-orm-performance-tips-part-1/)
- [Performance 2](http://www.yilmazhuseyin.com/blog/dev/django-orm-performance-tips-part-2/)
- [Advanced Models](http://www.djangobook.com/en/2.0/chapter10.html)
- [Aggregation](https://docs.djangoproject.com/en/dev/topics/db/aggregation/)
- [Content Types](https://docs.djangoproject.com/en/1.7/ref/contrib/contenttypes/)

### Exercise
Use the [advanced-models.py](advanced-models.py) file as a reference.
Building on the previous day's library app, complete the following:

- Write a query that checks how many books a Member currently has checked out.
- Using a Q object check how many books a Member has checked out under the genre "history" or "science".
- Update the Checkout model to use a content type field instead of the book foreign key
    (include the content_type and object_id fields)

#### Links
Next: [Introduction to Django REST Framework](../../03-django-rest-framework/01-introduction/introduction.md)