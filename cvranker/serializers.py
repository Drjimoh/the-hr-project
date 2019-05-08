from rest_framework import serializers
from .models import *

class CvSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cv 
		fields = ('name', 'age', 'qualification')