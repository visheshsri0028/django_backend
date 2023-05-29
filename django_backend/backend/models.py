from django.db import models
from django.utils.encoding import force_str
from django.utils.html import mark_safe
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from . import utils
@python_2_unicode_compatible
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    phone_number = models.CharField(_('number'), max_length=20, blank=True)
    address = models.CharField(_('address'), max_length=200, blank=True)
    def __str__(self):
        return self.user.username
    def get_absolute_url(self):
        return reverse('profile', kwargs={'username': self.user.username})
    def get_full_name(self):
        return self.user.get_full_name()
    def get_short_name(self):
        return self.user.get_short_name()
    def profile_image_tag(self):
        return mark_safe('<img src="%s" class="img-circle" width="50" height="50" />' % (self.image.url))
    def profile_image_url(self):
        return self.image.url
    def profile_image_url_https(self):
        return self.image.url
    def profile_image_url_http(self):
        return self.image.url
    def profile_image_url_https_absolute(self):
        return self.image.url

