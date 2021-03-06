## Basic Django ORM

### Preparation
- [Models](https://docs.djangoproject.com/en/1.7/topics/db/models/)
- [Fields](https://docs.djangoproject.com/en/1.7/ref/models/fields/)
- [Queries](https://docs.djangoproject.com/en/1.7/topics/db/queries/)
- [Effective ORM](http://effectivedjango.com/orm.html)

### Exercise
Create a new Django app called "library", with 3 models: Member, Book, and, Checkout.

- The Member model should have 3 fields:
    - ID (Primary key)
    - Name (Char)
    - Checkout limit (Int)
- The Book model should have 4 fields:
    - ID (Primary key)
    - Title (Char)
    - Author (Char)
    - Genre (Char)
- The Checkout model should have 5 fields:
    - ID (Primary key)
    - Book (Foreign key)
    - Member (Foreign key)
    - Return by (Date time)
    - Returned (Boolean)

#### Links
Next: [Django Schema and Data Migrations](../03-migrations/migrations.md)