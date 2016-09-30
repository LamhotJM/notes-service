from __future__ import unicode_literals
from django.db import models

import datetime


class MasterComment(models.Model):
    commentid = models.IntegerField(primary_key=True)
    userid = models.CharField(blank=True, null=True, max_length=100)
    loanid = models.CharField(blank=True, null=True, max_length=100)
    comment = models.CharField(blank=True, null=True, max_length=225)
    file_upload = models.CharField(null=True, max_length=254, editable=True)
    context_id = models.IntegerField(blank=True)
    context_scope = models.CharField(blank=True, null=True, max_length=400)
    status = models.IntegerField(blank=True)
    createdby = models.CharField(blank=True, null=True, max_length=25)
    createdfrom = models.CharField(blank=True, null=True, max_length=60)
    createddate = models.DateTimeField(editable=False)
    modifiedby = models.CharField(blank=True, null=True, max_length=25)
    modifiedfrom = models.CharField(blank=False, null=True, max_length=60)
    modifieddate = models.DateTimeField(editable=True, null=True)

    def __unicode__(self):
        return self.commentid

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.commentid:
            self.createddate = datetime.datetime.today()
        self.createddate = datetime.datetime.today()
        self.modifieddate = datetime.datetime.today()
        return super(MasterComment, self).save(*args, **kwargs)

    class Meta:
        managed = True
        db_table = 'comments'
