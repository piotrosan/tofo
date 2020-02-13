from django.db import models

from userprofile.models import Profile


class UserManager(models.Manager):
    def create(self, user_validate_data, profile_validate_data):
        user = self.model(**user_validate_data)
        profile = Profile(**profile_validate_data)
        profile.save()
        user.profile = profile
        user.save()
        return user

    def update(self, instance, validate_data):
        profile = validate_data.pop('profile')
        self.model.objects.filter(id=instance.id).update(**validate_data)
        Profile.objects.filter(id=instance.profile.id).update(**profile)
        return instance
