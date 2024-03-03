from django.db.models import Count
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Product, Lesson, Group, AccessStudents
from .serializers import (
    GroupSerializer,
    AccessSerializer,
    ProductListSerializer,
    ProductLessonSerializer,
)


class ProductAPIView(ListCreateAPIView):
    """
        Предоставляет список всех продуктов
    """
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class AccessStudent(ListCreateAPIView):
    """
        Предоставляет одобрение и проверку доступов пользователей
    """
    queryset = AccessStudents.objects.all()
    serializer_class = AccessSerializer


class AccessCreateAPIView(generics.CreateAPIView):
    """
        Предоставляет доступ к пользователям и создание групп для продуктов
    """
    queryset = AccessStudents.objects.all()
    serializer_class = AccessSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        access_instance = serializer.save()

        product = access_instance.product
        user = access_instance.user

        active_groups = Group.objects.filter(
            product=product, start_datetime__lte=timezone.now()
        )

        if active_groups.exists():
            group = (
                active_groups.annotate(num_users=Count("user"))
                .order_by("num_users")
                .first()
            )
            max_users = product.max_users
            if group.num_users < max_users:
                group.user.add(user)
            elif active_groups.last().num_users() - group.num_users > 1:
                group = Group.objects.create(
                    product=product, start_datetime=timezone.now()
                )
                group.user.add(user)
            else:
                group = Group.objects.create(
                    product=product, start_datetime=timezone.now()
                )
                group.user.add(user)
                pass
        else:
            pass
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LessonListAPIView(generics.ListAPIView):
    """
        Предоставляет список уроков от продукта
    """
    queryset = Lesson.objects.all()
    serializer_class = ProductLessonSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        product_id = self.kwargs.get("product_id")
        queryset = Lesson.objects.filter(product_id=product_id)
        return queryset


class GroupAPIView(ListCreateAPIView):
    """
        Предоставляет список групп от продуктов
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
