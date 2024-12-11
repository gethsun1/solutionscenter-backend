from rest_framework import viewsets
from ..models import Solution
from ..serializers import SolutionSerializer

class SolutionViewSet(viewsets.ModelViewSet):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer
