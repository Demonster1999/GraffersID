from django.db import models

### company review table
class CompanyReview(models.Model):
    reviewer_name=models.CharField(max_length=70)
    reviewer_company=models.CharField(max_length=50)
    reviewer_subject=models.CharField(max_length=256)
    reviewer_review=models.TextField()
    def __str__(self):
        ret = reviewer_name
        return ret
    class Meta:
        unique_together = ['reviewer_name']
        
    
    
