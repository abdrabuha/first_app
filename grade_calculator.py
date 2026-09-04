"""
grade_calculator.py
===================
حاسبة الدرجات — Grade Calculator (بالعربية والإنجليزية / in Arabic & English)

تطبيق تعليمي بسيط يحسب متوسط درجات الطالب وتقديره الحرفي.
نفس الفكرة معروضة بشكل تفاعلي داخل المتصفح في index.html.

A simple educational app that computes a student's average and letter grade.
The same idea is shown interactively in the browser inside index.html.

الاستخدام / Usage:
    python grade_calculator.py            # بالعربية / in Arabic
    python grade_calculator.py en         # بالإنجليزية / in English
"""

import sys

# اجعل الطباعة العربية تعمل على أي وسم (UTF-8) / make Arabic printing work on any console
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

# ---------- منطق الحساب (نفسه في أي لغة) ----------
# ---------- The calculation logic (identical in any language) ----------


def calculate_average(grades):
    """احسب المتوسط = مجموع الدرجات ÷ عددها.
    Return the average = sum of grades / count."""
    return sum(grades) / len(grades)


def determine_letter_grade(average):
    """حوّل المتوسط إلى تقدير حرفي حسب الجدول.
    Map the average to a letter grade using the table."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "Fail"


# ---------- العرض ----------
# ---------- Display ----------

def main():
    # اختيار اللغة من سطر الأوامر / choose language from command line
    lang = sys.argv[1] if len(sys.argv) > 1 else "ar"
    english = lang.lower() in ("en", "english")

    students = ["Ahmad", "Bader", "Huda", "Mohammed"]
    grades = [[85, 78, 92], [76, 88, 90], [90, 95, 93], [52, 59, 50]]

    if english:
        print("=" * 46)
        print(" GRADE CALCULATOR (sample data)")
        print("=" * 46)
    else:
        print("=" * 46)
        print(" حاسبة الدرجات (بيانات تجريبية)")
        print("=" * 46)

    for name, row in zip(students, grades):
        average = calculate_average(row)
        letter = determine_letter_grade(average)
        if english:
            print(f"{name:10s} Average = {average:5.2f}  Letter = {letter}")
        else:
            print(f"{name:10s} المتوسط = {average:5.2f}  التقدير = {letter}")

    print("=" * 46)


if __name__ == "__main__":
    main()
