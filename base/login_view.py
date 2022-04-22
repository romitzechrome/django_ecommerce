import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import bcrypt
from django.contrib import messages
from django.forms import model_to_dict
from django.shortcuts import render, redirect

from base.models import LoginVO

global_loginvo_list = []
global_login_secretkey_set = {0}

def user_load_login(request):
    try:
        return render(request, 'user/login.html')
    except Exception as ex:
        print("user_load_login route exception occured>>>>>>>>>>", ex)
        return render(request, 'user/viewError.html', context={'message': ex})

def admin_validate_login(request):
    try:
        global global_loginvo_list
        global global_login_secretkey_set

        login_username = request.POST.get('loginUsername')
        login_password = request.POST.get('loginPassword').encode("utf-8")

        login_vo_list = LoginVO.objects.filter(login_username = login_username)
        login_dict = login_vo_list[0].__as_dict__()
        len_login_dict = len(login_dict)

        if len_login_dict == 0:
            error_message = 'username is incorrect !'
            messages.info(request, error_message)
            return redirect('/')

        elif not login_dict['login_status']:
            error_message = 'You have been temporarily blocked by website admin !'
            messages.info(request, error_message)
            return redirect('/')

        else:
            login_id = login_dict['login_id']
            login_username = login_dict['login_username']
            login_role = login_dict['login_role']
            login_secretkey = login_dict['login_secretkey']
            hashed_login_password = login_dict['login_password'].encode("utf-8")
            if bcrypt.checkpw(login_password, hashed_login_password):
                login_vo_dict = {
                    login_secretkey: {'login_username': login_username, 'login_role': login_role, 'login_id': login_id}}
                if len(global_loginvo_list) != 0:
                    for i in global_loginvo_list:
                        temp_list = list(i.keys())
                        global_login_secretkey_set.add(temp_list[0])
                    login_secretkey_list = list(global_login_secretkey_set)
                    if login_secretkey not in login_secretkey_list:
                        global_loginvo_list.append(login_vo_dict)
                else:
                    global_loginvo_list.append(login_vo_dict)

                if login_role == 'admin':
                    response = redirect(admin_load_dashboard)
                    response.set_cookie('login_secretkey', value=login_secretkey, max_age=1800)
                    response.set_cookie('login_username', value=login_username, max_age=1800)
                    return response

                elif login_role == 'user':
                    response = redirect(user_load_dashboard)
                    response.set_cookie('login_secretkey', value=login_secretkey, max_age=1800)
                    response.set_cookie('login_username', value=login_username, max_age=1800)
                    return response
                else:
                    return redirect(admin_logout_session)
            else:

                error_message = 'password is incorrect !'
                messages.info(request, error_message)
                return redirect('/')
    except Exception as ex:
        print("admin_validate_login route exception occured>>>>>>>>>>", ex)
        return render(request, 'user/viewError.html', context={'message': ex})

def admin_login_session(request):
    try:
        global global_loginvo_list
        login_role_flag = ""
        login_secretkey = request.COOKIES.get('login_secretkey')
        if login_secretkey is None:
            return redirect('/')
        for i in global_loginvo_list:
            if login_secretkey in i.keys():
                if i[login_secretkey]['login_role'] == 'admin':
                    login_role_flag = "admin"                   
                elif i[login_secretkey]['login_role'] == 'user':
                    login_role_flag = "user"
        return login_role_flag
    except Exception as ex:
        print("admin_login_session route exception occured>>>>>>>>>>", ex)
        return render(request, 'user/viewError.html', context={'message': ex})


def admin_load_dashboard(request):
    try:
        if admin_login_session(request) == "admin":
            return render(request, "admin/index.html")
        else:
            return admin_logout_session(request)
    except Exception as ex:
        print("in admin_load_dashboard function exception occured>>>>>", ex)
        return render(request, 'admin/viewError.html', context={'message': ex})


def user_load_dashboard(request):
    try:
        if admin_login_session(request) == "user":
            return render(request, "user/index.html")
        else:
            return admin_logout_session(request)
    except Exception as ex:
        print("in user_load_dashboard function exception occured>>>>>", ex)
        return render(request, 'user/viewError.html', context={'message': ex})


