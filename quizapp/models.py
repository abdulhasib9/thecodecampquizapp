from django.db import models

class Exam(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.name} ({self.code})"

class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    text = models.TextField()
    exhibit = models.ImageField(upload_to='static/exhibits/', blank=True, null=True)
    is_multiple = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)  # Add description field

    def __str__(self):
        return self.text

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255, blank=True)  # Allow blank text field
    is_correct = models.BooleanField(default=False)
    exhibit = models.ImageField(upload_to='static/exhibits/', blank=True, null=True)  # Exhibit field

    def __str__(self):
        return self.text if self.text else "Exhibit Option"  # Return "Exhibit Option" if no text

class Quiz(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return f"{self.name} ({self.code})"
