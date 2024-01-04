from django.db import models

# Create your models here.
class Task(models.Model):
    PRIORITY = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    )
    title = models.CharField(max_length=300)
    description = models.TextField()
    due_date =models.DateTimeField()
    priority = models.CharField(choices=PRIORITY, default='Low', max_length=20)
    is_complete = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    updated_date = models.DateField(auto_now=True, editable=False)
    
    def __str__(self) -> str:
        return self.title


class Task_Photo(models.Model):
    tast = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='task_photo', blank=True)
    image = models.ImageField(upload_to='task_photo/')
    
    def __str__(self) -> str:
        return self.image.name

    @property
    def image_url(self):
        return self.image.url


