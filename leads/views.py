from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Lead
from .forms import LeadForm
from contacts.models import Contact


@login_required
def lead_list(request):
    leads = Lead.objects.all()
    return render(request, 'leads/lead_list.html', {'leads': leads})


@login_required
def lead_detail(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    return render(request, 'leads/lead_detail.html', {'lead': lead})


@login_required
def lead_create(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.created_by = request.user
            lead.save()
            messages.success(request, "Lead created successfully!")
            return redirect('lead_detail', pk=lead.pk)
        else:
            messages.error(request, "Lead creation failed. Please correct the errors.")
    else:
        # Pre-populate contact if provided in GET parameters
        contact_id = request.GET.get('contact_id')
        initial_data = {}
        if contact_id:
            try:
                contact = Contact.objects.get(id=contact_id)
                initial_data['contact'] = contact
            except Contact.DoesNotExist:
                pass
        form = LeadForm(initial=initial_data)

    return render(request, 'leads/lead_form.html', {'form': form, 'action': 'Create'})


@login_required
def lead_update(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    if request.method == 'POST':
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            messages.success(request, "Lead updated successfully!")
            return redirect('lead_detail', pk=lead.pk)
        else:
            messages.error(request, "Lead update failed. Please correct the errors.")
    else:
        form = LeadForm(instance=lead)

    return render(request, 'leads/lead_form.html', {'form': form, 'action': 'Update', 'lead': lead})


@login_required
def lead_delete(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    if request.method == 'POST':
        lead.delete()
        messages.success(request, "Lead deleted successfully!")
        return redirect('lead_list')

    return render(request, 'leads/lead_confirm_delete.html', {'lead': lead})


@login_required
def lead_convert(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    if request.method == 'POST':
        from deals.forms import DealForm
        form = DealForm(request.POST)
        if form.is_valid():
            deal = form.save(commit=False)
            deal.contact = lead.contact
            deal.lead = lead
            deal.created_by = request.user
            deal.save()

            # Update lead status to converted
            lead.status = 'converted'
            lead.save()

            messages.success(request, "Lead converted to deal successfully!")
            return redirect('deal_detail', pk=deal.pk)
        else:
            messages.error(request, "Lead conversion failed. Please correct the errors.")
    else:
        from deals.forms import DealForm
        initial_data = {
            'title': f"Deal from {lead.title}",
            'contact': lead.contact,
            'amount': lead.estimated_value,
        }
        form = DealForm(initial=initial_data)

    return render(request, 'leads/lead_convert.html', {'form': form, 'lead': lead})