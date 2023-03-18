from django.shortcuts import render
from .serializers import MenuSerializer
from rest_framework import viewsets
from .models import Menu
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Menu
from .models import Booking
from .serializers import BookingSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.


def index(request):
    return render(request, 'index.html', {})


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
