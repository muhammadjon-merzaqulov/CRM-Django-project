from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Task
from .forms import TaskForm


@login_required
def task_list(request):
    # Get filter parameters
    status_filter = request.GET.get('status', '')
    priority_filter = request.GET.get('priority', '')

    # Base queryset
    tasks = Task.objects.all()

    # Apply filters
    if status_filter:
        tasks = tasks.filter(status=status_filter)

    if priority_filter:
        tasks = tasks.filter(priority=priority_filter)

    # Get overdue tasks
    today = timezone.now()
    overdue_tasks = tasks.filter(status__in=['not_started', 'in_progress'], due_date__lt=today)

    # Get upcoming tasks (due in the next 7 days)
    next_week = today + timezone.timedelta(days=7)
    upcoming_tasks = tasks.filter(status__in=['not_started', 'in_progress'], due_date__gte=today,
                                  due_date__lte=next_week)

    # Get completed tasks
    completed_tasks = tasks.filter(status='completed')

    context = {
        'tasks': tasks,
        'overdue_tasks': overdue_tasks,
        'upcoming_tasks': upcoming_tasks,
        'completed_tasks': completed_tasks,
        'status_filter': status_filter,
        'priority_filter': priority_filter,
    }

    return render(request, 'tasks/task_list.html', context)


@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})


@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            messages.success(request, "Task created successfully!")
            return redirect('task_detail', pk=task.pk)
        else:
            messages.error(request, "Task creation failed. Please correct the errors.")
    else:
        # Pre-populate fields if provided in GET parameters
        initial_data = {}
        contact_id = request.GET.get('contact_id')
        lead_id = request.GET.get('lead_id')
        deal_id = request.GET.get('deal_id')

        if contact_id:
            from contacts.models import Contact
            try:
                contact = Contact.objects.get(id=contact_id)
                initial_data['contact'] = contact
            except Contact.DoesNotExist:
                pass

        if lead_id:
            from leads.models import Lead
            try:
                lead = Lead.objects.get(id=lead_id)
                initial_data['lead'] = lead
                if not contact_id:  # Only set contact if not already set
                    initial_data['contact'] = lead.contact
            except Lead.DoesNotExist:
                pass

        if deal_id:
            from deals.models import Deal
            try:
                deal = Deal.objects.get(id=deal_id)
                initial_data['deal'] = deal
                if not contact_id:  # Only set contact if not already set
                    initial_data['contact'] = deal.contact
            except Deal.DoesNotExist:
                pass

        # Default assigned_to to current user
        initial_data['assigned_to'] = request.user

        form = TaskForm(initial=initial_data)

    return render(request, 'tasks/task_form.html', {'form': form, 'action': 'Create'})


@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully!")
            return redirect('task_detail', pk=task.pk)
        else:
            messages.error(request, "Task update failed. Please correct the errors.")
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/task_form.html', {'form': form, 'action': 'Update', 'task': task})


@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        messages.success(request, "Task deleted successfully!")
        return redirect('task_list')

    return render(request, 'tasks/task_confirm_delete.html', {'task': task})


@login_required
def task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.status = 'completed'
        task.save()
        messages.success(request, "Task marked as completed!")

        # Redirect back to the referring page if available
        next_url = request.POST.get('next', 'task_list')
        return redirect(next_url)

    return redirect('task_detail', pk=pk)