from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm

def projects(request):
    msg = 'Was up Dennis, Wtf is up Dennis'
    projects = Project.objects.all()
    context = {'projects': projects, 'message':msg}
    return render(request, 'projects/projects.html', context)

def individual_project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    return render(request, 'projects/single-project.html', {'project':projectObj, 'tags': tags, })

@login_required(login_url='login')
def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'projects/delete_template.html', context)


# render stuff from the backend to the frontend like the 'msg', this function is to render
# the static data or 'testdata' and the Pokemon Data from a FakeStore API
# def all_projects(request):
#     msg = 'Was up Dennis, Wtf is up Dennis'
#     age = 24
#     prolist = testdata.projectsList
#     store_items = pokemon.all_in
#     context = {'message':msg, 'age':age, 'projectlist':prolist, 'items':store_items}
#     return render(request, 'projects/projects.html', context)

### I have no Idea why this is not working....
# def individual_project(request, pk):
#     store_items = pokemon.all_in
#     projectObj = None
#     for i in store_items:
#         if i['id'] == pk:
#             projectObj = i
#     return render(request, 'projects/single-project.html', {'project':projectObj})

