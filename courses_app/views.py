from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages


def index(request):
    context= {
        'all_courses': Course.objects.all()
    }
    return render(request, 'index.html', context)

def add_course(request):
    errors= Course.objects.basic_validator(request.POST)
    if errors:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/')
    else:
        
        course_des= Description.objects.create(description= request.POST['des'])
        Course.objects.create(cor_name= request.POST['name'], description= course_des)
        messages.success(request, "Course successfully created")
    return redirect('/')

def remove(request, course_id):
    context={
        'course': Course.objects.get(id= course_id)
    }
    return render(request, 'delete.html', context)

def delete(request, course_id):
    Course.objects.get(id= course_id).delete()
    return redirect('/')

def comments(request, course_id):
    this_course= Course.objects.get(id= course_id)
    if request.method == "GET":
        context={
            'all_comments': Comment.objects.all(),
        }
        return render(request, 'comments.html', context)
    else:
        errors= Comment.objects.basic_validator(request.POST)
        if errors:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect(f"/comments/{course_id}")
        else:
            Comment.objects.create(content= request.POST['comment'], course= this_course)
            return redirect(f"/comments/{course_id}")
