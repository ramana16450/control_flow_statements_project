from django.shortcuts import render

# Create your views here.
def jinjacondition(request):
    d={'a':100,'b':20,'c':30}
    return render(request,'jinjacondition.html',context=d)