from django.urls import path
from . import views

urlpatterns = [
    path("product/", views.ProductAPIView.as_view()),  # Список продуктов
    path("product/access/", views.AccessCreateAPIView.as_view()),  # Получение доступа
    path("product/<int:product_id>/lesson", views.LessonListAPIView.as_view()),  # Список уроков от продукта
    path("check/", views.AccessStudent.as_view()),  # Одобрение или проверка пользователей
    path("group/", views.GroupAPIView.as_view()),   # Список групп
]
