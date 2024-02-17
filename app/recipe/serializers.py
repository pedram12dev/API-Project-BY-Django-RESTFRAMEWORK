"""serializers for recipe api"""

from rest_framework import serializers
from core.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """serializer for recipe"""

    class Meta:
        model = Recipe
        fields = ('id','title','time_minutes','price','link')
        read_only_fields = ('id',)


class RecipeDetailSerializer(serializers.ModelSerializer):
    """ serializer for recipe detail"""

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ('description',)