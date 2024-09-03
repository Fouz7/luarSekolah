from django.db import models
from api.models.users_models import User
from api.models.categories_models import Category

class DataPelatihan(models.Model):
    nama_pelatihan = models.CharField(max_length=100)
    trainer = models.ForeignKey(User, on_delete=models.CASCADE)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    nilai_feedback = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nama_pelatihan