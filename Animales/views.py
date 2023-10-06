from django.shortcuts import render

# Create your views here.
def animal_list(request):
    return render(request, 'animales/animal_list.html', {})
def protectora_list(request):
    return render(request, 'animales/protectora_list.html', {})
def colaborador_list(request):
    return render(request, 'animales/colaborador_list.html', {})
