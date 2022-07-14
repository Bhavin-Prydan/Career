from .models import Candidate
from .serializers import CandidateSerializer
from rest_framework import viewsets

# Create your views here.

class CandidateViewSet(viewsets.ModelViewSet):
	queryset = Candidate.objects.all()
	serializer_class = CandidateSerializer
