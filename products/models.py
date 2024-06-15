from django.db import models
from django.utils import timezone


class User(models.Model):
    """
        Абстрактно аутентифицированные пользователи
    """
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Пользователи"
        verbose_name_plural = "Добавить пользователя"

    def __str__(self):
        return self.name


class Product(models.Model):
    """
        Модель для продукта
    """
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    date_start = models.DateTimeField(default=timezone.now(), null=True)
    price = models.PositiveIntegerField()
    min_users = models.PositiveIntegerField(null=True)
    max_users = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name = "Добавить продукт"
        verbose_name_plural = "Создать продукт"

    def __str__(self):
        return self.name


class AccessStudents(models.Model):
    """
        Модель для одобрения доступа или же для изменения
    """
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name="access_students", null=True
    )
    user = models.ForeignKey("User", on_delete=models.CASCADE, null=True)
    check_access = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Новый доступ"
        verbose_name_plural = "Доступы пользователей"

    def __str__(self):
        return f"{self.user.name} - {self.product.name}, {self.check_access}"


class Lesson(models.Model):
    """
        Модель для уроков
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    video = models.URLField()

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "Добавить урок"

    def __str__(self):
        return self.name


class Group(models.Model):
    """
        Модель группы
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, default="default_group")
    user = models.ManyToManyField("User", related_name="groups")
    start_datetime = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = "Добавить группы"
        verbose_name_plural = "Группы"

    def __str__(self):
        return self.name

    def num_users(self):
        return self.user.count()
