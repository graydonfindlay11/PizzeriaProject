import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE","learning_log.settings")

import django
django.setup()

from Pizzas.models import * 

pizzas = Pizza.objects.all()

'''
print(pizzas)
for p in pizzas:
    print(p)
    print(p.text)
    print(p.date_added)
'''

p = Pizza.objects.get(id=1)
print(p)

'''

'''