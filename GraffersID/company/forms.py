from django import forms 
from .models import CompanyInfoModel

class AddCompany(forms.Form):
    company_logo=forms.ImageField()
    company_name=forms.CharField(max_length=50)
    company_location=forms.CharField(max_length=256)
    company_Registeration=forms.CharField(max_length=256)
    class META:
        model=CompanyInfoModel
    
    
        
          