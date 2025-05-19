from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum
from django.utils import timezone
from leads.models import Lead
from deals.models import Deal
from tasks.models import Task
from contacts.models import Contact
import datetime


@login_required
def dashboard(request):
    # Get counts
    total_leads = Lead.objects.count()
    total_deals = Deal.objects.count()
    total_contacts = Contact.objects.count()
    total_tasks = Task.objects.count()

    # Get deals by stage
    deals_by_stage = Deal.objects.values('stage').annotate(count=Count('id'))
    deals_by_stage_dict = {item['stage']: item['count'] for item in deals_by_stage}

    # Get leads by status
    leads_by_status = Lead.objects.values('status').annotate(count=Count('id'))
    leads_by_status_dict = {item['status']: item['count'] for item in leads_by_status}

    # Get recent leads
    recent_leads = Lead.objects.order_by('-created_at')[:5]

    # Get recent deals
    recent_deals = Deal.objects.order_by('-created_at')[:5]

    # Get upcoming tasks
    today = timezone.now()
    upcoming_tasks = Task.objects.filter(
        status__in=['not_started', 'in_progress'],
        due_date__gte=today
    ).order_by('due_date')[:5]

    # Get overdue tasks
    overdue_tasks = Task.objects.filter(
        status__in=['not_started', 'in_progress'],
        due_date__lt=today
    ).order_by('due_date')[:5]

    # Get deal forecast
    deal_forecast = Deal.objects.aggregate(
        total_value=Sum('amount')
    )['total_value'] or 0

    # Get weighted deal forecast
    weighted_forecast = Deal.objects.aggregate(
        weighted_value=Sum('amount', field='amount * probability / 100')
    )['weighted_value'] or 0

    # Get deals closing this month
    this_month = today.month
    this_year = today.year
    deals_closing_this_month = Deal.objects.filter(
        expected_close_date__month=this_month,
        expected_close_date__year=this_year
    ).aggregate(
        total_value=Sum('amount')
    )['total_value'] or 0

    # Get deals by month for the next 6 months
    deals_by_month = []
    for i in range(6):
        month = (today.month + i - 1) % 12 + 1
        year = today.year + (today.month + i - 1) // 12
        month_name = datetime.date(year, month, 1).strftime('%B')

        month_deals = Deal.objects.filter(
            expected_close_date__month=month,
            expected_close_date__year=year
        ).aggregate(
            total_value=Sum('amount')
        )['total_value'] or 0

        deals_by_month.append({
            'month': month_name,
            'value': month_deals
        })

    context = {
        'total_leads': total_leads,
        'total_deals': total_deals,
        'total_contacts': total_contacts,
        'total_tasks': total_tasks,
        'deals_by_stage': deals_by_stage_dict,
        'leads_by_status': leads_by_status_dict,
        'recent_leads': recent_leads,
        'recent_deals': recent_deals,
        'upcoming_tasks': upcoming_tasks,
        'overdue_tasks': overdue_tasks,
        'deal_forecast': deal_forecast,
        'weighted_forecast': weighted_forecast,
        'deals_closing_this_month': deals_closing_this_month,
        'deals_by_month': deals_by_month,
    }

    return render(request, 'dashboard/dashboard.html', context)