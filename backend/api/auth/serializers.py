from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from apps.accounts.models import CustomUser


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        # validators=[validate_password]
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
    )

    class Meta:
        model = CustomUser
        fields = [
            'id',
            'email',
            'username',
            'password',
            'password2'
        ]

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {
                    "password": "Password fields didn't match."
                }
            )
        return attrs