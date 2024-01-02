from django.shortcuts import render,get_object_or_404
from django.http import Http404,HttpResponse
# Create your views here.
from django.shortcuts import render
from .models import Links,Skills,Profile,Jobroles,Projects
# Create your views here.
def Index(request):
    profiles = Profile.objects.all()[:1]
    roles = Jobroles.objects.all()
    links = Links.objects.all()
    context = {'profiles':profiles,'roles':roles,'links':links}
    return render(request,'index.html',context)

# My skills part
def MySkills(request):
    front_end = Skills.objects.filter(option='Front-End Development')
    back_end = Skills.objects.filter(option='Back-End Development')
    others= Skills.objects.filter(option='OtherSkills')
    context = {'front_end':front_end,'back_end':back_end,'others':others}
    return render(request,'skills.html',context)

def MyProjects(request):
    projects = Projects.objects.all()
    context = {'projects':projects}
    return render(request,'my-projects.html',context)

def ProjectDetails(request,id):
    try:
        project = get_object_or_404(Projects,pk=id)
    
    except:
        raise Http404
    
    context = {'project':project}
    return render(request,'project-detail.html',context)

def Resume(request):
    resume = Profile.objects.all()
    context = {'resume':resume}
    return render(request,'resume.html',context)

def Download_resume(request,file_id):
    uploaded_file = Profile.objects.get(pk=file_id)
    response = HttpResponse(uploaded_file.resume_doc, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.resume_doc.name}"'
    return response

def Contact(request):
    return render(request,'contact.html')

#HTTP Error 403 - Forbidden
def custom_403_view(request, exception=None):
    return render(request, '403.html', status=403)

# Page not found
def custom_404(request, exception):
    return render(request, '404.html', status=404)

# Server Internal Error
def custom_500(request):
    return render(request, '500.html', status=500)
