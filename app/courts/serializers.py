from rest_framework import serializers

from courts.models import Court


class CourtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Court
        fields = (
            'pk',
            'name',
            'address',
            'lat',
            'lng',
            'no_basket',
            'bench',
            'showerbox',
            'parking',
        )