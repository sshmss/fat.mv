from django.contrib.auth.models import User
from main.models import Trainer, Member
from django.shortcuts import get_object_or_404
from main.serializers import UserSerializer, TrainerSerializer, MemberSerializer
from rest_framework import viewsets
from rest_framework.response import Response

class UserViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class TrainerViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving trainers.
    """
    def list(self, request):
        queryset = Trainer.objects.all()
        serializer = TrainerSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Trainer.objects.all()
        trainer = get_object_or_404(queryset, pk=pk)
        serializer = TrainerSerializer(trainer)
        return Response(serializer.data)

class MemberViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving members.
    """
    def list(self, request):
        queryset = Member.objects.all()
        serializer = MemberSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Member.objects.all()
        member = get_object_or_404(queryset, pk=pk)
        serializer = MemberSerializer(member)
        return Response(serializer.data)