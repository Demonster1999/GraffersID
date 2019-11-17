from django.db import models
# Whole Project Database :
class CompanyInfoModel(models.Model):
    company_logo=models.ImageField()
    company_name=models.CharField(max_length=80)
    company_location=models.TextField()
    comapny_Registration_number=models.CharField(max_length=50)
    def __str__(self):
        ret = company_name
        return ret
    class Meta:
        unique_together = ['company_name']
        

    
