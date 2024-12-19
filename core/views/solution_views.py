from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from ..models import Solution
from ..serializers import SolutionSerializer

class SolutionViewSet(viewsets.ModelViewSet):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer
    permission_classes = [AllowAny]  

    def perform_create(self, serializer):
        # Automatically assign the authenticated user to the solution
        serializer.save(user=self.request.user)
