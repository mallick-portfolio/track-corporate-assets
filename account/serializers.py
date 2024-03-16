from rest_framework import serializers
from account.models import CustomUser
from django.contrib.auth.password_validation import validate_password


# user serializer
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUser
    fields = ['id', 'first_name', 'last_name', 'phone', 'email', 'user_type']


# registration serializer
class RegistrationSerializer(serializers.ModelSerializer):
  password2 = serializers.CharField(style={"input_type": 'password'}, write_only=True)
  class Meta:
    model = CustomUser
    fields = ['email', 'first_name', 'last_name', 'password', 'password2',]
    extra_kwargs = {
        'password': {'write_only': True}
    }

  def save(self):
    email = self.validated_data['email']
    first_name = self.validated_data['first_name']
    last_name = self.validated_data['last_name']
    password = self.validated_data['password']
    password2 = self.validated_data['password2']
    user = CustomUser(email=email, first_name=first_name, last_name=last_name)

    if password != password2:
      raise serializers.ValidationError({'password': 'Passwords must match.'})
    user.set_password(password)
    user.save()
    return user