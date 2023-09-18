from django.contrib import admin
from .models import Category, BannerSlider, Employee ,Department, CardInfo
from .models import SignUp

# Register your models here.

admin.site.register(Category)
admin.site.register(BannerSlider)
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(CardInfo)
admin.site.register(SignUp)



