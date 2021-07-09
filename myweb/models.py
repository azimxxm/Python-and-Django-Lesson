from django.db import models

class DataBase(models.Model):
    title = models.CharField('Nomlanishi', max_length=20)
    anons = models.CharField('Anons', max_length=50)
    full_test = models.TextField('Maqola matni..', max_length=100)
    data = models.DateTimeField('Maqola sanasi')

    def __str__(self):
        return self.title

    # class Meta:
    #     data_base_name = 'Data_Bases'
    #     data_base__name_news = 'Create news'