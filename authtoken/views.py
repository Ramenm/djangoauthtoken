from .serializers import WriteOnlyUserSerializer, ReadOnlyUserSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins, generics
from rest_framework.response import Response


class UserList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = ReadOnlyUserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


    def get_serializer_class(self):
        if self.request.method in ('POST','PUT', 'PATCH'):
            return WriteOnlyUserSerializer
        return ReadOnlyUserSerializer

    def perform_create(self, serializer):
        return serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        instance_serializer = ReadOnlyUserSerializer(instance)
        return Response(instance_serializer.data)




class UserDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = ReadOnlyUserSerializer
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


    def get_serializer_class(self):
        if self.request.method in ('POST','PUT', 'PATCH'):
            return WriteOnlyUserSerializer
        return ReadOnlyUserSerializer


    def perform_update(self, serializer):
        return serializer.save()

    def update(self, request, *args, **kwargs):
        print(request.data)
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
        instance = self.perform_update(serializer)
        instance_serializer = ReadOnlyUserSerializer(instance)
        return Response(instance_serializer.data)

