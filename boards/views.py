from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

from .serializers import BoardSerializer
from .models import Board


class BoardView(ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class BoardDetailView(RetrieveDestroyAPIView):
    queryset = Board.objects.all()
    lookup_field = 'id'
    serializer_class = BoardSerializer
