from rest_framework.serializers import (
	SerializerMethodField,
	ModelSerializer
)

from .models import (
	Reservation,
	Table
)


class ReservationSerializer(ModelSerializer):
	class Meta:
		model = Reservation
		fields = [
			'name',
			'surname',
			'date',
			'start',
			'end',
		]


class TableSerializer(ModelSerializer):
	reservation = SerializerMethodField()

	class Meta:
		model = Table
		fields = [
			'id',
			'reservation',
		]


	@staticmethod
	def get_reservation(obj):
		qs = ReservationSerializer(
			Reservation.objects.filter(table=obj),
			many=True
		)
		return qs.data
