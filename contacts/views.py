from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Contact
from .forms import ContactForm


@login_required
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})


@login_required
def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contacts/contact_detail.html', {'contact': contact})


@login_required
def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.created_by = request.user
            contact.save()
            messages.success(request, "Contact created successfully!")
            return redirect('contact_detail', pk=contact.pk)
        else:
            messages.error(request, "Contact creation failed. Please correct the errors.")
    else:
        form = ContactForm()

    return render(request, 'contacts/contact_form.html', {'form': form, 'action': 'Create'})


@login_required
def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, "Contact updated successfully!")
            return redirect('contact_detail', pk=contact.pk)
        else:
            messages.error(request, "Contact update failed. Please correct the errors.")
    else:
        form = ContactForm(instance=contact)

    return render(request, 'contacts/contact_form.html', {'form': form, 'action': 'Update', 'contact': contact})


@login_required
def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        messages.success(request, "Contact deleted successfully!")
        return redirect('contact_list')

    return render(request, 'contacts/contact_confirm_delete.html', {'contact': contact})


@login_required
def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)

    # Check if the user has permission to delete this contact
    if contact.created_by != request.user and not request.user.is_staff:
        messages.error(request, "You don't have permission to delete this contact.")
        return redirect('contact_detail', pk=pk)

    if request.method == 'POST':
        contact_name = f"{contact.first_name} {contact.last_name}"
        contact.delete()
        messages.success(request, f"Contact '{contact_name}' has been deleted successfully.")
        return redirect('contact_list')

    return render(request, 'contacts/contact_delete.html', {'contact': contact})