## Django Migrations

### Preparation
- [Migrations](https://docs.djangoproject.com/en/1.7/topics/migrations/)
- [Migration Operations](https://docs.djangoproject.com/en/1.7/ref/migration-operations/)

### Exercise
For the library app we have been building:

(I would consider it totally acceptable to revert the changes to the checkout model of book FK ->
    content types fields for simplicity, not required though)

- Create an initial migration for the 3 models in the library app
- Write a set of migrations that converts the `returned` field into a `returned at` field, keep in 
    mind that you should update any checkout that has `returned=True`
- Using the shell create at least one object for each model in your database

#### Links
Next: [Queries and Django Models: Part 2](../04-queries-and-models/queries-and-models.md)