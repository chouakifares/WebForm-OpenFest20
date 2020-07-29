from django.db import models
from django import forms
from django.core.validators import RegexValidator

# Create your models here.
BOOLEAN_CHOICES = [
    ("", "Select Option"),
    (1, u'Yes'),
    (0, u'No'),  
]

UNI_CHOICES = [
    ("", "Select Your University"),
    ("USTHB", "USTHB"),
    ("ENP", "ENP"),
    ("ENSTP", "ENSTP"),
    ("ESI", "ESI"),
    ("ESSA", "ESSA"),
    ('O', 'Other')
]

BRANCH_CHOICES=[
    ("", "Select Your Branch"),
    ("MI", "Mathematics and Computer Science"),
    ("SM", "Science of Matter"),
    ("ST", "Science and Technology"),
    ("SNV", "Science of Nature and Life"),
    ("STU", "Science of Earth and the Universe"),
    ('MATH', 'Mathematics'),
    ("FEI", "Electric Engineering and Computer Science"),
    ("PHY", "Physics"),
    ("CHI", "Chemistry"),
    ("GC", "Civil Engineering"),
    ("GM", "Mechanical Engineering"),
    ("GP", "Process Engineering"),
    ("BIO", "Biology"),
    ("EARTH", "Science of Earth"),
    ('GAT', 'Geography and Territorial Planning'),
    ('O', 'Other')
]

LVL_CHOICES=[
    ("", "Select Your Level"),
    ("L1", "Undergrad. deg. 1"),
    ("L2", "Undergrad. deg. 2"),
    ("L3", "Undergrad. deg. 3"),
    ("M1", "Master's deg. 1"),
    ("M2", "Master's deg. 2"),
    ('D', 'Doctorate deg.'),
    ('O', 'Other')
]

class Participant(models.Model):
    first_name = models.CharField(max_length=50,
        validators=[
            RegexValidator(
            regex=r'^[a-zA-Z]+(([\'\,\.\- ][a-zA-Z ])?[a-zA-Z]*)*$',
            message=("This is not a valid first name."),
            code='invalid_first_name')
        ]
    )
    last_name = models.CharField(max_length=30,
        validators=[
            RegexValidator(
            regex=r'^[a-zA-Z]+(([\'\,\.\- ][a-zA-Z ])?[a-zA-Z]*)*$',
            message=("This is not a valid last name."),
            code='invalid_last_name')
        ]
    )
    email = models.EmailField(primary_key=True)
    phone_number = models.CharField(max_length=10, 
        validators=[
            RegexValidator(
            regex=r'0[567][0-9]{8}',
            message=("This is not a valid phone number."),
            code='invalid_phone_number')
        ])
    university = models.CharField(max_length=5,choices=UNI_CHOICES, blank=False)
    branch = models.CharField(max_length=20,choices=BRANCH_CHOICES, blank=False)
    level = models.CharField(max_length=5,choices=LVL_CHOICES, blank=False)
    availability = models.BooleanField(choices=BOOLEAN_CHOICES, blank=False)
    experience = models.BooleanField(choices=BOOLEAN_CHOICES, blank=False)
    do_git = models.BooleanField(choices=BOOLEAN_CHOICES, blank=False)
    do_fest = models.BooleanField(choices=BOOLEAN_CHOICES, blank=False)
    conduct = models.BooleanField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name