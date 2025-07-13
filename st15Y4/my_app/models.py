from django.db import models

# Create your models here.
class Position(models.Model):
          name = models.CharField(max_length=50, unique=True)
          status = models.BooleanField(default=True)
          def __str__(self):
                    return self.name
          
class Staff(models.Model): 
          firstname = models.CharField(max_length=50, )
          lastname = models.CharField(max_length=50, )
          gender = models.CharField(
                    max_length=1,
                    choices=(('M', 'Male'), ('F', 'Female')),
                    default='O'
                    )
          dateofbirth = models.DateField()
          position = models.ForeignKey(Position, on_delete=models.CASCADE)
          def __str__(self):
                    return self.firstname + " " + self.lastname + " " + self.gender + " " + str(self.dateofbirth)
          
class Subject(models.Model):
          subject_name = models.CharField(max_length=50, unique=True)
          create_by = models.ForeignKey(Staff, on_delete=models.CASCADE)
          create_at = models.DateField(auto_now_add=True)
          update_by = models.CharField(max_length=50)
          update_at = models.DateField()
          status = models.BooleanField(default=True)
          def __str__(self):
                    return self.name
          
class Teacher(models.Model):
          firstname = models.CharField(max_length=50)
          lastname = models.CharField(max_length=50)
          gender = models.CharField(
          max_length=1,
          choices=(('M', 'Male'), ('F', 'Female')),
          default='O' 
          )
          dateofbirth = models.DateField()
          salary = models.DecimalField(max_digits=10, decimal_places=2)
          photo = models.ImageField(upload_to='media/', null=True, blank=True)
          create_at = models.DateTimeField(auto_now_add=True)
          create_by = models.ForeignKey(Staff, on_delete=models.CASCADE)
          update_at = models.DateTimeField()
          update_by = models.CharField(max_length=50)
          subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

          def __str__(self):
                    return f"{self.firstname} {self.lastname}"

        