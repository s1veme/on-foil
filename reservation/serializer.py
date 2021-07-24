from rest_frameword.serializers import ModelSerializer

from .models import Reservation


class ReservationSerializer(ModelSerializer):
	class Meta:
		model = Reservation
		fields = [
			'id',
			'date',
			'start',
			'end'
		]