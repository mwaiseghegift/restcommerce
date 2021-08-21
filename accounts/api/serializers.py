from rest_framework import serializers
from accounts.models import CustomUser


class RegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input-type':'password'}, write_only=True)
    class Meta:
        model = CustomUser
        fields = ['email', 'username','password','password2']

        extra_kwargs = {
            'password':{'write_only':True}
        }

        def save(self):
            user = CustomUser(
                email = self.validated_data['email'],
                username = self.validated_data['username'],
            )
            password = self.validated_data['password']
            password2 = self.validate_data['password2']

            if password != password2:
                raise serializers.ValidationError({'password':'password must match'})
            user.set_password(password)
            user.save()
            return user