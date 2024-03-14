from rest_framework import serializers

from fardaapp.models import User


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "phone",
            "email",
            "national_code",
            "birth_date",
            "father_name",
            "first_name",
            "last_name",
            "skills",
            "network",
        )
