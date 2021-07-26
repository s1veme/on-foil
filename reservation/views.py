from rest_framework.generics import CreateAPIView

from .models import Reservation
from .serializers import ReservationSerializer

# dev views
from rest_framework.views import APIView
from .service import generate_pdf
from rest_framework.response import Response


class ReservationCreateAPIView(CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class TestPDF(APIView):
	def get(self, request, *args, **kwargs):
		params = {
			'test': 'test'
		}
		generate_pdf(params)
		return Response({'status': 200})