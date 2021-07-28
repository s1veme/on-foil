from rest_framework.generics import (
	CreateAPIView,
	ListAPIView
)

from rest_framework.exceptions import ValidationError

from .models import (
	Reservation,
	Table
)

from .serializers import (
	ReservationSerializer,
	TableTimeSerializer
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



class ReservationTimeListAPIView(ListAPIView):
	queryset = Table.objects.all()
	serializer_class = TableTimeSerializer
