from django.urls import path

from . import category_view, subcategory_view, product_view, area_view, login_view, user_view, complain_view, \
    feedback_view

urlpatterns = [
    path('', login_view.user_load_login, name="admin_load_login"),
    path('admin/validate_login/', login_view.admin_validate_login, name="admin_validate_login"),
    path('admin/load_dashboard/', login_view.admin_load_dashboard, name="admin_load_dashboard"),
    path('user/load_dashboard/', login_view.user_load_dashboard, name="user_load_dashboard"),
    path('admin/logout_session/', login_view.admin_logout_session, name="admin_logout_session"),
    path('admin/block_user/', login_view.admin_block_user, name="admin_block_user"),
    path('admin/unblock_user/', login_view.admin_unblock_user, name="admin_unblock_user"),
    path('user/load_forget_password/', login_view.user_load_forget_password, name="user_load_forget_password"),
    path('user/validate_login_username/', login_view.user_validate_login_username, name="user_validate_login_username"),
    path('user/validate_otp_number/', login_view.user_validate_otp_number, name="user_validate_otp_number"),
    path('user/insert_reset_password/', login_view.user_insert_reset_password, name="user_insert_reset_password"),

    path('admin/load_area/', area_view.admin_load_area, name="admin_load_area"),
    path('admin/insert_area/', area_view.admin_insert_area, name="admin_insert_area"),
    path('admin/view_area/', area_view.admin_view_area, name="admin_view_area"),
    path('admin/delete_area/', area_view.admin_delete_area, name="admin_delete_area"),
    path('admin/edit_area/', area_view.admin_edit_area, name="admin_edit_area"),
    path('admin/update_area/', area_view.admin_update_area, name="admin_update_area"),

    path('admin/load_category/', category_view.admin_load_category, name="admin_load_category"),
    path('admin/insert_category/', category_view.admin_insert_category, name="admin_insert_category"),
    path('admin/view_category/', category_view.admin_view_category, name="admin_view_category"),
    path('admin/delete_category/', category_view.admin_delete_category, name="admin_delete_category"),
    path('admin/edit_category/', category_view.admin_edit_category, name="admin_edit_category"),
    path('admin/update_category/', category_view.admin_update_category, name="admin_update_category"),

    path('admin/load_subcategory/', subcategory_view.admin_load_subcategory, name="admin_load_subcategory"),
    path('admin/insert_subcategory/', subcategory_view.admin_insert_subcategory, name="admin_insert_subcategory"),
    path('admin/view_subcategory/', subcategory_view.admin_view_subcategory, name="admin_view_subcategory"),
    path('admin/delete_subcategory/', subcategory_view.admin_delete_subcategory, name="admin_delete_subcategory"),
    path('admin/edit_subcategory/', subcategory_view.admin_edit_subcategory, name="admin_edit_subcategory"),
    path('admin/update_subcategory/', subcategory_view.admin_update_subcategory, name="admin_update_subcategory"),

    path('admin/load_product/', product_view.admin_load_product, name="admin_load_product"),
    path('admin/ajax_subcategory_product/', product_view.admin_ajax_subcategory_product,
         name="admin_ajax_subcategory_product"),
    path('admin/insert_product/', product_view.admin_insert_product, name="admin_insert_product"),
    path('admin/view_product/', product_view.admin_view_product, name="admin_view_product"),
    path('admin/delete_product/', product_view.admin_delete_product, name="admin_delete_product"),
    path('admin/edit_product_data/', product_view.admin_edit_product_data, name="admin_edit_product_data"),
    path('admin/update_product_data/', product_view.admin_update_product_data, name="admin_update_product_data"),
    path('admin/edit_product_image/', product_view.admin_edit_product_image, name="admin_edit_product_image"),
    path('admin/update_product_image/', product_view.admin_update_product_image, name="admin_update_product_image"),

    path('admin/view_user/', user_view.admin_view_user, name="admin_view_user"),
    path('user/insert_user/', user_view.user_insert_user, name="user_insert_user"),
    path('user/load_user/', user_view.user_load_user, name="user_load_user"),

    path('admin/view_complain/', complain_view.admin_view_complain, name="admin_view_complain"),
    path('admin/load_complain_reply/', complain_view.admin_load_complain_reply, name="admin_load_complain_reply"),
    path('admin/insert_complain_reply/', complain_view.admin_insert_complain_reply, name="admin_insert_complain_reply"),
    path('admin/delete_complain/', complain_view.admin_delete_complain, name="admin_delete_complain"),
    path('user/insert_complain/', complain_view.user_insert_complain, name="user_insert_complain"),
    path('user/view_complain/', complain_view.user_view_complain, name="user_view_complain"),

    path('admin/view_feedback/', feedback_view.admin_view_feedback, name="admin_view_feedback"),
    path('admin/delete_feedback/', feedback_view.admin_delete_feedback, name="admin_delete_feedback"),
    path('user/insert_feedback/', feedback_view.user_insert_feedback, name="user_insert_feedback"),
    path('user/view_feedback/', feedback_view.user_view_feedback, name="user_view_feedback"),

]