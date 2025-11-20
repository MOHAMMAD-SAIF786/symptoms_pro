from django.contrib import admin
from .models import Contact,ContactForm,Feature,Working,Discliamer

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display =('title','email')
admin.site.register(Contact,ContactAdmin)
 
class ContactFormAdmin(admin.ModelAdmin):
   list_display=('name','email','phone','message')
admin.site.register(ContactForm,ContactFormAdmin)

class FeatureAdmin(admin.ModelAdmin):
    list_display=('title','feature_button')
admin.site.register(Feature,FeatureAdmin)

class WorkingAdmin(admin.ModelAdmin):
    list_display=('title','steps')
admin.site.register(Working,WorkingAdmin)

class DiscliamerAdmin(admin.ModelAdmin):
    list_display=('important_disclaimer','footer')
admin.site.register(Discliamer,DiscliamerAdmin)

