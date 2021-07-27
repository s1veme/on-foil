from rest_framework.generics import (
	CreateAPIView,
	ListAPIView
)

from .models import (
	Reservation,
	Table
)

from .serializers import (
	ReservationSerializer,
	TableTimeSerializer
)


class ReservationCreateAPIView(CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class ReservationTimeListAPIView(ListAPIView):
	queryset = Table.objects.all()
	serializer_class = TableTimeSerializer
