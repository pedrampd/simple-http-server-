from datetime import time
from django.http import HttpResponse
from django.shortcuts import render
from similarRect.models import Rectangle
from similarRect.forms import TextForm
from django.utils import timezone


current_time = timezone.get_current_timezone()
timezone.activate(current_time)

def get_name(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        
        # check whether it's valid:
        if form.is_valid():
            now = timezone.now()
            j = form.cleaned_data['jtext']
            main_rect_jason = j['main'] 
            rects_jason = j['input']

            main_rect = Rectangle(x=main_rect_jason['x'], y=main_rect_jason['y'], width=main_rect_jason['width'], height=main_rect_jason['height'],main=True, time_created = now)
            main_rect.save()

            for rect in rects_jason :
                temp = Rectangle(x=rect['x'], y=rect['y'], width=rect['width'], height=rect['height'],time_created = now)
                check_rects(main_rect,temp)
                temp.save()
            
            form = TextForm()
            return render(request, 'form.html', {'form': form,'answer':''})

    elif request.method == 'GET':
            s = []
            rects = (Rectangle.objects.filter(included = True))
            s = [str(rect) for rect in rects]
            form = TextForm()
            return render(request, 'form.html', {'form': form,'answer':s})

    form = TextForm()
    return render(request, 'form.html', {'form': form,'answer':''})


def check_rects(rect1,rect2):
    l1 = (rect1.x,rect1.y)
    r1 = (rect1.x + rect1.width, rect1.y + rect1.height)
    l2 = (rect2.x,rect2.y)
    r2 = (rect2.x + rect2.width, rect2.y + rect2.height)
    
    if r1[0] <= l2[0] or r2[0]<=l1[0] and (l1[1] <=r2[1] or l2[1] <= r1[1] ):
        return False
    else:
        rect2.included = True
        return True
 