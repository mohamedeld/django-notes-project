from django.shortcuts import render,redirect,get_object_or_404
from .models import Note
from .forms import NoteForm

from accounts.models import Profile
# Create your views here.

def all_notes(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    all_notes = Note.objects.filter(user=user)

    return render(request,'notes.html',{
        'all_notes':all_notes,
        'profile':profile,
    })


def note_detail(request,slug):
    note = get_object_or_404(Note,slug=slug)
    user = request.user
    profile = get_object_or_404(Profile, user=user)

    return render(request,'one_note.html',{
        'note':note,
        'profile': profile,
    })


def create_note(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()


            return redirect('/notes')
    else:
        form = NoteForm()

    return render(request,'create_note.html',{
        'form':form,
        'profile':profile,
    })

def edit_note(request,slug):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    note = get_object_or_404(Note,slug=slug)
    if request.method == 'POST':
        form = NoteForm(request.POST,instance=note)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            
            return redirect('/notes/')
    else:
        form = NoteForm(instance=note)

    return render(request,'edit_note.html',{
        'form':form,
        'profile':profile,
    })
