from django.db import models


class AppUsers(models.Model):
    username = models.CharField(max_length=50, null=False, blank=False)
    number = models.CharField(max_length=70, null=False, blank=False)
    password = models.CharField(max_length=50, null=False, blank=False)
    type = models.CharField(max_length=50, null=False, blank=False)
    ngo = models.CharField(max_length=50, null=False, blank=False)
    active = models.BooleanField(default=True, null=False)
    created_by = models.CharField(max_length=30, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.username
    

class Posts(models.Model):
    projectName = models.CharField(max_length=50, null=False, blank=False)
    postedUser = models.CharField(max_length=50, null=False, blank=False)
    postedAt = models.CharField(max_length=50, null=False, blank=False)
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=False)
    image = models.TextField()
    ngo = models.CharField(max_length=40, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title
    

class Work(models.Model):
    username = models.CharField(max_length=50, null=False, blank=False)
    startDate = models.CharField(max_length=20, null=False, blank=False)
    startTime = models.CharField(max_length=20, null=False, blank=False)
    endDate = models.CharField(max_length=20, null=False, blank=True)
    endTime = models.CharField(max_length=20, null=False, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.startTime
    

class Projects(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField()
    coordinatorName = models.CharField(max_length=50, blank=False)
    ngo = models.CharField(max_length=40, null=True)
    password = models.CharField(max_length=50, blank=False)
    updated = models.DateTimeField(auto_now=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name
    
    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    

class ActivityImages(models.Model):
    image = models.ImageField()
    updated = models.DateTimeField(auto_now=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.created
    
    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    

class Amount(models.Model):
    projectName = models.CharField(max_length=100, blank=False)
    receivedAmount = models.CharField(max_length=60, blank=False)
    spentAmount = models.CharField(max_length=60, blank=False)
    remainingAmount = models.CharField(max_length=60, blank=False)
    reason = models.CharField(max_length=255, blank=False)
    time = models.CharField(max_length=20, null=False, blank=False)
    reimbursementamt = models.CharField(max_length=60, blank=True)
    ngo = models.CharField(max_length=40, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.receivedAmount
    

class Food(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    sponserName = models.CharField(max_length=50, null=False, blank=False)
    mobile = models.CharField(max_length=70, null=False, blank=False)
    preparation = models.CharField(max_length=50, null=False, blank=False)
    amount = models.CharField(max_length=255, null=False, blank=False)
    status = models.BooleanField(default=True, null=False)
    scheduled = models.CharField(max_length=50, null=False, blank=False)
    date = models.CharField(max_length=20, null=True, blank=False)
    paymentMethod = models.CharField(max_length=50, null=True)
    ngo = models.CharField(max_length=40, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.scheduled}"
    

class Donation(models.Model):
    sponserName = models.CharField(max_length=50, null=False, blank=False)
    mobile = models.CharField(max_length=70, null=False, blank=False)
    item = models.CharField(max_length=50, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    imagePath = models.CharField(max_length=20, null=True, blank=False)
    quantity = models.CharField(max_length=50, null=False, blank=False)
    ngo = models.CharField(max_length=40, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    month = models.CharField(max_length=20, null=True, blank=False)

    def __str__(self):
        return f"{self.name} {self.quantity}"