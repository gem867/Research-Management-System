from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Register your model here.
from django.shortcuts import get_object_or_404

# Create your views here.
from .models import *

def home(request):
    return render(request, "home.html", context={"current_tab": "home"})

def authors(request):
    return render(request, "authors.html", context={"current_tab": "authors"})

def studies(request):
    return render(request, "studies.html", context={"current_tab": "studies"})


    
def authors_tab(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')
        authors = Author.objects.filter(author_name__icontains=query)  # Adjust the filter as needed
    else:
        authors = Author.objects.all()
    
    return render(request, "authors.html", 
                  context={"current_tab": "authors", 
                           "authors": authors,
                           "query": query if 'query' in locals() else ''})

def save_author(request):
    author_item = Author(
        author_name=request.POST['author_name'],
        author_title=request.POST['author_title'],
        author_type=request.POST['author_type'],
        author_department=request.POST['author_department'],
        employee_number=request.POST['employee_number'],  # Handle new field
    )
    author_item.save()
    return redirect('/authors')

def save_author(request):
    author_item=Author(
                       author_name=request.POST['author_name'],
                       author_title=request.POST['author_title'],
                       author_type=request.POST['author_type'],
                       author_department=request.POST['author_department']
                       )
    author_item.save()
    return redirect('/authors')


def edit_author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    if request.method == 'POST':
        author.author_name = request.POST['author_name']
        author.author_title = request.POST['author_title']
        author.author_type = request.POST['author_type']
        author.author_department = request.POST['author_department']
        author.save()
        return redirect('/authors')
    return render(request, 'edit_author.html', {'author': author})


def delete_author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    if request.method == 'POST':
        author.delete()
        return redirect('/authors')
    return render(request, 'delete_author.html', {'author': author})

def studies_list(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')
        studies = Study.objects.filter(title__icontains=query)  # Adjust the filter as needed
    else:
        studies = Study.objects.all()
    
    return render(request, 'studies.html', {'studies': studies, 'query': query if 'query' in locals() else ''})


def add_study(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        abstract = request.POST['abstract']
        keywords = request.POST['keywords']
        status = request.POST['status']
        date_started = request.POST['date_started']
        researchers = request.POST['researchers']
        file = request.FILES.get('file')
        
        new_study = Study(
            title=title,
            description=description,
            abstract=abstract,
            keywords=keywords,
            status=status,
            date_started=date_started,
            researchers=researchers,
            file=file
        )
        new_study.save()
        return redirect('/studies')
    
    return render(request, 'add_study.html')


def edit_study(request, study_id):
    study = get_object_or_404(Study, id=study_id)
    if request.method == 'POST':
        study.title = request.POST['title']
        study.description = request.POST['description']
        study.abstract = request.POST['abstract']
        study.keywords = request.POST['keywords']
        study.status = request.POST['status']
        study.date_started = request.POST['date_started']
        study.researchers = request.POST['researchers']
        if 'file' in request.FILES:
            study.file = request.FILES['file']
        study.save()
        return redirect('/studies')
    return render(request, 'edit_study.html', {'study': study})


def delete_study(request, study_id):
    study = get_object_or_404(Study, id=study_id)
    if request.method == 'POST':
        study.delete()
        return redirect('/studies')
    return render(request, 'delete_study.html', {'study': study})

def delete_study(request, study_id):
    study = get_object_or_404(Study, id=study_id)
    if request.method == 'POST':
        study.delete()
        return redirect('/studies')
    return render(request, 'delete_study.html', {'study': study})


def study_detail(request, study_id):
    study = get_object_or_404(Study, id=study_id)
    return render(request, 'study_detail.html', {'study': study})
