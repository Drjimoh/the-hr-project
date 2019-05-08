from django.forms import ModelForm
from .models import Cv



class CvForm(ModelForm):
	class Meta:
		model = Cv
		fields = '__all__'