from django.db import models


class TimestampFields(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        abstract = True


class TorrentFile(TimestampFields):
    name = models.CharField(max_length=255)
    uploader = models.CharField(max_length=25)
    location = models.CharField(max_length=255)
    uploadTime = models.DateTimeField(auto_now=False, auto_now_add=True)
    category = models.ForeignKey('MtCategory', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True

    def __str__(self):
        return self.name.title()


class MtCategory(TimestampFields):
    name = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'mt_category'

    def __str__(self):
        return self.name.title()
