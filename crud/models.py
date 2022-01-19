from django.db import models

# Create your models here.
class DepartmentUUID(models.Model):
	uuidNumber = models.BigIntegerField(default=0)
	
def getDepartmentUUID():
	try:
		uuid = DepartmentUUID.objects.latest('uuidNumber')
	except Exception as e:
		uuid = DepartmentUUID()
		uuid.save()
	uuid.uuidNumber = uuid.uuidNumber+1
	uuid.save()
	getUUIDId = 'DeptId-'+ str(uuid.uuidNumber)
	return getUUIDId

class Department(models.Model):
    uId = models.CharField(default=getDepartmentUUID, max_length=10, unique=True)
    name = models.TextField(null=True,blank=True)
    def __str__(self):
        return self.uId

class Employee(models.Model):
    name = models.TextField(null=True,blank=True)
    email = models.TextField(null=True,blank=True)
    department = models.ForeignKey(Department,null=True,blank=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
