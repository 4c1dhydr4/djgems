from rest_framework import serializers
from apps.gems.models import Gem, GemProfile

class GemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Gem
		fields = ('id', 'nombre', 'latitude' ,'longitude')

class GemProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = GemProfile
		fields = ('id', 'username', 'password' ,'nombre','apellidos','photo')