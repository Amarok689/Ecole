from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Cursus,Student,Presence
from .form import StudentForm,particularform, EditStudentForm
from django.views.generic import CreateView, UpdateView
from django.urls import reverse
from django.shortcuts import get_object_or_404


#def index(request):
#  return HttpResponse("Racine de lycee")

# index : utilisation de HttpResponse
#def index(request):
#  result_list = Cursus.objects.order_by('name')
#  # chargement du template
#  template = loader.get_template('lycee/index.html')
#  # contexte
#  context = { 'liste' : result_list}
#  return HttpResponse(template.render(context, request))

# index : variante avec template intEgrE
def index (request):
  result_list = Cursus.objects.order_by('name')
  # contexte
  context = { 'liste' : result_list}
  # utilisation du template intEgrE
  return render (request, 'lycee/index.html', context)

def detail(request, cursus_id):
  eleves = Student.objects.filter(cursus=cursus_id)
  context = { 'eleves' : eleves}
  return render (request, 'cursus.html', context)
  
def detail_student(request,student_id):
  #result_list = Student.objects.get(pk=student_id)
  result_list = get_object_or_404(Student, pk=student_id)
  # context
  context = {'liste': result_list,}
  return render (request, 'lycee/student/detail_student.html' , context)

class StudentCreateView(CreateView):
  # ref au modEle
  model = Student
  # ref au formulaire
  form_class = StudentForm
  # le nom du render
  template_name = "lycee/student/create.html"


  def get_success_url(self):
    return reverse ("detail_student", args=(self.object.pk,))

#Particularform
class ParticularCreateView(CreateView):
  model = Presence
  form_class = particularform
  template_name = "lycee/form/particular.html"

  def get_success_url(self):
    return reverse ("index")
 
#EditStudent
class StudentEditView(UpdateView):
  model = Student
  form_class = StudentForm
  template_name= "lycee/form/student_edit.html"

  # Quand le fichier termine par edit => reconnu comme formulaire d'edition
  template_name_suffix="_edit"

  def get_success_url(self):
    return reverse ("detail_student", args=(self.object.pk,))

#Callofroll

def Callofroll(self, request, cursus_id):
  eleves = Student.objects.filter(cursus=cursus_id)
  context = { 'eleves' : eleves}

  if request.method == 'POST':
    date = request.POST.get("date")
    for student in students:
      missing = request.POST.get('student'+str(student.id), "off")
  
  return render (request, 'callofroll.html', context)

