from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Coffee
from .forms import CoffeeForm
# Create your views here.

def index(request):
    # return HttpResponse('hello')
    name = 'Michael'
    my_list = [1,2,3,4,5]
    return render(request, 'index.html', 
    {'my_name' : name, "my_list" : my_list})

def coffee_view(request):
    coffee_all = Coffee.objects.all()   # SELECT * FROM Coffee
    # 만약 request가 POST라면 
        # POST를 바탕으로 Form을 만들고
        # Form이 유효하면 저장
    
    form = CoffeeForm(request.POST) # 완성된 Form
    if request.method in ['POST']:
        if form.is_valid(): # 완성된 Form이 유효하다면:
            form.save()     # Form을 model에 저장

    return render(request, 'coffee_home.html', 
    {"coffee_list" : coffee_all, "coffee_form" : form})

def detail(request, question_id):
    coffee_all = Coffee.objects.all()   # SELECT * FROM Coffee

    form = CoffeeForm(request.POST) # 완성된 Form
    if request.method == 'POST':
        if form.is_valid(): # 완성된 Form이 유효하다면:
            form.save()     # Form을 model에 저장
            return redirect('pybo:coffee')
        else:
            id = request.POST.get('id')     # POST request에서 name='id' 값을 받아온다
            c = get_object_or_404(Coffee, id=id)    # model의 데이터를 받아오며, 없을경우 404 출력
            c.delete()      # 데이터 delete

            return redirect('pybo:coffee')

    return render(request, 'coffee.html', 
    {"coffee_list" : coffee_all, "coffee_form" : form})