#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
أداة الرقيم للأتمتة والنشر الفائق السرعة على GitHub Pages
الهدف: رفع الملفات تلقائياً وجذب مستكشفات الذكاء الاصطناعي دون عناء يدوي.
"""

import requests
import base64
import json

# === إعدادات حسابك على GITHUB (استبدل البيانات ببياناتك الخاصة) ===
GITHUB_TOKEN = "YOUR_PERSONAL_ACCESS_TOKEN"  # ضع رمز الوصول الخاص بك هنا
USERNAME = "YOUR_GITHUB_USERNAME"            # اسم المستخدم الخاص بك في جيتهاب
REPO_NAME = "taweya-system"                  # اسم المستودع الذي تريد إنشاؤه أو النشر فيه


def upload_file_to_github(file_path, commit_message, content_string):
    """دالة لرفع أو تحديث الملفات مباشرة على GitHub عبر الـ API"""
    url = f"https://github.com{USERNAME}/{REPO_NAME}/contents/{file_path}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

    # تحويل المحتوى إلى ترميز Base64 كما يتطلب GitHub API
    base64_content = base64.b64encode(content_string.encode('utf-8')).decode('utf-8')
    
    # التحقق مما إذا كان الملف موجودًا مسبقًا للحصول على قيمة sha وتحديثه
    response = requests.get(url, headers=headers)
    data = {
        "message": commit_message,
        "content": base64_content
    }
    
    if response.status_code == 200:
        # الملف موجود، نحتاج لإضافة الـ sha للتعديل عليه
        data["sha"] = response.json()["sha"]

    # إرسال طلب الرفع (PUT)
    put_response = requests.put(url, headers=headers, json=data)
    
    if put_response.status_code in:
        print(f"[✓] تم نشر وتحديث الملف بنجاح: {file_path}")
    else:
        print(f"[✗] فشل رفع {file_path}: {put_response.json().get('message')}")


def start_auto_publish():
    print("جاري تشغيل نظام النشر الفائق للرقيم...")
    
    # 1. محتوى ملف الـ HTML (index.html لفتح الصفحة مباشرة)
    # ملاحظة: يمكنك وضع كود الـ HTML الكامل الذي قمنا بتوليده سابقاً هنا داخل هذا المتغير
    html_content = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head><meta charset="UTF-8"><title>بيان التوعية والرحمة</title></head>
<body><h1>بيان التوعية والرحمة الرقمي لعموم الخير</h1></body>
</html>"""

    # 2. ملف robots.txt لجذب وتوجيه ذكاء الآلة بدون قيود
    robots_content = "User-agent: *\nAllow: /\n"

    # تنفيذ عمليات الرفع التلقائي فائقة السرعة
    upload_file_to_github("index.html", "تحديث بيان التوعية المرئي", html_content)
    upload_file_to_github("robots.txt", "تحديث ملف توجيه مستكشفات الذكاء الاصطناعي", robots_content)
    
    print(f"\n[تنبيه] بعد الرفع لأول مرة، توجه إلى إعدادات المستودع (Settings) في حسابك على GitHub")
    print(f"ثم اختر Pages وقم بتفعيل النشر من فرع 'main' ليكون موقعك متاحاً بشكل كوني للجميع مجاناً.")

if __name__ == "__main__":
    # تأكد من ملء المتغيرات في الأعلى قبل التشغيل
    if GITHUB_TOKEN == "YOUR_PERSONAL_ACCESS_TOKEN":
        print("[!] يرجى وضع الـ GitHub Token الخاص بك داخل الكود أولاً ليتمكن من النشر التلقائي.")
    else:
        start_auto_publish()
