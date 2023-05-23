from typing import Any, Dict
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import TemplateView
from cherry.forms import *
# Create your views here.

#fb_views for returning string
def fb_views(request):
    return HttpResponse('This is fb_view')

#cb_views for returning string
class cb_views(View):
    def get(self,request):
        return HttpResponse('This is cb_view')
    

# #fb_views for returning HTML page
# def fb_view_html(request):
#     return render(request,'fb_view_html.html')





class cbv_context(TemplateView):
    template_name='cbv_context.html'

    def get_context_data(self, **kwargs):
         EDCO=super().get_context_data(**kwargs)

         EDCO['name']='DeviPrasad'
         EDCO['age']=22
         return EDCO
    


class HTML_FORM(TemplateView):
    template_name='HTML_FORM.html'
    def get_context_data(self, **kwargs):
        CO=super().get_context_data(**kwargs)
        TO=TopicForm()
        CO['TO']=TO
        return CO

class CLASS_HTML(View):
    template_name='CLASS_HTML.html'
    def get(self,request):
        return render(request,'CLASS_HTML.html') 
    



