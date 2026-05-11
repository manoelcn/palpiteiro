from django.db import models
from accounts.models import CustomUser
import secrets
import string


class Group(models.Model):
    name = models.CharField(max_length=100)
    invite_code = models.CharField(unique=True, max_length=5)
    owner = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='owned_groups')
    matches = models.ManyToManyField('matches.Match', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def generate_code(size=5):
        characters = string.ascii_lowercase + string.digits
        code = ''.join(secrets.choice(characters) for _ in range(size))
        return code

    def save(self, *args, **kwargs):
        if not self.invite_code:
            self.invite_code = self.generate_code()
        return super().save(*args, **kwargs)


class Membership(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='memberships')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='memberships')
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('group', 'user',)
