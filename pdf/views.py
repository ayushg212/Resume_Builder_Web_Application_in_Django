from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse,StreamingHttpResponse
from .functions import *
import io
from django.http import FileResponse
from docx2pdf import convert
import mimetypes
import os
from wsgiref.util import FileWrapper
# Create your views here.

def first_view(request):
    if request.method == 'POST':
        name = request.POST.get("name","")
        phone = request.POST.get("phone","")
        email = request.POST.get("email","")
        summary = request.POST.get("summary","")
        tenth = request.POST.get("tenth","")
        twelth = request.POST.get("twelth","")
        graduation = request.POST.get("graduation","")
        post_graduation = request.POST.get("post_graduation","")
        previous_work = request.POST.get("previous_work","")
        skills = request.POST.get("skills","")
        submitbutton= request.POST.get('submit')
        dict = { 'name':name , 'phone':phone , 'email':email , 'summary':summary , 'tenth':tenth , 'twelth':twelth , 'graduation':graduation , 'post_graduation':post_graduation , 'previous_work':previous_work , 'skills' : skills , 'submitbutton':submitbutton  }
        create_json(dict)
        return redirect('/page2')
    return render(request,"page1.html")

def second_view(request):
    deletefiles()
    return render( request , "page2.html" )

def download_pdf1(request):
    create_Doc_1()
    convert('resume1.docx')
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'resume1.pdf'
    filepath = base_dir + '/' + filename
    thefile = filepath
    filename = os.path.basename(thefile)
    chunk_size = 99999
    response = StreamingHttpResponse(FileWrapper(open(thefile,'rb'),chunk_size),content_type = mimetypes.guess_type(thefile)[0])
    response['Content-Length'] = os.path.getsize(thefile)
    response['Content-Disposition'] = "Attachment;fileaname=%s" % filename
    return response

def download_pdf2(request):
    create_Doc_2()
    convert('resume2.docx')
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'resume2.pdf'
    filepath = base_dir + '/' + filename
    thefile = filepath
    filename = os.path.basename(thefile)
    chunk_size = 9999
    response = StreamingHttpResponse(FileWrapper(open(thefile,'rb'),chunk_size),content_type = mimetypes.guess_type(thefile)[0])
    response['Content-Length'] = os.path.getsize(thefile)
    response['Content-Disposition'] = "Attachment;fileaname=%s" % filename
    return response


def download_pdf3(request):
    create_Doc_3()
    convert('resume3.docx')
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'resume3.pdf'
    filepath = base_dir + '/' + filename
    thefile = filepath
    filename = os.path.basename(thefile)
    chunk_size = 9999
    response = StreamingHttpResponse(FileWrapper(open(thefile,'rb'),chunk_size),content_type = mimetypes.guess_type(thefile)[0])
    response['Content-Length'] = os.path.getsize(thefile)
    response['Content-Disposition'] = "Attachment;fileaname=%s" % filename
    return response