def admin_logout_session(request):
    try:
        global global_loginvo_list
        login_secretkey = request.COOKIES.get('login_secretkey')
        login_username = request.COOKIES.get('login_username')
        response = redirect('/')
        if login_secretkey is not None and login_username is not None:
            response.set_cookie('login_secretkey', login_secretkey, max_age=0)
            response.set_cookie('login_username', login_username, max_age=0)
            for i in global_loginvo_list:
                if login_secretkey in i.keys():
                    global_loginvo_list.remove(i)
                    break
        return response
    except Exception as ex:
        print("admin_logout_session route exception occured>>>>>>>>>>", ex)
        return render(request, 'user/viewError.html', context={'message': ex})


def admin_block_user(request):
    try:
        if admin_login_session(request) == 'admin':

            login_id = request.GET.get('loginId')
            login_vo = LoginVO.objects.get(login_id=login_id)
            login_vo.login_status = False
            login_vo.save()
            return redirect("/admin/view_user")
        else:
            return admin_logout_session(request)
    except Exception as ex:
        print("admin_block_user route exception occured>>>>>>>>>>", ex)
        return render(request, 'admin/viewError.html', context={'message': ex})


def admin_unblock_user(request):
    try:
        if admin_login_session(request) == 'admin':

            login_id = request.GET.get('loginId')
            login_vo = LoginVO.objects.get(login_id=login_id)
            login_vo.login_status = True
            login_vo.save()
            return redirect('/admin/view_user')
        else:
            return admin_logout_session(request)
    except Exception as ex:
        print("admin_unblock_user route exception occured>>>>>>>>>>", ex)
        return render(request, 'admin/viewError.html', context={'message': ex})


def user_load_forget_password(request):
    try:
        return render(request, 'user/forgetPassword.html')
    except Exception as ex:
        print("user_load_forget_password route exception occured>>>>>>>>>>", ex)
        return render(request, 'user/viewError.html', context={'message': ex})


def user_validate_login_username(request):
    try:
        login_username = request.POST.get("loginUsername")
        login_vo_list = LoginVO.objects.filter(login_username=login_username)
        login_list = [model_to_dict(i) for i in login_vo_list]
        len_login_list = len(login_list)
        if len_login_list == 0:
            error_message = 'username is incorrect !'
            messages.info(request, error_message)
            return redirect('/user/load_forget_password')
        else:
            login_id = login_list[0]['login_id']
            request.session['session_login_id'] = login_id
            login_username = login_list[0]['login_username']
            sender = "enter your email....."
            receiver = login_username
            msg = MIMEMultipart()
            msg['From'] = sender
            msg['To'] = receiver
            msg['Subject'] = "PYTHON OTP"
            otp = random.randint(1000, 9999)
            request.session['session_otp_number'] = otp
            message = str(otp)
            msg.attach(MIMEText(message, 'plain'))
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender, "qazwsxedcrfvtgb1234567890")
            text = msg.as_string()
            server.sendmail(sender, receiver, text)
            server.quit()
            return render(request, 'user/otpValidation.html')
    except Exception as ex:
        print("user_validate_login_username route exception occured>>>>>>>>>>", ex)
        return render(request, 'user/viewError.html', context={'message': ex})


def user_validate_otp_number(request):
    try:
        otp_number = int(request.POST.get("otpNumber"))
        session_otp_number = request.session.get('session_otp_number')
        if otp_number == session_otp_number:
            return render(request, 'user/resetPassword.html')
        else:
            request.session.flush()
            error_message = 'otp is incorrect !'
            messages.info(request, error_message)
            return redirect('/admin/load_forget_password')
    except Exception as ex:
        print("user_validate_otp_number route exception occured>>>>>>>>>>", ex)
        return render(request, 'user/viewError.html', context={'message': ex})


def user_insert_reset_password(request):
    try:
        login_password = request.POST.get("loginPassword")
        salt = bcrypt.gensalt(rounds=12)
        hashed_login_password = bcrypt.hashpw(login_password.encode("utf-8"), salt)
        login_id = request.session.get("session_login_id")
        login_vo = LoginVO.objects.get(login_id=login_id)
        login_vo.login_password = hashed_login_password
        login_vo.save()
        return redirect('/')
    except Exception as ex:
        print("user_insert_reset_password route exception occured>>>>>>>>>>", ex)
        return render(request, 'user/viewError.html', context={'message': ex})