from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'




from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):

	password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

	class Meta:
		model = User
		fields = ['email', 'username', 'password', 'password2', 'first_name', 'last_name',]
		extra_kwargs = {
				'password': {'write_only': True},
		}	


	def	save(self):

		user = User(
					email=self.validated_data['email'],
					username=self.validated_data['username']
				)
		password = self.validated_data['password']
		password2 = self.validated_data['password2']
		if password != password2:
			raise serializers.ValidationError({'password': 'Passwords must match.'})
		user.set_password(password)
		user.save()
		return user


class UserPropertiesSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = '__all__'
		# fields = ['pk', 'email', 'username', 'first_name', 'last_name', 'user_permissions']



class ChangePasswordSerializer(serializers.Serializer):

	old_password = serializers.CharField(required=True)
	new_password = serializers.CharField(required=True)
	confirm_new_password = serializers.CharField(required=True)

