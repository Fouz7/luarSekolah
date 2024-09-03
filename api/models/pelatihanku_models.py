from django.db import models
from api.models.users_models import User
from api.models.datapelatihan_models import DataPelatihan

class PelatihanKu(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pelatihan = models.ForeignKey(DataPelatihan, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.fullname} - {self.pelatihan.nama_pelatihan}"