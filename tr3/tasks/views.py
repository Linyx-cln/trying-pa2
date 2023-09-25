from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


class NewTaskForm(forms.Form):
    taski = forms.CharField(label = "New Task")

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {
        "tasks" : request.session["tasks"]
    })


def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["taski"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "forms": NewTaskForm(request.POST)
            })

    return render(request, "tasks/add.html", {
        "forms" : NewTaskForm()
    })


