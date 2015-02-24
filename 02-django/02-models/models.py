## Models
# Standard models in Django are class based that all inherit from Django's base "Model" class. The
# very basic style of class should inherit in some way, directly or indirectly from the base class.
from django.db import models

# The name of the model is what our object/resource will be called, should be a noun. Our class
# can inherit from other mixins, noted below.
class ModelOne(models.Model):
    # To add fields to a model we add properties of a certain type to this class
    # We can define several methods and serialize them as properties for more complex items
    pass

    class Meta(object):
        # The Meta subclass allows us to set up more high level settings on our model that can
        # manipulate how it is stored or even if it is stored in the database.
        pass



## Mixins
# We have a handful of model mixins that provide some basic functionality. From the libs, we have a
# model_mixins set. All of the mixins have a couple import attributes; each have their Meta 
# subclass with a property "abstract" set to "True".

# CreationAuditMixin
# This creates two fields, "created_at" is a date time field which represents the date and time that
# an object was created. "created_by" is a foreign key to user, to show who created it.

# ModificationAuditMixin
# "modified_at" and "modified_by", date time and foreign key to user again, but for when a user
# updates the fields.

# DeletionMixin
# "deleted_at" and "deleted_by", date time and foreign key to user. Happens on a delete request.
from libs.model_mixins.audit import CreationAuditMixin, ModificationAuditMixin, DeletionMixin

# FullAuditMixin
# Despite what its name suggests, the FullAuditMixin only provides creation and modification audit
# mixins, and not the DeletionMixin.
from libs.model_mixins.audit import FullAuditMixin

# Across the sidewalk apps you will see models that inherit from some collection of the audit mixins
class ModelTwo(FullAuditMixin, DeletionMixin):
    pass



## Fields
# Fields are how we store information on a model. If models are tables, fields are columns in our 
# database. Django provides plenty of default types of fields, and you can create you own field for
# more custom behavior. (https://docs.djangoproject.com/en/1.7/ref/models/fields/#field-types)
from django.db import models

# Examples of a couple different types of fields and configuring their options using our keyword
# arguments.
class ModelThree(FullAuditMixin):
    # The primary key is the ID column for each model. MindMixer has a custom field named:
    # "BigAutoField" to ensure that the field uses a big int rather than normal int.
    # You can load these by importing "libs.fields"
    id = mm_fields.BigAutoField(primary_key=True)
    # The CharField allows us to create a text field on a model. MindMixer has two constants that
    # help us maintain a consistent length.
    strings = models.CharField(max_length=500)
    # We can create boolean fields with default values.
    visible = models.BooleanField(default=False)
    # MindMixer prefers to use DateTimeFields over generic DateFields for more accuracy. Setting
    # DateTime fields to blank and null equal to True allows us to ensure that dates never get set
    # improperly. There is no good default date. blank, null being set to True should be used 
    # sparingly, but also makes a field not required.
    date_time = models.DateTimeField(blank=True, null=True)



## Methods
# Each one of our models in MindMixer should include an overwritten __unicode__ method which is the
# string representation for not only the "/admin" screen but also for use in the
# interactive terminal. A model can include many other methods
class ModelFour(FullAuditMixin):
    # The string should be a unicode string (prepended with a "u"), and list the important
    # attributes of the model.
    _format = u"{}: strings - {}, visible - {}, date_time - '{}'"

    id = models.AutoField(primary_key=True)
    strings = models.CharField(max_length=500)
    visible = models.BooleanField(default=False)
    date_time = models.DateTimeField(blank=True, null=True)

    # The unicode method should just call a format on the self._format string to populate the fields
    def __unicode__(self):
        return self._format.format(
                self.id,
                self.strings,
                self.visible,
                self.date_time,
            )



## Meta
# The Meta subclass allows us to set some high level properties of a model. There are several 
# view sets that deliver a resource based on a SQL view, which can map to a model like below.
class ModelFive(FullAuditMixin):

    class Meta(object):
        # Abstract allow us to create presets like the CreationAuditMixin which adds two fields, but
        # itself is not unique model / table in the database.
        abstract = False

        # managed = False tells Django to not include this in any migrations, the default value
        # is true.
        managed = False

        # The db_table lets us customize the name of the table for the model, by default the table
        # name follows this convention; "{app}_{model}" where app and model are all lowercase.
        db_table = "view_modelfive"

        # We can create a set of constraints to use in a database preventing a user from creating 
        # multiple of the same records if they haven't been deleted. A comma separated tuple sets
        # the unique_together to make sure nothing is an EXACT match
        unique_together = ("id", "date_time")