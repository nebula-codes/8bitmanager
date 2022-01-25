from distutils.command.upload import upload
from operator import index
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .logic import *
from django.core.files.storage import default_storage
from .forms import UploadFileForm
from .models import CodeSource, Device
from django.conf import settings

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
    codes = getAllUploadedCode()
    compilation = compilefile(code_source)
    uploadForm = UploadFileForm()

    context = {
        'compilation': compilation,
        'code_source': code_source,
        'uploadForm': uploadForm,
        'codes': codes
    }

    return HttpResponseRedirect('/bincompiler/manage')

def manage(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manage')
    else:
        codes = getAllUploadedCode()
        uploadForm = UploadFileForm()
        context = {
            'uploadForm': uploadForm,
            'codes': codes
        }
        return render(request, 'bincompiler/manage.html', context)



def delete(request, code_id):
    if request.method == 'GET':
        source = CodeSource.objects.get(pk=code_id)

        deleteFile(source)

        return HttpResponseRedirect('/bincompiler/manage')


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404