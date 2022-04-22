import datetime

from django.shortcuts import render, redirect

from base.models import ComplainVO
from base.models import LoginVO
from base.models import ReplyVO
from .login_view import admin_login_session, admin_logout_session


def admin_view_complain(request):
    try:
        if admin_login_session(request) == "admin":
            complain_vo_list = ComplainVO.objects.raw('''SELECT * FROM complain_table ct INNER JOIN login_table lt ON
ct.complain_login_id =lt.login_id LEFT JOIN reply_table rt ON
rt.reply_complain_id=ct.complain_id''')
            return render(request, 'admin/viewComplain.html',
                          context={"complain_vo_list": complain_vo_list})
        else:
            return admin_logout_session(request)
    except Exception as ex:
        print("admin_view_complain route exception occured>>>>>>>>>>", ex)
        return render(request, 'admin/viewError.html', context={'message': ex})


def admin_load_complain_reply(request):
    try:
        if admin_login_session(request) == "admin":
            complain_id = request.GET.get('complainId')
            complain_vo_list = ComplainVO.objects.get(complain_id=complain_id)
            return render(request, 'admin/addReply.html', context={"complain_vo_list": complain_vo_list})
        else:
            return admin_logout_session(request)
    except Exception as ex:
        print("admin_load_reply_complain route exception occured>>>>>>>>>>", ex)
        return render(request, 'admin/viewError.html', context={'message': ex})


def admin_insert_complain_reply(request):
    try:
        if admin_login_session(request) == "admin":
            complain_id = request.POST.get('complainId')
            reply_description = request.POST.get('complainReplyDescription')
            login_username = request.COOKIES.get('login_username')

            reply_vo = ReplyVO()

            login_vo = LoginVO.objects.filter(login_username=login_username).first()
            complain_vo = ComplainVO.objects.get(complain_id=complain_id)
            complain_vo.complain_status = "Replied"
            complain_vo.complain_id = complain_id
            complain_vo.save()

            reply_vo.reply_datetime = datetime.datetime.now()
            reply_vo.reply_description = reply_description
            reply_vo.reply_complain_vo = complain_vo
            reply_vo.reply_login_vo = login_vo
            reply_vo.save()
            return redirect('/admin/view_complain')
        else:
            return admin_logout_session(request)
    except Exception as ex:
        print("admin_replied_complain_reply route exception occured>>>>>>>>>>", ex)
        return render(request, 'admin/viewError.html', context={'message': ex})


def admin_delete_complain(request):
    try:
        if admin_login_session(request) == "admin":
            complain_id = request.GET.get('complainId')
            complain_vo = ComplainVO.objects.get(complain_id=complain_id)
            complain_vo.delete()
            return redirect('/admin/view_complain')
        else:
            return admin_logout_session(request)
    except Exception as ex:
        print("admin_delete_complain route exception occured>>>>>>>>>>", ex)
        return render(request, 'admin/viewError.html', context={'message': ex})


def user_insert_complain(request):
    try:
        if admin_login_session(request) == "user":
            complain_subject = request.POST.get('complainSubject')
            complain_description = request.POST.get('complainDescription')
            complain_status = "Pending"
            login_username = request.COOKIES.get('login_username')

            login_vo = LoginVO.objects.filter(login_username=login_username).first()

            complain_vo = ComplainVO()
            complain_vo.complain_subject = complain_subject
            complain_vo.complain_description = complain_description
            complain_vo.complain_datetime = datetime.datetime.now()
            complain_vo.complain_status = complain_status
            complain_vo.complain_login_vo = login_vo
            complain_vo.save()
            return redirect('/user/view_complain')
        else:
            return admin_logout_session(request)
    except Exception as ex:
        print("user_insert_complain route exception occured>>>>>>>>>>", ex)
        return render(request, 'user/viewError.html', context={'message': ex})


def user_view_complain(request):
    try:
        if admin_login_session(request) == "user":

            login_username = request.COOKIES.get('login_username')
            login_vo = LoginVO.objects.filter(login_username=login_username).first()

            complain_vo_list = ComplainVO.objects \
                .select_related('complain_login_vo') \
                .filter(complain_login_vo=login_vo) \
                .all()
            reply_vo_list = ReplyVO.objects.select_related('reply_complain_vo').select_related('reply_login_vo').all()
            return render(request, "user/addComplain.html",
                          context={"complain_vo_list": complain_vo_list, "reply_vo_list": reply_vo_list})
        else:
            return admin_logout_session(request)
    except Exception as ex:
        print("user_view_complain route exception occured>>>>>>>>>>", ex)
        return render(request, 'user/viewError.html', context={'message': ex})

