from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from apps.gems.serializers import GemSerializer, GemProfileSerializer
from apps.gems.models import Gem, Configuration, GemProfile

def index(request):
	return render(request, 'index.html',{})

def login(request):
	return render(request, 'login.html',{})


def change_locations(gem):
	configuration = Configuration.objects.last()
	if configuration.simulation_active:
		factor = float(configuration.factor)
		if configuration.left_right:
			gem.longitude = float(gem.longitude) - factor
			gem.latitude = float(gem.latitude)  - factor
		else:
			gem.longitude = float(gem.longitude) + factor
			gem.latitude = float(gem.latitude)  + factor
		gem.save()

class GemsView(viewsets.ModelViewSet):
	queryset = Gem.objects.all()
	model = Gem
	serializer_class = GemSerializer

	def list(self, request):
		queryset = Gem.objects.all()
		for gem in queryset:
			change_locations(gem)
		serializer = GemSerializer(queryset, many=True)
		return Response(serializer.data)

	def get_object(self):
		queryset = get_object_or_404(Gem, id=self.kwargs['pk'])
		change_locations(queryset)
		return queryset

class GemProfileView(viewsets.ModelViewSet):
	queryset = GemProfile.objects.all()
	model = GemProfile
	serializer_class = GemProfileSerializer

	def get_object(self):
		username =  self.kwargs['pk']
		queryset = get_object_or_404(GemProfile, username=username)
		return queryset