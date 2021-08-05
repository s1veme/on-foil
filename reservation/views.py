from rest_framework.exceptions import ValidationError

from rest_framework.views import APIView

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
	TableTimeSerializer,
	ReservationTimeSerializer
)

from .service import check_difference_time


class ReservationCreateAPIView(CreateAPIView):
	queryset = Reservation.objects.all()
	serializer_class = ReservationSerializer

	def validate(self):
		start = self.request.data['start']
		end = self.request.data['end']

		if not check_difference_time(start, end):
			raise ValidationError({'error': 'the time difference must be one and a half hours'})


	def create(self, request, *args, **kwargs):
		self.validate()
		return super().create(request, *args, **kwargs)


class ReservationListAPIView(ListAPIView):
	serializer_class = ReservationTimeSerializer

	def get_queryset(self):
		date = self.kwargs['date']
		table_id = self.kwargs['table']
		return Reservation.objects.filter(date=date, table=table_id)


class TableTimeListAPIView(ListAPIView):
	queryset = Table.objects.all()
	serializer_class = TableTimeSerializer
