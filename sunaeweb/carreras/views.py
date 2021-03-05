from django.shortcuts import render

def carreras(request, *args, **kwargs):
    carre = carreer.objects.filter(active__exact=True)
    context = {
        'carre': carre
    }
    return render(request, 'home.html', context=context)