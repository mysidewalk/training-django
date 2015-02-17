from django.db import models

from libs import mm_fields
from libs.model_mixins import audit


class Member(audit.FullAuditMixin, audit.DeletionMixin):
    _format = u'{} - name: {}, checkout_limit: {}'

    id = mm_fields.BigAutoField(primary_key=True)
    name = models.CharField(max_length=mm_fields.SHORT_CHAR_LEN)
    checkout_limit = models.IntegerField(default=3)

    def __unicode__(self):
        return self._format.format(
            self.id,
            self.name,
            self.checkout_limit,
        )


class Book(audit.CreationAuditMixin, audit.DeletionMixin):
    _format = u'{} - title: {}, author: {}, genre: {}'

    id = mm_fields.BigAutoField(primary_key=True)
    title = models.CharField(max_length=mm_fields.LONG_CHAR_LEN)
    author = models.CharField(max_length=mm_fields.SHORT_CHAR_LEN)
    genre = models.CharField(max_length=mm_fields.SHORT_CHAR_LEN)

    def __unicode__(self):
        return self._format.format(
            self.id,
            self.title,
            self.author,
            self.genre,
        )


class Checkout(audit.FullAuditMixin, audit.DeletionMixin):
    _format = u'{} - book: {}, member: {}, return_by: {}, returned: {}'

    id = mm_fields.BigAutoField(primary_key=True)
    book = mm_fields.BigForeignKey('library.Book', related_name='checkouts')
    member = mm_fields.BigForeignKey('library.Member', related_name='checkouts')
    return_by = models.DateTimeField()
    returned = models.BooleanField(default=False)

    def __unicode__(self):
        return _format.format(
            self.id,
            self.book,
            self.member,
            self.return_by,
            self.returned,
        )