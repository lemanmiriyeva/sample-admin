from django.apps import apps
from django.contrib import messages
from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.sites import site


def dashboard_home(request):
    models = []
    for model, model_admin in site._registry.items():
        models.append({
            "name": model._meta.model_name,
            "app_label": model._meta.app_label,
            "verbose_name": model._meta.verbose_name_plural.title(),
        })
    return render(request, 'dashboard/home.html', {"models": models})


def get_model(app_label, model_name):
    return apps.get_model(app_label, model_name)

def get_registered_models():
    from django.contrib.admin.sites import site
    models = []
    for model, model_admin in site._registry.items():
        models.append({
            "name": model._meta.model_name,
            "app_label": model._meta.app_label,
            "verbose_name": model._meta.verbose_name_plural.title(),
        })
    return models

def model_list(request, app_label, model_name):
    model = get_model(app_label, model_name)
    objects = model.objects.all()
    models = get_registered_models()
    return render(request, 'dashboard/model_list.html', {
        'objects': objects,
        'model_name': model._meta.verbose_name.title(),
        'fields': model._meta.fields,
        'app_label': app_label,
        'model_key': model_name,
        'models': models,
    })

def model_add(request, app_label, model_name):
    model = get_model(app_label, model_name)
    Form = modelform_factory(model, exclude=[])
    models = get_registered_models()
    if request.method == 'POST':
        form = Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Added successfully.")
            return redirect('dashboard:model_list', app_label, model_name)
    else:
        form = Form()
    return render(request, 'dashboard/model_form.html', {'form': form, 'action': 'Add', 'models': models})

def model_edit(request, app_label, model_name, pk):
    model = get_model(app_label, model_name)
    obj = get_object_or_404(model, pk=pk)
    Form = modelform_factory(model, exclude=[])
    models = get_registered_models()
    if request.method == 'POST':
        form = Form(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Updated successfully.")
            return redirect('dashboard:model_list', app_label, model_name)
    else:
        form = Form(instance=obj)
    return render(request, 'dashboard/model_form.html', {'form': form, 'action': 'Edit', 'models': models})

def model_delete(request, app_label, model_name, pk):
    model = get_model(app_label, model_name)
    obj = get_object_or_404(model, pk=pk)
    obj.delete()
    messages.success(request, "Deleted successfully.")
    return redirect('dashboard:model_list', app_label, model_name)
