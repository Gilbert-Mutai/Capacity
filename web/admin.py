from django.contrib import admin

# Register your models here.
from .models import Testimonial,Faqs,Contact

admin.site.register(Testimonial)
admin.site.register(Faqs)
admin.site.register(Contact)
