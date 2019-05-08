from django.db import models



class Title(models.Model):
	title = models.CharField(max_length=100)

	def __str__(self):
		return self.title

class Qualification(models.Model):
	qualification = models.CharField(max_length=200)

	def __str__(self):
		return self.qualification

class Cv(models.Model):
	title = models.ForeignKey(Title, on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=200, null=False,  blank=False)
	qualification = models.ForeignKey(Qualification, on_delete=models.SET_NULL, null=True)
	age = models.IntegerField( null=False, blank=False)
	professional_profile = models.TextField('Tell us about your professional career', blank=False, null=False)
	hobbies = models.TextField(null=False, blank=True)

	def __str__(self):
		return(str(self.title) + ' ' + str(self.name)) 


class ScoredCv(models.Model):
	name = models.CharField(max_length=200, null=False, blank=False)
	score = models.IntegerField(null=False, blank=False)


	def __str__(self):
		return (str(self.name) + ' ' + str(self.score))


