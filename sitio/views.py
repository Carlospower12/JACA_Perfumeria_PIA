import json
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactoForm, ArchivoForm
from .models import Perfume

def cargar_json():
    try:
        with open(settings.BASE_DIR/"data"/"perfumes.json", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def inicio(request):
    return render(request, "inicio.html", {
        "perfumes": Perfume.objects.filter(disponible=True)[:3],
        "perfumes_json": cargar_json()[:3],
    })

def nosotros(request):
    return render(request, "nosotros.html")

def perfumes(request):
    return render(request, "perfumes.html", {
        "perfumes": Perfume.objects.filter(disponible=True),
        "perfumes_json": cargar_json(),
    })

def contacto(request):
    form = ContactoForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        messages.success(request, "Tu mensaje fue enviado correctamente.")
        return redirect("contacto")
    return render(request, "contacto.html", {"form": form})

def subir_archivo(request):
    form = ArchivoForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "El archivo se cargó correctamente.")
        return redirect("subir_archivo")
    return render(request, "subir.html", {"form": form})
def detalle_perfume(request, origen, identificador):
    if origen == "db":
        perfume = get_object_or_404(Perfume, id=identificador)

        return render(request, "detalle_perfume.html", {
            "perfume": perfume,
            "origen": "db",
        })

    elif origen == "json":
        perfumes = cargar_json()

        try:
            perfume = perfumes[int(identificador)]
        except (IndexError, ValueError):
            return redirect("perfumes")

        return render(request, "detalle_perfume.html", {
            "perfume": perfume,
            "origen": "json",
        })

    return redirect("perfumes")
