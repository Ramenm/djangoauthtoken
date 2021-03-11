from django.contrib.auth.models import User
from rest_framework import serializers


class ReadOnlyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "is_active", "last_login", "is_superuser")


class WriteOnlyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "password", "is_active")

    password = serializers.RegexField(min_length=1, max_length=128, regex="^(?=.*[A-Z])(?=.*\d).{8,}$", error_messages={
        "invalid": "at least 8 chars with digit and uppercase"})  # error_messages={"password":"at least 8 chars with digit and uppercase"}
