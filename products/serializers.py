from rest_framework import serializers
from .models import User, AccessStudents, Group, Lesson, Product


class LessonSerializer(serializers.ModelSerializer):
    """
        Сериализатор для счета уроков в продукте
    """
    class Meta:
        model = Lesson
        fields = ("name",)


class ProductLessonSerializer(serializers.ModelSerializer):
    """
        Сериализатор для вывода списка уроков
                    определенного продукта
    """
    class Meta:
        model = Lesson
        fields = "__all__"


class ProductListSerializer(serializers.ModelSerializer):
    """
        Сериализатор для вывода списка продуктов
    """
    lessons_count = serializers.SerializerMethodField()
    student_count = serializers.SerializerMethodField()
    group_fill_percentage = serializers.SerializerMethodField()
    purchase_percentage = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "author",
            "date_start",
            "price",
            "lessons_count",
            "student_count",
            "group_fill_percentage",
            "purchase_percentage",
        )

    def get_lessons_count(self, obj):
        return obj.lesson_set.count()

    def get_student_count(self, obj):
        return obj.access_students.count()

    def get_purchase_percentage(self, obj):
        total_users_count = User.objects.count()
        access_count = AccessStudents.objects.filter(product=obj).count()
        if total_users_count == 0:
            return 0
        purchase_percentage = (access_count / total_users_count) * 100
        return round(purchase_percentage, 2)

    def get_group_fill_percentage(self, obj):
        max_users = obj.max_users
        if max_users is None:
            return 0
        groups = Group.objects.filter(product=obj)
        if not groups.exists():
            return 0
        total_users = sum(group.user.count() for group in groups)
        sum_users = total_users / groups.count()

        fill_percentage = (sum_users / max_users) * 100
        return round(fill_percentage, 2)


class AccessSerializer(serializers.ModelSerializer):
    """
        Сериализатор для доступов пользователей
    """
    class Meta:
        model = AccessStudents
        fields = ["id", "product", "user", "check_access"]

    def validate(self, attrs):
        product = attrs.get("product")
        user = attrs.get("user")
        if not Product.objects.filter(pk=product.pk).exists():
            raise serializers.ValidationError("Выбранный продукт не существует")
        if not User.objects.filter(pk=user.pk).exists():
            raise serializers.ValidationError("Указанный пользователь не существует")

        return attrs


class GroupSerializer(serializers.ModelSerializer):
    """
        Сериализатор для групп
    """
    class Meta:
        model = Group
        fields = "__all__"
