from django.test import TestCase
from .models import Record

# Create your tests here.
# for x in len(Record.objects.all()):
#     print( Record.objects.all())
print( Record.objects.all().path)