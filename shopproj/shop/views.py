
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Shop

class Add_shop(CreateView):
    model = Shop
    fields = "__all__"


class List_shop(ListView):
    model = Shop

class Detail_shop(DetailView):
    model = Shop


class Update_shop(UpdateView):
    model = Shop

    fields = "__all__"
    success_url = "/"

class Delete_shop(DeleteView):
    model = Shop
    success_url = "/"
    template_name = "shop/Shop_confirm.html"
