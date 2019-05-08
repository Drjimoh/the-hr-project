from django.shortcuts import render
from .models import Cv, ScoredCv
from .serializers import CvSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework import status
from django.views import generic
from .forms import CvForm 

class ApiView(APIView):

	def get(self, request):
		cv = Cv.objects.all()
		serializer = CvSerializer(cv, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = CvSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenerateScoredCvView(generic.ListView):
	template_name = "cvranker/generate.html"
	model = ScoredCv
	def get_queryset(self):
		queryset = self.model.objects.all()

		return queryset

def get_top_cvs(request):
	cv_list = Cv.objects.all()[::-1]
	cv_score = 0
	ranked_cv_dict = {}

	for cv in cv_list:
		cv_score = 0
		if cv.qualification.qualification == 'BSc.':
			cv_score += 2
		elif cv.qualification.qualification == 'SSCE':
			cv_score += 1
		elif cv.qualification.qualification == 'Ph.D':
			cv_score += 8
		elif cv.qualification.qualification == 'MSc.':
			cv_score += 3
		ranked_cv_dict[cv] = cv_score
	name_list = list(ranked_cv_dict.keys())
	score_list = list(ranked_cv_dict.values())
	#creating a sorted list based on the score of the cvs
	scores = sorted(ranked_cv_dict.values(), reverse=True)
	#let's link the scores to the names
	final_list = []
	for scorer in scores:
		name_of_person = name_list[score_list.index(scorer)]
		output = str(name_of_person) + ' Scored ' + str(scorer)
		final_list.append(output)

				

	return render(request,
	 				'cvranker/rank.html', 
	 				{'final_list':final_list}
	 				)



def add_cv(request):
	cv_form = CvForm()
	if request.method == 'POST':
		cv_form = CvForm(request.POST)
		if cv_form.is_valid():
			cv_form_item = cv_form.save(commit=False)
			cv_form_item.save()
		cv_form = CvForm()
	else:
		cv_form = CvForm()
	return render(request, 'cvranker/index.html', {'form':cv_form})
