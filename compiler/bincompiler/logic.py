from py import code
from .models import CodeSource, Device
from subprocess import check_output, STDOUT, CalledProcessError
import subprocess
from django.conf import settings
from django.core.files.storage import default_storage
import os 
def compilefile(source):
    try:
        print(source.file.path)
        output = subprocess.call(['vasm6502', '-Fbin', '-dotdir', source.file.path, '-o', './media/documents/' +source.name + '.out'])
        
        source.hascompiled = True
        source.save()
        
        
        return output
    except CalledProcessError as exc:
        return exc.output
    except OSError as exc:
        return exc

def getCurrentWorkingDirectory():
    try:
        output = subprocess.check_output(['pwd'],shell=True)
        return output
    except CalledProcessError as exc:
        return(exc)
    except OSError as exc:
        return(exc)



def deleteFile(source):
    file = source.file
    deleteCodeSource(source.id)
    default_storage.delete(file.path)

    outpath = './media/documents/' +source.name + '.out'
    print("Deleting " + outpath)
    if os.path.isfile(outpath):
         os.remove(outpath)

def deleteCodeSource(id):
    CodeSource.objects.filter(id=id).delete()


def getUploadedCode(code_id):
    code_source = CodeSource.objects.get(pk=code_id)
    file = default_storage.open(code_source.filepath)

def getAllUploadedCode():
    codes = CodeSource.objects.all()
    return codes