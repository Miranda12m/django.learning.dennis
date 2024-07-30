from django.contrib import admin
from django.apps import apps

app = apps.get_app_config('users')

# Exclude models
exlude_models = ['']

for model in app.get_models():
    if model.__name__ not in exlude_models:
        admin.site.register(model)

