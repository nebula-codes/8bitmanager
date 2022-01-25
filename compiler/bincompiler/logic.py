from py import code
from .models import CodeSource, Device
from subprocess import check_output, STDOUT, CalledProcessError
import subprocess
from django.core.files.storage import default_storage

def compilefile(source):
    try:
        print('teest')
        print(getCurrentWorkingDirectory())
        output = subprocess.run(['vasm6502', '-Fbin', '-dotdir', source.filepath], stdout=subprocess.PIPE, shell=True).stdout.decode("utf-8")
        return output
    except CalledProcessError as exc:
        return exc.output
    except OSError as exc:
        return exc.output

def getCurrentWorkingDirectory():
    try:
        output = subprocess.check_output(['pwd'],shell=True)
        return output
    except CalledProcessError as exc:
        return(exc)
    except OSError as exc:
        return(exc)



def handleUploadedCode(file):

    default_storage.save(file.name, file)

def getUploadedCode(code_id):
    code_source = CodeSource.objects.get(pk=code_id)
    file = default_storage.open(code_source.filepath)

def getAllUploadedCode():
    codes = CodeSource.objects.all()
    return codes