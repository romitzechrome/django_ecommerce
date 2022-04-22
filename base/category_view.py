from django.shortcuts import render, redirect

from .login_view import admin_login_session, admin_logout_session
from .models import CategoryVO

def admin_load_category(request):
    try:
        if admin_login_session(request) == "admin":
            return render(request, "admin/addCategory.html")
        else:
            return admin_logout_session(request)
    except Exception as ex:
        print("in admin_load_category function exception occured>>>>>", ex)
        return render(request, 'admin/viewError.html', context={'message': ex})

def admin_insert_category(request):
    try:
        if admin_login_session(request) == "admin":
            category_vo = CategoryVO()
            category_vo.category_name = request.POST.get('categoryName')
            category_vo.category_description = request.POST.get('categoryDescription')
            category_vo.save()
            return redirect('/admin/view_category')
        else:
            return admin_logout_session(request)
    except Exception as ex:
        print("in admin_insert_category function exception occured>>>>>", ex)
        return render(request, 'admin/viewError.html', context={'message': ex})


def admin_view_category(request):
    try:
        if admin_login_session(request) == "admin":
            category_vo_list = CategoryVO.objects.all()
            return render(request, 'admin/viewCategory.html', context={'category_vo_list': category_vo_list})
        else:
            return admin_logout_session(request)
    except Exception as ex:
        print("in admin_view_category function exception occured>>>>>", ex)
        return render(request, 'admin/viewError.html', context={'message': ex})


def admin_delete_category(request):
    try:
        if admin_login_session(request) == "admin":
            category_id = request.GET.get('categoryId')
            category_vo = CategoryVO.objects.get(category_id=category_id)
            category_vo.delete()
            return redirect("/admin/view_category")
        else:
            return admin_logout_session(request)
    except Exception as ex:
        print("in admin_delete_category function exception occured>>>>>", ex)
        return render(request, 'admin/viewError.html', context={'message': ex})


def admin_edit_category(request):
    try:
        if admin_login_session(request) == "admin":
            category_id = request.GET.get('categoryId')
            category_vo_list = CategoryVO.objects.filter(category_id=category_id)
            return render(request, "admin/editCategory.html", context={'category_vo_list': category_vo_list})
        else:
            return admin_logout_session(request)
    except Exception as ex:
        print("in admin_edit_category function exception occured>>>>>", ex)
        return render(request, 'admin/viewError.html', context={'message': ex})

def admin_update_category(request):
    try:
        if admin_login_session(request) == "admin":

            category_id = request.POST.get('categoryId')
            category_name = request.POST.get('categoryName')
            category_description = request.POST.get('categoryDescription')

            category_vo = CategoryVO.objects.get(category_id=category_id)

            category_vo.category_name = category_name
            category_vo.category_description = category_description
            category_vo.save()
            return redirect("/admin/view_category")
        else:
            return admin_logout_session(request)
    except Exception as ex:
        print("in admin_update_category function exception occured>>>>>", ex)
        return render(request, 'admin/viewError.html', context={'message': ex})




























