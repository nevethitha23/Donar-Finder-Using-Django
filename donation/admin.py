from django.contrib import admin
from .models import Donor
from .models import Hospital, HospitalFormSubmission
admin.site.register(Donor)

admin.site.register(Hospital)
admin.site.register(HospitalFormSubmission)
