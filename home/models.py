# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Balcao(models.Model):

    #__Balcao_FIELDS__
    codigo = models.CharField(max_length=255, null=True, blank=True)
    descricao = models.CharField(max_length=255, null=True, blank=True)

    #__Balcao_FIELDS__END

    class Meta:
        verbose_name        = _("Balcao")
        verbose_name_plural = _("Balcao")


class Tipo_Item(models.Model):

    #__Tipo_Item_FIELDS__
    codigo = models.CharField(max_length=255, null=True, blank=True)
    descricao = models.CharField(max_length=255, null=True, blank=True)

    #__Tipo_Item_FIELDS__END

    class Meta:
        verbose_name        = _("Tipo_Item")
        verbose_name_plural = _("Tipo_Item")


class Subtipo_Item(models.Model):

    #__Subtipo_Item_FIELDS__
    codigo = models.CharField(max_length=255, null=True, blank=True)
    descricao = models.CharField(max_length=255, null=True, blank=True)
    fk_tipo_item = models.IntegerField(null=True, blank=True)

    #__Subtipo_Item_FIELDS__END

    class Meta:
        verbose_name        = _("Subtipo_Item")
        verbose_name_plural = _("Subtipo_Item")



#__MODELS__END
