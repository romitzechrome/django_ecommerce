from django.db import models


class AreaVO(models.Model):
    area_id = models.AutoField(db_column="area_id", primary_key=True, null=False)
    area_name = models.CharField(db_column="area_name", max_length=255, default="", null=False)
    area_pincode = models.TextField(db_column="area_pincode", max_length=255, default="", null=False)

    def __str__(self):
        return '{} {}'.format(self.area_name, self.area_pincode)

    def __as_dict__(self):
        return {
            "area_id": self.area_id,
            "area_name": self.area_name,
            "area_pincode": self.area_pincode
        }

    class Meta:
        db_table = "area_table"


class CategoryVO(models.Model):
    category_id = models.AutoField(db_column="category_id", primary_key=True, null=False)
    category_name = models.CharField(db_column="category_name", max_length=255, default="", null=False)
    category_description = models.TextField(db_column="category_description", max_length=255, default="", null=False)

    def __str__(self):
        return '{} {}'.format(self.category_name, self.category_description)

    def __as_dict__(self):
        return {
            "category_id": self.category_id,
            "category_name": self.category_name,
            "category_description": self.category_description
        }

    class Meta:
        db_table = "category_table"


class SubCategoryVO(models.Model):
    subcategory_id = models.AutoField(db_column="subcategory_id", primary_key=True, null=False)
    subcategory_name = models.CharField(db_column="subcategory_name", max_length=255, default="", null=False)
    subcategory_description = models.TextField(db_column="subcategory_description", max_length=255, default="",
                                               null=False)
    subcategory_category_vo = models.ForeignKey(CategoryVO, on_delete=models.CASCADE,
                                                db_column="subcategory_category_id")

    def __str__(self):
        return '{} {}'.format(self.subcategory_name, self.subcategory_description)

    def __as_dict__(self):
        return {
            "subcategory_id": self.subcategory_id,
            "subcategory_name": self.subcategory_name,
            "subcategory_description": self.subcategory_description,
            "subcategory_category_vo": self.subcategory_category_vo,
        }

    class Meta:
        db_table = "subcategory_table"

class ProductVO(models.Model):
    product_id = models.AutoField(db_column="product_id", primary_key=True, null=False)
    product_name = models.CharField(db_column="product_name", max_length=50, default="", null=False)
    product_description = models.TextField(db_column="product_description", max_length=500, default="", null=False)
    product_quantity = models.IntegerField(db_column="product_quantity", null=False)
    product_price = models.IntegerField(db_column="product_price", null=False)
    product_image = models.ImageField(upload_to='static/adminResources/product/', db_column="product_image")
    product_category_vo = models.ForeignKey(CategoryVO, on_delete=models.CASCADE, db_column="product_category_id")
    product_subcategory_vo = models.ForeignKey(SubCategoryVO, on_delete=models.CASCADE,
                                               db_column="product_subcategory_id", )


    def __str__(self):
        return '{} {} {} {}'.format(self.product_name, self.product_description, self.product_quantity,
                                    self.product_price)

    def __as_dict__(self):
        return {
            "product_id": self.product_id,
            "product_name": self.product_name,
            "product_description": self.product_description,
            "product_quantity": self.product_quantity,
            "product_price": self.product_price,
            "product_image": self.product_image,
            "product_category_vo": self.product_category_vo,
            "product_subcategory_vo": self.product_subcategory_vo,
        }

    class Meta:
        db_table = "product_table"


class LoginVO(models.Model):
    login_id = models.AutoField(db_column="login_id", primary_key=True, null=False)
    login_username = models.CharField(db_column="login_username", max_length=200, default="", null=False)
    login_password = models.CharField(db_column="login_password", max_length=200, default="", null=False)
    login_role = models.CharField(db_column="login_role", max_length=10, default="", null=False)
    login_secretkey = models.CharField(db_column="login_secretkey", max_length=200, default="", null=False)
    login_status = models.BooleanField(db_column="login_status", max_length=1, default="", null=False)

    def __str__(self):
        return '{} {} {} {}'.format(self.login_username, self.login_password, self.login_role,
                                    self.login_secretkey)

    def __as_dict__(self):
        return {
            "login_id": self.login_id,
            "login_username": self.login_username,
            "login_password": self.login_password,
            "login_role": self.login_role,
            "login_secretkey": self.login_secretkey,
            "login_status": self.login_status
        }

    class Meta:
        db_table = "login_table"


