from django.db import models
from django.contrib.auth.models import User
from contacts.models import Contact
from leads.models import Lead


class Deal(models.Model):
    STAGE_CHOICES = [
        ('discovery', 'Discovery'),
        ('proposal', 'Proposal'),
        ('negotiation', 'Negotiation'),
        ('closed_won', 'Closed Won'),
        ('closed_lost', 'Closed Lost'),
    ]

    title = models.CharField(max_length=200)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='deals')
    lead = models.ForeignKey(Lead, on_delete=models.SET_NULL, null=True, blank=True, related_name='deals')
    stage = models.CharField(max_length=20, choices=STAGE_CHOICES, default='discovery')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    expected_close_date = models.DateField()
    probability = models.IntegerField(default=50, help_text="Probability of closing (%)")
    description = models.TextField(blank=True, null=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='assigned_deals')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_deals')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']