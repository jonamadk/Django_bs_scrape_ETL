from rest_framework import serializers
from .models import LiveTradingData

class LiveTradingDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = LiveTradingData
        fields = '__all__'
    

