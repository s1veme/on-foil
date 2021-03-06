from datetime import datetime

from rest_framework.serializers import (
	SerializerMethodField,
	ModelSerializer,
	ValidationError
)

from .models import (
	Reservation,
	Table
)


class ReservationSerializer(ModelSerializer):
	class Meta:
		model = Reservation
		fields = [
			'id',		
			'name',
			'surname',
			'phone_number',
			'start',
			'end',
			'date',
			'table',
			'taste',
			'sturdiness',
			'before_arrival',
			'wishes'
		]


class ShortReservationSerializer(ModelSerializer):
	class Meta:
		model = Reservation
		fields = [
			'id',
			'start',
			'end',
			'table',
		]


class ReservationTimeSerializer(ModelSerializer):
	class Meta:
		model = Reservation
		fields = [
			'start',
			'end',
		]


class ShortTableSerializer(ModelSerializer):
	reservation = SerializerMethodField()
	
	class Meta:
		model = Table
		fields = [
			'id',
			'reservation',
		]


	@staticmethod
	def get_reservation(obj):
		qs = ShortReservationSerializer(
			Reservation.objects.filter(
				table=obj,
				date=datetime.today()
			),
			many=True
		)
		return qs.data


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
			Reservation.objects.filter(
				table=obj,
				date=datetime.today()
			),
			many=True
		)
		return qs.data


class TableTimeSerializer(ModelSerializer):
	reservation = SerializerMethodField()

	class Meta:
		model = Table
		fields = [
			'id',
			'reservation'
		]


	@staticmethod
	def get_reservation(obj):
		qs = ReservationTimeSerializer(
			Reservation.objects.filter(table=obj),
			many=True
		)
		return qs.data