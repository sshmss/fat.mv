from rest_framework import serializers
from django.contrib.auth.models import User
from main.models import Trainer
from main.models import Member
from main.models import Gym
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}
class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
    

    # def create(self, validated_data):
    #     user = User(
    #         email=validated_data['email'],
    #         username=validated_data['username']
    #     )
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user