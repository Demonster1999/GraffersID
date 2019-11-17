from django import forms
from .models import CompanyReview
class AddReviewForm(forms.Form):
    reviewer_name=forms.CharField(max_length=70,required=True)
    reviewer_company=forms.CharField(max_length=50,required=True)
    reviewer_subject=forms.CharField(max_length=256)
    reviewer_review=forms.TextField()
    class Meta:
        model=CompanyReview

