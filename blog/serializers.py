from rest_framework import serializers
from .models import (
    Category,
    Post,
)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]

class PostSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField()
    class Meta:
        model = Post
        fields = ["id", "title", "content", "category_id", "status", "created_date"]