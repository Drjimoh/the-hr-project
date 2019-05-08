from django.contrib import admin
from .models import *


admin.site.register(Title)
admin.site.register(Qualification)
admin.site.register(Cv)
admin.site.register(ScoredCv)


admin.site.site_header = 'Web HR'
