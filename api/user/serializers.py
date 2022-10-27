from api.user.models import Followers, User
import uuid
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['type', 'id', 'url', 'host', 'displayName', 'github', 'profileImage']
        read_only_field = ['is_active', 'created', 'updated']
