from rest_framework import viewsets, permissions
from django.shortcuts import render
from .models import (
    Profile,
    Project,
    CertifyingInstitution,
    Certificate
    )
from .serializers import (
    ProfileSerializer,
    ProjectSerializer,
    CertifyingInstitutionSerializer,
    CertificateSerializer
    )


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def retrieve(self, request, *args, **kwargs):
        if request.method == 'GET':
            # Dessa forma abaixo, não está encontrando os certificados dos
            # perfis
            # instance = self.get_object()
            # serializer = self.get_serializer(instance)
            profile_id = kwargs.get('pk')
            profile = Profile.objects.get(pk=profile_id)
            return render(
                request,
                "profile_detail.html",
                {"profile": profile}
                )
        return super().retrieve(request, *args, **kwargs)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class CertifyingInstitutionViewSet(viewsets.ModelViewSet):
    queryset = CertifyingInstitution.objects.all()
    serializer_class = CertifyingInstitutionSerializer


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
