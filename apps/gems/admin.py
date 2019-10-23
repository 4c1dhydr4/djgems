from django.contrib import admin
from apps.gems.models import Gem, Configuration, GemProfile

admin.site.register(Gem)
admin.site.register(Configuration)
admin.site.register(GemProfile)