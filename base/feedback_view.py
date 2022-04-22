import datetime

from django.shortcuts import render, redirect

from base.models import LoginVO, FeedbackVO
from .login_view import admin_login_session, admin_logout_session


def admin_view_feedback(request):
    try:
        if admin_login_session(request) == "admin":
            feedback_vo_list = FeedbackVO.objects.select_related("feedback_login_vo").all()
            return render(request, 'admin/viewFeedback.html',
                          context={"feedback_vo_list": feedback_vo_list})
        else:
            return admin_logout_session(request)
    except Exception as ex:
        print("admin_view_feedback route exception occured>>>>>>>>>>", ex)
        return render(request, 'admin/viewError.html', context={'message': ex})


def admin_delete_feedback(request):
    try:
        if admin_login_session(request) == "admin":
            feeback_id = request.GET.get('feebackId')
            feedback_vo = FeedbackVO.objects.get(feeback_id=feeback_id)
            feedback_vo.delete()
            return redirect('/admin/view_feedback')
        else:
            return admin_logout_session(request)
    except Exception as ex:
        print("admin_delete_feedback route exception occured>>>>>>>>>>", ex)
        return render(request, 'admin/viewError.html', context={'message': ex})


def user_insert_feedback(request):
    try:
        if admin_login_session(request) == "user":
            feedback_description = request.POST.get('feedbackDescription')
            feedback_rating = request.POST.get('feedbackRating')
            login_username = request.COOKIES.get('login_username')

            login_vo = LoginVO.objects.filter(login_username=login_username).first()

            feedback_vo = FeedbackVO()
            feedback_vo.feedback_description = feedback_description
            feedback_vo.feedback_rating = feedback_rating
            feedback_vo.feedback_datetime = datetime.datetime.now()
            feedback_vo.feedback_login_vo = login_vo
            feedback_vo.save()
            return redirect('/user/view_feedback')
        else:
            return admin_logout_session(request)
    except Exception as ex:
        print("user_insert_feedback route exception occured>>>>>>>>>>", ex)
        return render(request, 'user/viewError.html', context={'message': ex})


def user_view_feedback(request):
    try:
        if admin_login_session(request) == "user":

            login_username = request.COOKIES.get('login_username')
            login_vo = LoginVO.objects.filter(login_username=login_username).first()

            feedback_vo_list = FeedbackVO.objects \
                .select_related('feedback_login_vo') \
                .filter(feedback_login_vo=login_vo) \
                .all()
            return render(request, "user/addFeedback.html",
                          context={"feedback_vo_list": feedback_vo_list})
        else:
            return admin_logout_session(request)
    except Exception as ex:
        print("user_view_feedback route exception occured>>>>>>>>>>", ex)
        return render(request, 'user/viewError.html', context={'message': ex})