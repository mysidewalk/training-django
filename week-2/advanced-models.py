## Field Choices
# Yesterday we created several models including the Book model which had a Char field "genre".
# While a free form "genre" field is great, it would be more helpful to specifically categorize
# books by genre, which would require a consistent set.
from django.db import models

from libs import fields as mm_fields
from libs.model_mixins import audit

# This should be really similar to what you ended up with yesterday for the book model based on the
# exercise. We are going to modify down below this one.
class BookOne(audit.CreationAuditMixin, audit.DeletionMixin):
    _format = u'{} - title: {}, author: {}, genre: {}'

    id = mm_fields.BigAutoField(primary_key=True)
    title = models.CharField(max_length=mm_fields.LONG_CHAR_LEN)
    author = models.CharField(max_length=mm_fields.SHORT_CHAR_LEN)
    # The CharField has a couple arguments we can add to let us restrict the options available
    genre = models.CharField(max_length=mm_fields.SHORT_CHAR_LEN)

    def __unicode__(self):
        return self._format.format(
            self.id,
            self.title,
            self.author,
            self.genre,
        )

# We can make a generic class that has all of the choices we want by creating properties
# for each one and then a list of all properties that includes all of them, the name choices is not
# important, but whatever we call the collection is what must be referenced down below in the 
# BookTwo model.
class Genres(object):
    MYSTERY = 'Mystery'
    SCIENCE = 'Science'
    HISTORY = 'History'
    HUMOR = 'Humor'

    choices = (
        (MYSTERY, 'Mystery'),
        (SCIENCE, 'Science'),
        (HISTORY, 'History'),
        (HUMOR, 'Humor'),
    )


# Here we have updated the book model's genre field to include some new things that use the Genres
# class we created above. Within Django's admin screen, this will appear as a select drop down.
class BookTwo(audit.CreationAuditMixin, audit.DeletionMixin):
    _format = u'{} - title: {}, author: {}, genre: {}'

    id = mm_fields.BigAutoField(primary_key=True)
    title = models.CharField(max_length=mm_fields.LONG_CHAR_LEN)
    author = models.CharField(max_length=mm_fields.SHORT_CHAR_LEN)
    # We can add a "choices" keyword and reference the choices list on the Genres class
    # This will limit the options a book can use to the list from above
    genre = models.CharField(max_length=mm_fields.SHORT_CHAR_LEN, choices=Genres.choices)

    def __unicode__(self):
        return self._format.format(
            self.id,
            self.title,
            self.author,
            self.genre,
        )



## ContentTypes
# Yesterday we talked about Foreign Keys and the forward and reverse relationship they create
# between 2 models. Usually 1 model includes a foreign key to the other, which works for many cases.
# For more generic types of content such as tags, comments, or likes, it is unnecessary to create
# a unique model for each "type" of relationship. For example the difference between "liking" an
# organization versus a context is just which model it references.

# Django provides us the contenttypes framework to help us solve problems that situations like the
# above can create. Django's contenttypes framework let's us create models with 3 attributes, two
# are more standard fields, one is a placeholder that ends up housing the content we are after.
# Below is an example of how we would use that framework.
class GenericModelOne(models.Model):
    # By default we can use a content_type field which can use a normal BigForeignKey to that table which
    # has a row created for every model in the whole group of apps.
    content_type = mm_fields.BigForeignKey('django.contenttypes')
    # we can include a BigIntegerField which holds the same information a Foreign Key does,
    # (the ID or primary key to the other table), not a foreign key because it is not a specific
    # type of object
    object_id = models.BigIntegerField()


# You can see we have 1 reference to the type of content and another to the id of the content.
# Together we know what kind and which one of a content type to go get.

# Although we do not currently support serializing the last field (content_object), Django allows 
# you to carry that object on the model.

# A model with all of the content types fields looks like this:
class GenericModelTwo(models.Model):
    content_type = mm_fields.BigForeignKey('django.contenttypes')
    object_id = models.BigIntegerField()
    content_object = generic.GenericForeignKey()



## Q Objects
# The Q object gives us access to more powerful query sets. We can create more powerful conditions
# based and/or. For instance, we could search for a book with that matches the "mystery" genre or 
# is by a specific author.

Books.objects.filter(
    # Here we are checking for books with the author of me or the title that matches that below.
    Q(author="Peter Freeze") | Q(title="Funny Things I Say")
)

# We could do a more complex match based on the inclusion of two things
Books.objects.filter(
    # We can make sure the author field now contains more than one specific thing
    Q(author__icontains="pet") & Q(author__icontains="eze"),
    genre="History"
)

# There are some pretty complex queries using the Q object in the "ContestSummaryFilterBackend" in
# the election view sets. 



## F Objects
# F objects let us manipulate the current object based on a current property without having to 
# retrieve the value from the database.

# If we have a group of articles, we can assign the first one to be featured only if it has been
# published, without having to go and get the item first. The only thing this set of statements does
# is assignment, rather than retrieval.


article = Article.objects.filter(published=True).first()
article.featured = F('published')
article.save()

# As the documentation notes, the current instance of this article will not reflect the updated
# value because it never retrieved the updated version. Everything was telling the database what
# to do rather than bringing it back into your shell or script.

# Here we have an updated version that would reflect the new value for featured
article = Article.objects.get(pk=article.id)

# Another way you can use the F Object is to combine the above statements. On the group of objects,
# we have selected the first one, and updated it to use the value of the current objects published
# value for the featured.
Article.objects
    .first()
    .update(
        featured=F('published')
    )

# We could also have created a slug in a statement that wouldn't even need a iterative loop by using
# a similar syntax:
Article.objects.all()
    .update(
        slug=F('title').slugify()
    )