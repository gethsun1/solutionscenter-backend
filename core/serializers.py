from rest_framework import serializers
from .models import User, Solution

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'mobile_number']

class SolutionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Solution
        fields = [
            'id',
            'user',
            'solution_type',
            'description',
            'terms',
            'amount_to_charge',
            'amount_willing_to_pay',
            'created_at',
        ]
