from django.conf import settings
from django.db import models

# -------------------
# Doctor Profile Model
# -------------------

class DoctorProfile(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL ,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'doctor'},
        related_name='doctor_profiles'
    )
    qr_code_doctor =models.CharField(max_length=255, null=True, blank=True)
    specialty = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.user_id and getattr(self.user, "role", None) != "doctor":
            raise ValueError('Selected user is not a doctor.')
        super().save(*args, **kwargs)

# -------------------
# Patient Profile Model
# -------------------

class PatientProfile(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'patient'},
        related_name='patient_profiles'
    )
    doctor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='patients_assigned',
        # limit_choices_to is just a display filter in admin or automated forms.
        limit_choices_to={'role': 'doctor'}
    )
    qr_code_patient =models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # At the database level, the restriction is not enforced. So if you manually code it, the wrong user may still be logged in.
    def save(self, *args, **kwargs):
        if self.doctor_id and getattr(self.doctor, "role", None) != "doctor":
        # if self.doctor and self.doctor.role != 'doctor':
            raise ValueError('Selected user is not a doctor.')

        if self.user_id and getattr(self.user, "role", None) != "patient":
        # if self.user.role != 'patient':
            raise ValueError('Selected user is not a patient.')
        super().save(*args, **kwargs)