class UserVO(models.Model):
    user_id = models.AutoField(db_column="user_id", primary_key=True, null=False)
    user_firstname = models.CharField(db_column="user_firstname", max_length=200, default="", null=False)
    user_lastname = models.CharField(db_column="user_lastname", max_length=200, default="", null=False)
    user_gender = models.CharField(db_column="user_gender", max_length=10, default="", null=False)
    user_address = models.CharField(db_column="user_address", max_length=500, default="", null=False)
    user_hobby = models.CharField(db_column="user_hobby", max_length=50, default="", null=False)
    user_login_vo = models.ForeignKey(LoginVO, on_delete=models.CASCADE,
                                      db_column="user_login_id")
    user_area_vo = models.ForeignKey(AreaVO, on_delete=models.CASCADE,
                                     db_column="user_area_id")

    def __str__(self):
        return '{} {} {} {} {}'.format(self.user_firstname, self.user_lastname, self.user_gender,
                                       self.user_address, self.user_hobby)

    def __as_dict__(self):
        return {
            "user_id": self.user_id,
            "user_firstname": self.user_firstname,
            "user_lastname": self.user_lastname,
            "user_gender": self.user_gender,
            "user_address": self.user_address,
            "user_hobby": self.user_hobby,
            "user_login_vo": self.user_login_vo,
            "user_area_vo": self.user_area_vo
        }

    class Meta:
        db_table = "user_table"


class ComplainVO(models.Model):
    complain_id = models.AutoField(db_column="complain_id", primary_key=True, null=False)
    complain_subject = models.CharField(db_column="complain_subject", max_length=255, default="", null=False)
    complain_description = models.TextField(db_column="complain_description", max_length=500, default="", null=False)
    complain_datetime = models.DateTimeField(db_column="complain_datetime", null=False)
    complain_status = models.CharField(db_column="complain_status", max_length=255, default="", null=False)
    complain_login_vo = models.ForeignKey(LoginVO, db_column="complain_login_id", on_delete=models.CASCADE, null=False)

    def __str__(self):
        return '{} {} {} {}'.format(self.complain_subject, self.complain_description, self.complain_datetime,
                                    self.complain_status)

    def __as_dict__(self):
        return {
            "complain_id": self.complain_id,
            "complain_subject": self.complain_subject,
            "complain_description": self.complain_description,
            "complain_datetime": self.complain_datetime,
            "complain_status": self.complain_status,
            "complain_login_vo": self.complain_login_vo
        }

    class Meta:
        db_table = "complain_table"


class ReplyVO(models.Model):
    __tablename__ = "reply_table"
    reply_id = models.AutoField("reply_id", primary_key=True, null=False)
    reply_description = models.TextField("reply_description", max_length=500, default="", null=False)
    reply_datetime = models.DateTimeField("reply_datetime", null=False)
    reply_complain_vo = models.ForeignKey(ComplainVO, db_column="reply_complain_id", on_delete=models.CASCADE,
                                          null=False)
    reply_login_vo = models.ForeignKey(LoginVO, db_column="reply_login_id", on_delete=models.CASCADE, null=False)

    def as_dict(self):
        return {
            "reply_id": self.reply_id,
            "reply_description": self.reply_description,
            "reply_datetime": self.reply_datetime,
            "reply_complain_vo": self.reply_complain_vo,
            "reply_login_vo": self.reply_login_vo
        }

    class Meta:
        db_table = "reply_table"


class FeedbackVO(models.Model):
    feedback_id = models.AutoField(db_column="feedback_id", primary_key=True, null=False)
    feedback_description = models.TextField(db_column="feedback_description", max_length=500, default="", null=False)
    feedback_datetime = models.DateTimeField(db_column="feedback_datetime", null=False)
    feedback_rating = models.IntegerField(db_column="feedback_rating", null=False)
    feedback_login_vo = models.ForeignKey(LoginVO, db_column="feedback_login_id", on_delete=models.CASCADE, null=False)

    def __str__(self):
        return '{} {} {}'.format(self.feedback_description, self.feedback_datetime, self.feedback_rating)

    def __as_dict__(self):
        return {
            "feedback_id": self.feedback_id,
            "feedback_description": self.feedback_description,
            "feedback_datetime": self.feedback_datetime,
            "feedback_rating": self.feedback_rating,
            "feedback_login_vo": self.feedback_login_vo
        }

    class Meta:
        db_table = "feedback_table"