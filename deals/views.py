from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from .models import Deal
from .forms import DealForm


@login_required
def deal_list(request):
    deals = Deal.objects.all()

    # Calculate total value by stage
    stage_totals = Deal.objects.values('stage').annotate(total=Sum('amount'))
    stage_totals_dict = {item['stage']: item['total'] for item in stage_totals}

    # Calculate total value
    total_value = sum(stage_totals_dict.values())

    # Calculate weighted value (probability * amount)
    weighted_value = Deal.objects.aggregate(
        weighted_total=Sum('amount', field='amount * probability / 100')
    )['weighted_total'] or 0

    context = {
        'deals': deals,
        'stage_totals': stage_totals_dict,
        'total_value': total_value,
        'weighted_value': weighted_value,
    }

    return render(request, 'deals/deal_list.html', context)


@login_required
def deal_detail(request, pk):
    deal = get_object_or_404(Deal, pk=pk)
    return render(request, 'deals/deal_detail.html', {'deal': deal})


@login_required
def deal_create(request):
    if request.method == 'POST':
        form = DealForm(request.POST)
        if form.is_valid():
            deal = form.save(commit=False)
            deal.created_by = request.user
            deal.save()
            messages.success(request, "Deal created successfully!")
            return redirect('deal_detail', pk=deal.pk)
        else:
            messages.error(request, "Deal creation failed. Please correct the errors.")
    else:
        # Pre-populate contact if provided in GET parameters
        contact_id = request.GET.get('contact_id')
        lead_id = request.GET.get('lead_id')
        initial_data = {}

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
                initial_data['contact'] = lead.contact
                initial_data['title'] = f"Deal from {lead.title}"
                initial_data['amount'] = lead.estimated_value
            except Lead.DoesNotExist:
                pass

        form = DealForm(initial=initial_data)

    return render(request, 'deals/deal_form.html', {'form': form, 'action': 'Create'})


@login_required
def deal_update(request, pk):
    deal = get_object_or_404(Deal, pk=pk)
    if request.method == 'POST':
        form = DealForm(request.POST, instance=deal)
        if form.is_valid():
            form.save()
            messages.success(request, "Deal updated successfully!")
            return redirect('deal_detail', pk=deal.pk)
        else:
            messages.error(request, "Deal update failed. Please correct the errors.")
    else:
        form = DealForm(instance=deal)

    return render(request, 'deals/deal_form.html', {'form': form, 'action': 'Update', 'deal': deal})


@login_required
def deal_delete(request, pk):
    deal = get_object_or_404(Deal, pk=pk)
    if request.method == 'POST':
        deal.delete()
        messages.success(request, "Deal deleted successfully!")
        return redirect('deal_list')

    return render(request, 'deals/deal_confirm_delete.html', {'deal': deal})


@login_required
def update_deal_stage(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        deal_id = request.POST.get('deal_id')
        new_stage = request.POST.get('new_stage')

        try:
            deal = Deal.objects.get(id=deal_id)
            deal.stage = new_stage
            deal.save()
            return JsonResponse({'success': True})
        except Deal.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Deal not found'})

    return JsonResponse({'success': False, 'error': 'Invalid request'})