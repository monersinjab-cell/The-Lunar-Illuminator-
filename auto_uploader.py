import os
import subprocess

# 1. ضع بيانات مستودعك والرمز السري هنا بأمان
GITHUB_USERNAME = "monersinjab-cell"
REPOSITORY_NAME = "The-Lunar-Illuminator-"
# استبدل النص أدناه برمز الـ Token الخاص بك الذي استخرجته من إعدادات GitHub
GITHUB_TOKEN = "ضع_هنا_رمز_الـ_TOKEN_الخاص_بِك"

# بناء الرابط الآمن المشفر للرفع تلقائياً
REMOTE_URL = f"https://{GITHUB_USERNAME}:{GITHUB_TOKEN}@://github.com{GITHUB_USERNAME}/{REPOSITORY_NAME}.git"

def run_git_command(command, description):
    try:
        print(f"[+] جاري تنفيذ: {description}...")
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"[-] خطأ أثناء {description}: {e.stderr}")
        return False

def main():
    # التأكد من أن المجلد مهيأ كـ Git
    if not os.path.exists(".git"):
        run_git_command(["git", "init"], "تهيئة مستودع Git محلي")
        run_git_command(["git", "branch", "-M", "main"], "تسمية الفرع الرئيسي بـ main")
    
    # تحديث أو إضافة رابط الرفع المشفر
    subprocess.run(["git", "remote", "remove", "origin"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    run_git_command(["git", "remote", "add", "origin", REMOTE_URL], "ربط المجلد بالمستودع عبر الرابط الآمن")

    # خطوات الرفع الثلاثية تلقائياً
    if run_git_command(["git", "add", "."], "تجهيز وتجميع كافة الملفات والمجلدات غير المضغوطة"):
        if run_git_command(["git", "commit", "-m", "تحديث تلقائي للمستودع وتنسيق الملفات المفتوحة"], "تثبيت التعديلات"):
            print("[+] جاري بدء الرفع ونقل البيانات إلى GitHub، يرجى الانتظار...")
            if run_git_command(["git", "push", "-u", "origin", "main"], "إرسال الملفات إلى GitHub"):
                print("\n🎉 تم بنجاح! تم رفع كافة الأكواد والملفات إلى مستودعك مباشرة دون ضغط.")

if __name__ == "__main__":
    main()
