from distutils.command.upload import upload
from operator import index
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .logic import *
from django.core.files.storage import default_storage
from .forms import UploadFileForm
from .models import CodeSource, Device
# Create your views here.


def index(request):
    return HttpResponse("Hello, world")

def detail(request, code_id):
    try:
        code_source = CodeSource.objects.get(pk=code_id)
    except CodeSource.DoesNotExist:
        raise Http404
    return render(request, 'bincompiler/detail.html', {'code_source': code_source})
def compile(request, code_id):
    code_source = CodeSource.objects.get(pk=code_id)
    
    
    compilation = compilefile(code_source)
    return render(request, 'bincompiler/detail.html', {'code_source': code_source})

def manage(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('manage')
    else:
        codes = getAllUploadedCode()
        uploadForm = UploadFileForm()
        context = {
            'uploadForm': uploadForm,
            'codes': codes
        }
        return render(request, 'bincompiler/manage.html', context)

