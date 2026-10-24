# نموذج منير محمد نذير سنجاب - نموذج المليار
# طبقة تشغيل محلية؛ لا تدّعي تدريب أوزان النموذج على القرآن.

from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from quran_guard import protected_ask

print("منير محمد نذير سنجاب — نموذج المليار")
print("نموذج محلي تجريبي | الإجابات تحتاج إلى مراجعة بشرية")
print("اكتب خروج لإنهاء الجلسة.")

while True:
    try:
        question = input("\nسؤالك: ").strip()
        if question.lower() in {"خروج", "exit", "quit"}:
            print("انتهت الجلسة.")
            break
        if not question:
            continue

        prompt = (
            "أجب بالعربية بوضوح وبقدر السؤال. "
            "لا تختلق آيات أو مراجع. لا تضف تفسيرًا للقرآن. "
            "لا تغيّر النص القرآني. إذا لم يتوفر نص موثق، "
            "قل ذلك صراحة. افصل بين الحقيقة والفرضية والتأمل. "
            "لا تعتبر وجود وثيقة وحده دليلًا كافيًا على صحتها.\n"
            "السؤال: " + question
        )
        result = protected_ask(prompt, 128)
        answer = result.get("answer", "") if isinstance(result, dict) else str(result)
        answer = str(answer).strip()
        print("\nالإجابة التجريبية:")
        print(answer if answer else "لم ينتج جواب صالح للمراجعة.")
        print("\nالحالة: غير معتمدة حتى التحقق اليدوي.")
    except (KeyboardInterrupt, EOFError):
        print("\nانتهت الجلسة.")
        break
    except Exception as exc:
        print("تعذر إكمال الطلب:", type(exc).__name__, str(exc)[:250])
