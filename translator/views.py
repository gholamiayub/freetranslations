from pyexpat import model
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib import messages

from translator.models import Project, Text
from translator.forms import ProjectForm, TextForm, EditTextForm, EditProjectForm


# @login_required
# after fixing login and auth system uncomment @login_required
def add_text(request, project_slug):
    print("-----------------> Hi")
    if request.method == "POST":
        form = TextForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            form = form.save(commit=False)
            project = Project.objects.get(slug=project_slug)
            # connect project to the text
            form.project = project
            form.save()
            text = Text.objects.get(name=cd['name'])
            return redirect(reverse('translator:text_detail',
                                    kwargs={'project_slug': project_slug,
                                             'text_slug': text.slug}))
    else:
        form = TextForm()
    return render(request,
                  'translator/add_text.html',
                  {'form': form})

# @login_required
def create_project(request):
    """View for creating new translation project."""
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            # add form requested user to project owner field
            form.owner = request.user
            form.save()
            name = request.POST.get('name')
            obj = Project.objects.get(name=name)
            return redirect(reverse('translator:project_detail', kwargs={'slug':obj.slug}))
    else:
        form = ProjectForm()
    return render(request,
                  'translator/create_project.html',
                  {'form': form})
# adding LoginRequiredMixin to prevent anonymous user form submit
class CreateProject(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'translator/create_project.html'

        
def edit_project(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    # if request.user == text.owner:
    #     pass
    if request.method == "POST":
        form = EditProjectForm(request.POST, instance=project)
        if form.is_valid:
            form.save()
            messages.success(request,
                            "Edited successfully.",
                            extra_tags="")
            return redirect(reverse('translator:project_detail',
                                    kwargs={'slug': project_slug}))
        messages.error(request, "")
    else:
        form = EditProjectForm(instance=project)
    return render(request, "translator/project_edit.html", {"form": form})


class ProjectListView(ListView):
    print("This is list view")
    model = Project
    paginate = 20
    context_object_name = 'projects'
    template_name = 'translator/list.html'

# later delete this
def projects(request):
    pass
    # projects = Project.objects.all()
    # context = {'projects': projects}
    # return render(request, 'translator/list.html', context=context)

class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'project'

def text_detail(request, project_slug, text_slug):
    text = Text.objects.get(slug=text_slug)
    return render(request, 
                  'translator/text_detail.html',
                  {'text': text})

def text_edit(request, text_slug):
    text = get_object_or_404(Text, slug=text_slug)
    project_slug = text.project.slug
    # if request.user == text.owner:
    #     pass
    print("----------- i'm here")
    if request.method == "POST":
        form = EditTextForm(request.POST, instance=text)
        print("------------ i'm in bottom of form")
        if form.is_valid:
            form.save()
            print("---------------- i'm in validation.")
            messages.success(request,
                            "Edited successfully.",
                            extra_tags="")
            return redirect(reverse('translator:text_detail',
                                    kwargs={'project_slug': project_slug,
                                             'text_slug': text_slug}))
        messages.error(request, "")
    else:
        form = EditTextForm(instance=text)
    return render(request, "translator/text_edit.html", {"form": form})

def translate_editor(request, text_slug):
    text = get_object_or_404(Text, slug=text_slug)
    project_slug = text.project.slug
    print("------------------000))))))))))")
    if request.method == "POST":
        form = TextForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            form = form.save(commit=False)
            project = Project.objects.get(slug=project_slug)
            # connect project to the text
            form.project = project
            form.save()
            return redirect(reverse('translator:text_detail',
                                    kwargs={'project_slug': project_slug,
                                             'text_slug': text.slug}))
    else:
        form = TextForm()
        source_form = EditTextForm(instance=text)
    return render(request,
                  "translator/translate_editor.html",
                  {'form': form, 
                   'source_form': source_form,
                   'text': text})

