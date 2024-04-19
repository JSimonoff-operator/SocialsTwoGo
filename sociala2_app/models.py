from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class SocialAccount(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    specific_username = models.CharField(max_length=200, default=1)
    profile_pic = models.ImageField(null=True, blank=True)
    friend_code = models.CharField(max_length=30, default=1)
    private_code = models.CharField(max_length=8, default=11111111, blank=True)
    description = models.TextField(max_length=200, blank=True)
    PURPOSE = (
            ('FOR FUN', 'This account exists for fun'),
            ('FOR BUSINESS', 'This account exists for business reasons'),
            ('FOR PERSONAL USE', 'This account exists for personal usage'),
            ('FOR ART', 'This account exists for sharing art'),
            ('FOR INFLUENCE', 'This account exists for influencer purposes'),
            ('OTHER', 'This account exists for other reasons')
            )
    PLATFORMS = (
             ('TWITTER', 'Twitter'),
             ('FACEBOOK', 'Facebook'),
             ('YOUTUBE', 'Youtube'),
             ('INSTAGRAM', 'Instagram'),
             ('STEAM', 'Steam'),
             ('DISCORD', 'Discord'),
             ('OTHER', 'Another account')
            )
    # Determines if the accounts are public or private
    is_public = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.specific_username
    def get_absolute_url(self):
        return reverse('social-detail', args=[str(self.id)])
    purpose = models.CharField(max_length=200, choices=PURPOSE, blank=True)
    platform = models.CharField(max_length=200, choices=PLATFORMS, blank=False, default='NULL')

