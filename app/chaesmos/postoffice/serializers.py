from rest_framework.serializers import ModelSerializer

from .models import Letter, Solution


class LetterListSerializer(ModelSerializer):
    class Meta:
        model = Letter
        fields = '__all__'


class SolutionSerializer(ModelSerializer):
    class Meta:
        model = Solution
        fields = '__all__'
