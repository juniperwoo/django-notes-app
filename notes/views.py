

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Note
from django.contrib.auth.decorators import login_required
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

@login_required
def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'index.html')

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

@login_required
def get_notes(request):
    notes = list(Note.objects.filter(user=request.user).values())
    return JsonResponse(notes, safe=False)

@login_required
def add_note(request):
    data = json.loads(request.body)
    note = Note.objects.create(content=data['content'], user=request.user)
    return JsonResponse({'message': 'Note added'})

@login_required
def delete_note(request, id):
    Note.objects.filter(id=id, user=request.user).delete()
    return JsonResponse({'message': 'Deleted'})

@login_required
def toggle_important(request, id):
    note = Note.objects.get(id=id, user=request.user)
    note.important = not note.important
    note.save()
    return JsonResponse({'message': 'updated'})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # redirect to login after signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})