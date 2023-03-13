from django.db import models
from django.utils.translation import gettext as _


class ObjectLocations(models.Model):
    name = models.CharField(_('name'), max_length=100)
    activ = models.CharField(_('activ'), max_length=2)
    discShort = models.CharField(_('discShort'), max_length=700)
    discLong = models.CharField(_('discLong'), max_length=1000)
    addres = models.CharField(_('addres'), max_length=100)
    oktmo = models.IntegerField(_('oktmo'), null=True)
    fcp = models.CharField(_('fcp'), max_length=30)
    actions = models.CharField(_('actions'), max_length=50)
    startBuild = models.CharField(_('startBuild'), max_length=50)
    endBuild = models.CharField(_('endBuild'), max_length=50)
    finValue = models.IntegerField(_('finValue'), null=True)
    curator = models.CharField(_('curator'), max_length=100)
    telephone = models.CharField(_('telephone'), max_length=100)
    workHours = models.CharField(_('workHours'), max_length=100)
    email = models.CharField(_('email'), max_length=100)
    siteUrl = models.CharField(_('siteUrl'), max_length=100)
    typeObject = models.CharField(_('typeObject'), max_length=100)
    typeSport = models.CharField(_('typeSport'), max_length=100)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    scaleMap = models.IntegerField(_('scaleMap'), null=True)
    photoUrl = models.CharField(_('photoUrl'), max_length=50)

    def __str__(self):
        return self.name
