from pyexpat import model
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
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

# adding LoginRequiredMixin to prevent anonymous users to submit form
class CreateProject(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'translator/create_project.html'
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

        
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

# adding message
# mixin view for check permisions  
class UpdateProject(UpdateView):
    model = Project
    form_class = EditProjectForm
    template_name = 'translator/project_edit.html'
    
    # to check if the requested user is same as owner user
    def get_object(self, *args, **kwargs):
        obj = super().get_object()
        if not obj.owner == self.request.user:
            raise Http404
        return obj



class ProjectListView(ListView):

    model = Project
    paginate = 20
    context_object_name = 'projects'
    template_name = 'translator/list.html'


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

