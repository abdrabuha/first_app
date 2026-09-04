# 🎓 First App — تعلّم بالعربي والإنجليزي · Learn in Arabic & English

> **The Why:** هذا أول تطبيق تعليمي تفاعلي لك — يحوّل درسك الأصلي عن Git و GitHub و VS Code إلى تجربة ويب ثنائية اللغة (عربي/إنجليزي) مع اختبار تفاعلي وحاسبة درجات، ليتعلم المبتدئ بنفس الفكرة من اللغتين.
>
> **The Why (EN):** your first interactive educational app — it upgrades your original Git / GitHub / VS Code lesson into a bilingual (AR/EN) web experience with a quiz and a grade calculator, so beginners learn the same idea in both languages.

---

## 🚀 طريقة التشغيل · How to run

**🌐 جرّبه مباشرة · Try it live:** [abdrabuha.github.io/first_app](https://abdrabuha.github.io/first_app/)

**الويب / Web** — افتح `index.html` مباشرة في أي متصفح (بدون إنترنت أو سيرفر):
```bash
start index.html
```

**البايثون / Python**:
```bash
python grade_calculator.py        # بالعربية / in Arabic
python grade_calculator.py en     # بالإنجليزية / in English
```

## 🧩 ماذا ستتعلم من هذا المشروع؟ · What you will learn

1. **Git vs GitHub vs VS Code** — الفرق بين التتبّع المحلي والاستضافة السحابية والمحرر
2. **الأوامر الأساسية** — `init`, `add`, `commit`, `push`, `log`
3. **ترجمة الأفكار بين اللغات** — نفس منطق بايثون يتحول لجافاسكريبت
4. **أساسيات الويب ثنائي اللغة** — `dir="rtl/ltr"`, تبادل النصوص، و `localStorage`

## 📁 بنية المشروع · Project structure

```text
first_app/
├── index.html            ← التطبيق التعليمي التفاعلي (عربي/إنجليزي)
├── grade_calculator.py   ← نفس حاسبة الدرجات بلغة بايثون (ثنائية اللغة)
└── README.md
```

## 📸 لقطات سريعة · Quick preview

```text
[ 📖 الدرس ]  [ ❓ اختبر نفسك ]  [ 🧮 حاسبة الدرجات ]
     ↑ زر اللغة: عربي / English يقلب الصفحة كلها RTL ⇄ LTR
```

## 💛 Support the Author / دعم المؤلف

> **العربية:** إذا أردت دعمي، فنشكرك ونقدّر لك ذلك بصدق. ❤️ يمكنك إرسال الدعم عبر العناوين التالية.
>
> **English:** If you want to support me, we thank and appreciate that. ❤️ You can send a donation using the addresses below.

| العملة / Coin | العنوان / Address |
|---|---|
| Bitcoin (BTC) | _يُضاف لاحقاً · to be added_ |
| Ethereum (ETH) | _يُضاف لاحقاً · to be added_ |
| Solana (SOL) | _يُضاف لاحقاً · to be added_ |
| USDT | _يُضاف لاحقاً · to be added_ |
| USDC | _يُضاف لاحقاً · to be added_ |

---

## ©️ الحقوق والترخيص · Copyright & License

**المؤلف / Author:** عبدربه العتيبي (Abdrabuh Alotaibi) · [abdrabuha@outlook.com](mailto:abdrabuha@outlook.com)

**العربية:** © 2026 عبدربه العتيبي — هذا المشروع مُرخَّص بموجب رخصة MIT؛ يمكنك استخدام الأكواد وتعديلها وتعلُّمها ومشاركتها بحرية مع الإبقاء على حقوق المؤلف.

**English:** © 2026 Abdrabuh Alotaibi — this project is licensed under the MIT License; you may freely use, modify, learn from, and share the code, provided you keep this copyright notice.
