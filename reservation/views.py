from rest_framework.generics import CreateAPIView

from .models import Reservation
from .serializers import ReservationSerializer

# dev views
from rest_framework.views import APIView
from .service import generate_pdf
from rest_framework.response import Response
from .serializers import TableSerializer
from .models import Table


class ReservationCreateAPIView(CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class TestPDF(APIView):
	def get(self, request, *args, **kwargs):
		data = TableSerializer(
			Table.objects.all(),
			many=True
		).data
		params = {
			'test': 'test',
			'reservation_data': data
		}
		generate_pdf(params)
		return Response({'status': 200})