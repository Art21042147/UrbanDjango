from django.shortcuts import render

# Create your views here.
def class_template(request):
    return render(request, 'class_template.html')


def func_template(request):
    return render(request, 'func_template.html')
