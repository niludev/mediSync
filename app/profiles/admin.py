from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import PatientProfile, DoctorProfile


@admin.register(PatientProfile)
class PatientProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'doctor', 'qr_code_patient', 'created_at', 'updated_at')
    list_filter = ('created_at', 'doctor')
    search_fields = ('user__email', 'doctor__email')


@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'specialty', 'qr_code_doctor', 'created_at', 'updated_at')
    list_filter = ('specialty', 'created_at')
    search_fields = ('user__email',)
