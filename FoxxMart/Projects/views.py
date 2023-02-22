from django.shortcuts import render

# Create your views here.

def IDACA(request):

    return render(request, 'Projects/idaca.html', {})

def gallery(request):

    return render(request, 'Projects/gallery.html', {})


    

def bc(request):

    return render(request, 'Projects/bc.html', {})




def africanus(request):

    return render(request, 'Projects/africanus.html', {})


def about(request):

    return render(request, 'Projects/about.html', {})

def services(request):

    return render(request, 'Projects/services.html', {})

def contact(request):

    return render(request, 'Projects/contact.html', {})
