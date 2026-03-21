from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=100)
    required_skills = models.TextField()

    def __str__(self):
        return self.name

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    resume_file = models.FileField(upload_to='resumes/', null=True, blank=True)
    education = models.TextField(blank=True)
    skills = models.TextField(blank=True)
    tools = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    projects = models.TextField(blank=True)
    certifications = models.TextField(blank=True)
    extracted_text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Match(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='matches')
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    match_percentage = models.FloatField()
    fit_category = models.CharField(max_length=50) # Strong, Moderate, Low

class Prediction(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='predictions')
    top_role_1 = models.CharField(max_length=100)
    score_1 = models.FloatField()
    top_role_2 = models.CharField(max_length=100)
    score_2 = models.FloatField()
    top_role_3 = models.CharField(max_length=100)
    score_3 = models.FloatField()
