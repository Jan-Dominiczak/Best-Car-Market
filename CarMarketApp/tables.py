from email.header import Header
import django_tables2 as tables
from .models import Car

class CarTable(tables.Table):
    class Meta:
        model = Car
        template_name = 'django_tables2/bootstrap.html'
        exclude = ("description",)

# class TestTable(tables.Table):
    