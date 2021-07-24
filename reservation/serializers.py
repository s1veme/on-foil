from rest_framework.serializers import ModelSerializer

from .models import Reservation


class ReservationSerializer(ModelSerializer):
	class Meta:
		model = Reservation
		fields = [
			'id',
			'name',
			'surname',
			'table',
			'date',
			'start',
			'end',
		]