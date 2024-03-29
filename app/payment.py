from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import razorpay
from codeshetra import settings
from django.views.decorators.csrf import csrf_exempt
from .models import UserProfile, credit
# from razorpay.utility import verify_payment_signature

client = razorpay.Client(auth=(settings.AUTH, settings.KEY))



@login_required
def price(request):
    return render(request, 'pricing.html')

@login_required
def starter(request):
    amount = 199
    if request.method == "POST":
        new_order_response = client.order.create({
                        "amount": amount*100,
                        "currency": "INR",
                        "payment_capture": "1"
                      })
        print (new_order_response)
        # return redirect("callback")



    return render(request, 'starter.html')

@login_required
def pro(request):
    amount = 599
    if request.method == "POST":
        new_order_response = client.order.create({
                        "amount": amount*100,
                        "currency": "INR",
                        "payment_capture": "1"
                      })
        print (new_order_response)
    return render(request, 'pro.html')

@login_required
def master(request):
    amount = 999
    if request.method == "POST":
        new_order_response = client.order.create({
                        "amount": amount*100,
                        "currency": "INR",
                        "payment_capture": "1"
                      })
        print (new_order_response)
    return render(request, 'master.html')

@csrf_exempt
def success(request):
    return render(request, 'success.html')

@login_required
def order_callback1(request):
    print(request.POST)
    if request.method == "POST":
        # razorpay_order_id = request.POST.get('razorpay_order_id')
        razorpay_payment_id = request.POST.get('razorpay_payment_id')
        # razorpay_signature = request.POST.get('razorpay_signature')

        # if razorpay_order_id and razorpay_payment_id and razorpay_signature:
        if razorpay_payment_id:
            # payment_verification = client.utility.verify_payment_signature(razorpay_payment_id, razorpay_order_id, razorpay_signature)
            # if payment_verification:
                # client.utility.verify_payment_signature(request.POST)
            # if payment_verification:
                user = request.user
                try:
                    profile = credit.objects.get(user=request.user)
                    profile.credit += 1
                    profile.save()
                    print("Credit added")
                except credit.DoesNotExist:
                    profile = credit.objects.create(user=request.user, credit=1)
                    print("Credit created")

                try:
                    user_profile = UserProfile.objects.get(user=request.user)
                    user_profile.is_student = True
                    user_profile.is_teacher = False
                    user_profile.save()
                    print("User profile updated")
                except UserProfile.DoesNotExist:
                    UserProfile.objects.create(user=request.user, is_student=True, is_teacher=False)
                    print("User profile created")
            # else:
            #     return redirect("price")

    return redirect("success")

@login_required
def order_callback2(request):
    print(request.POST)
    if request.method == "POST":
        # razorpay_order_id = request.POST.get('razorpay_order_id')
        razorpay_payment_id = request.POST.get('razorpay_payment_id')
        # razorpay_signature = request.POST.get('razorpay_signature')

        # if razorpay_order_id and razorpay_payment_id and razorpay_signature:
        if razorpay_payment_id:
            # payment_verification = client.utility.verify_payment_signature(razorpay_payment_id, razorpay_order_id, razorpay_signature)
            # if payment_verification:
                # client.utility.verify_payment_signature(request.POST)
            # if payment_verification:
                user = request.user
                try:
                    profile = credit.objects.get(user=request.user)
                    profile.credit += 5
                    profile.save()
                    print("Credit added")
                except credit.DoesNotExist:
                    profile = credit.objects.create(user=request.user, credit=5)
                    print("Credit created")

                try:
                    user_profile = UserProfile.objects.get(user=request.user)
                    user_profile.is_student = True
                    user_profile.is_teacher = False
                    user_profile.save()
                    print("User profile updated")
                except UserProfile.DoesNotExist:
                    UserProfile.objects.create(user=request.user, is_student=True, is_teacher=False)
                    print("User profile created")
            # else:
            #     return redirect("price")

    return redirect("success")

@login_required
def order_callback3(request):
    print(request.POST)
    if request.method == "POST":
        # razorpay_order_id = request.POST.get('razorpay_order_id')
        razorpay_payment_id = request.POST.get('razorpay_payment_id')
        # razorpay_signature = request.POST.get('razorpay_signature')

        # if razorpay_order_id and razorpay_payment_id and razorpay_signature:
        if razorpay_payment_id:
            # payment_verification = client.utility.verify_payment_signature(razorpay_payment_id, razorpay_order_id, razorpay_signature)
            # if payment_verification:
                # client.utility.verify_payment_signature(request.POST)
            # if payment_verification:
                user = request.user
                try:
                    profile = credit.objects.get(user=request.user)
                    profile.credit += 10
                    profile.save()
                    print("Credit added")
                except credit.DoesNotExist:
                    profile = credit.objects.create(user=request.user, credit=10)
                    print("Credit created")

                try:
                    user_profile = UserProfile.objects.get(user=request.user)
                    user_profile.is_student = True
                    user_profile.is_teacher = False
                    user_profile.save()
                    print("User profile updated")
                except UserProfile.DoesNotExist:
                    UserProfile.objects.create(user=request.user, is_student=True, is_teacher=False)
                    print("User profile created")
            # else:
            #     return redirect("price")

    return redirect("success")
                