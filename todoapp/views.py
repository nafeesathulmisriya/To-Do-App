from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .models import Task
from .forms import TaskForm


# -------------------- HOME PAGE --------------------
@login_required
def home(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created_on')
    return render(request, 'todoapp/home.html', {'tasks': tasks})


# -------------------- CREATE TASK --------------------
@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()

            # ✅ redirect to TASK LIST page (not single task)
            return redirect('task_details')
    else:
        form = TaskForm()

    return render(request, 'todoapp/create_task.html', {'form': form})


# -------------------- TASK LIST / DETAILS PAGE --------------------
@login_required
def task_details(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created_on')
    return render(request, 'todoapp/task_details.html', {'tasks': tasks})


# -------------------- MARK TASK COMPLETED --------------------
@login_required
def mark_completed(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    task.status = "Completed"
    task.save()

    # ✅ go back to task list
    return redirect('task_details')


# -------------------- TOGGLE TASK STATUS (OPTIONAL) --------------------
@login_required
def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if task.status == "Pending":
        task.status = "Completed"
    else:
        task.status = "Pending"

    task.save()
    return redirect('task_details')


# -------------------- DELETE TASK --------------------
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect('task_details')


# -------------------- EDIT TASK --------------------
@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_details')
    else:
        form = TaskForm(instance=task)

    return render(request, 'todoapp/edit.html', {'form': form})


# -------------------- LOGIN VIEW --------------------
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'accounts/login.html')

@login_required
def completed_tasks(request):
    tasks = Task.objects.filter(
        user=request.user,
        status="Completed"
    ).order_by('-created_on')

    return render(
        request,
        'todoapp/completed_tasks.html',
        {'tasks': tasks}
    )

