from email.header import Header
import django_tables2 as tables
from django.utils.html import format_html
from .models import Car

class CarTable(tables.Table):
    
    # sprzedawca = tables.Column(verbose_name="Seller", accessor= "seller_id__first_name")
    sprzedawca = tables.Column(verbose_name="Seller", empty_values=())
    details = tables.Column(verbose_name="", empty_values=())

    class Meta:
        model = Car
        template_name = 'django_tables2/bootstrap.html'
        exclude = ("col1", "description", "seller_id")
    
    def render_sprzedawca(self, record):
        return format_html("<p>{} {}.</p>", record.seller_id.first_name, str(record.seller_id.last_name)[0])

    def render_details(self, record):
        temp_url = record.get_absolute_url_details()
        return format_html("<a href ='{}' >Show details</p>", temp_url)


    
    
class MyCarTable(tables.Table):
    

    # editable = tables.LinkColumn('edit_post',verbose_name='', empty_values=())
    edit = tables.Column(verbose_name='',empty_values=())

    class Meta:
        model = Car
        template_name = 'django_tables2/bootstrap.html'
        exclude = ("col1", "description", "seller_id", "Seller")
    

    def render_edit(self, record):
        temp_url = record.get_absolute_url_edit()
        return format_html("<a href ='{}' >Edit post</p>", temp_url)