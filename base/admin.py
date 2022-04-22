from django.contrib import admin

from .models import CategoryVO, SubCategoryVO, ProductVO, AreaVO, UserVO, ComplainVO, FeedbackVO, LoginVO, ReplyVO

# Register your models here.
admin.site.register(AreaVO)
admin.site.register(CategoryVO)
admin.site.register(SubCategoryVO)
admin.site.register(ProductVO)
admin.site.register(UserVO)
admin.site.register(LoginVO)
admin.site.register(ComplainVO)
admin.site.register(FeedbackVO)
admin.site.register(ReplyVO)


