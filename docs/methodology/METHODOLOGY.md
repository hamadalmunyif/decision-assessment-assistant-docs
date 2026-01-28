# المنهجية العلمية لـ Decision Assessment Assistant (DAA)

**آخر تحديث:** يناير 2026

---

## 1. الملخص (Abstract)

تعتمد منصة **Decision Assessment Assistant (DAA)** على إطار علمي راسخ يدمج بين نظريات تحليل القرارات متعددة المعايير (Multi-Criteria Decision Analysis - MCDA) ونماذج اتخاذ القرار في ظل عدم اليقين (Decision Making Under Uncertainty). الهدف الأساسي هو توفير عملية منهجية، شفافة، وقابلة للتدقيق لتحليل القرارات المعقدة، وتقليل تأثير الانحيازات المعرفية (Cognitive Biases)، وتقديم توصيات قائمة على الأدلة.

تستخدم المنهجية بشكل أساسي **عملية التحليل الهرمي (Analytic Hierarchy Process - AHP)** لتحديد أوزان المعايير بشكل موضوعي، ونموذج الجمع المرجح (Weighted Sum Model) لتقييم الخيارات، ومصفوفة المخاطر لتقييم الجوانب غير المؤكدة في كل قرار.

---

## 2. الإطار النظري (Theoretical Framework)

### 2.1. تحليل القرارات متعددة المعايير (MCDA)

**MCDA** هو فرع من بحوث العمليات يوفر مجموعة من الأساليب المنهجية لتقييم الخيارات بناءً على معايير متعددة ومتضاربة في كثير من الأحيان [1]. بدلاً من البحث عن حل "أمثل" واحد، تهدف MCDA إلى مساعدة صانعي القرار على فهم المقايضات (Trade-offs) بين المعايير المختلفة واختيار الخيار الذي يتوافق بشكل أفضل مع تفضيلاتهم [2].

> "MCDA emerged as a formal methodology to face available decisions in many fields and can be especially valuable in environmental decision making." [3]

### 2.2. عملية التحليل الهرمي (AHP)

**AHP**، التي طورها Thomas L. Saaty، هي تقنية رياضية منظمة لتحليل القرارات المعقدة [4]. تعتمد AHP على ثلاثة مبادئ أساسية:

1.  **التحليل الهرمي (Decomposition):** تقسيم المشكلة إلى هرم من العناصر: الهدف في الأعلى، ثم المعايير، وأخيراً الخيارات في الأسفل.
2.  **المقارنات الزوجية (Pairwise Comparisons):** مقارنة كل عنصرين في نفس المستوى لتحديد أهميتهما النسبية.
3.  **التوليف المنطقي (Logical Synthesis):** حساب الأوزان والأولويات لكل عنصر في الهرم.

تتميز AHP بقدرتها على التعامل مع المعايير الكمية والنوعية، والتحقق من اتساق الأحكام باستخدام **نسبة الاتساق (Consistency Ratio - CR)** [5].

### 2.3. اتخاذ القرار في ظل عدم اليقين

تتضمن معظم القرارات الحقيقية درجة من عدم اليقين. تعتمد منهجيتنا على نماذج من نظرية القرار للتعامل مع هذه الجوانب [6]. يتم ذلك من خلال:

- **تحديد المخاطر:** تحديد الأحداث غير المؤكدة التي قد تؤثر على نتائج كل خيار.
- **تقييم الاحتمالية والتأثير:** تقدير احتمالية حدوث كل خطر وتأثيره المحتمل.
- **مصفوفة المخاطر:** أداة مرئية لتصنيف المخاطر وتحديد أولوياتها.

---

## 3. منهجية DAA (A 6-Step Methodology)

| المرحلة | الوصف | المخرجات الرئيسية |
|---|---|---|
| **1. بناء الهيكل (Structuring)** | تقسيم المشكلة إلى هدف، معايير، وخيارات. | هرم القرار |
| **2. تحديد الأوزان (Weighting)** | استخدام المقارنات الزوجية (AHP) لتحديد أوزان المعايير. | مصفوفة الأوزان، نسبة الاتساق (CR) |
| **3. التقييم (Scoring)** | تقييم أداء كل خيار مقابل كل معيار. | مصفوفة الدرجات |
| **4. التوليف (Synthesis)** | حساب الدرجة الإجمالية لكل خيار باستخدام نموذج الجمع المرجح. | ترتيب الخيارات |
| **5. تحليل المخاطر (Risk Analysis)** | تحديد وتقييم المخاطر المرتبطة بكل خيار. | مصفوفة المخاطر، درجة المخاطر لكل خيار |
| **6. التوصية (Recommendation)** | دمج النتائج لتوليد توصية شاملة مع درجة ثقة. | تقرير القرار النهائي |

---

## 4. الأسس الرياضية (Mathematical Foundations)

### 4.1. حساب الأوزان (AHP)

1.  **إنشاء مصفوفة المقارنة الزوجية (A):**
    - `a_ij` = أهمية المعيار `i` بالنسبة للمعيار `j`.
    - `a_ji = 1 / a_ij`

2.  **حساب متجه الأولوية (w):**
    - يتم حسابه كمتجه ذاتي (Eigenvector) للمصفوفة A.
    - `A * w = λ_max * w`

3.  **حساب نسبة الاتساق (CR):**
    - `CI = (λ_max - n) / (n - 1)` (Consistency Index)
    - `CR = CI / RI` (Consistency Ratio)
    - `RI` هو مؤشر عشوائي يعتمد على حجم المصفوفة `n`.
    - إذا كان `CR ≤ 0.10`، فإن الأحكام تعتبر متسقة.

### 4.2. حساب الدرجة الإجمالية

يتم حساب الدرجة الإجمالية لكل خيار `i` باستخدام نموذج الجمع المرجح:

`Score(Option_i) = Σ (w_j * s_ij)`

- `w_j` = وزن المعيار `j`.
- `s_ij` = درجة الخيار `i` على المعيار `j`.

### 4.3. حساب درجة المخاطر

`Risk Score = Probability * Impact`

---

## 5. التحقق من الصحة (Validation)

تعتمد منهجيتنا على مبادئ علمية تم التحقق من صحتها على نطاق واسع في الأدبيات الأكاديمية. سيتم توثيق التحقق التجريبي من خلال دراسات الحالة (Case Studies) التي تقارن نتائج المنصة مع قرارات الخبراء في مجالات مختلفة.

---

## 6. المراجع (References)

[1] Greco, S., et al. (2025). "Fifty years of multiple criteria decision analysis." *European Journal of Operational Research*.

[2] Cinelli, M., et al. (2020). "How to support the application of multiple criteria decision..." *PMC*. [https://pmc.ncbi.nlm.nih.gov/articles/PMC7970504/](https://pmc.ncbi.nlm.nih.gov/articles/PMC7970504/)

[3] Huang, I. B., et al. (2011). "Multi-criteria decision analysis in environmental sciences: Ten years of applications and trends." *Science of The Total Environment*.

[4] Saaty, T. L. (1990). "An overview of the analytic hierarchy process and its applications." *European Journal of Operational Research*.

[5] Saaty, T. L. (1980). *The Analytic Hierarchy Process: Planning, Priority Setting, Resource Allocation*. McGraw-Hill.

[6] Kochenderfer, M. J. (2015). *Decision Making Under Uncertainty: Theory and Application*. MIT Press.

[7] Vaidya, O. S., & Kumar, S. (2018). "Review of application of analytic hierarchy process (AHP) in construction." *International Journal of Construction Management*.

[8] Forman, E. H., & Gass, S. I. (2001). "The analytic hierarchy process—an exposition." *Operations research*.

[9] Triantaphyllou, E. (2000). *Multi-criteria decision making methods: A comparative study*. Springer.

[10] Belton, V., & Stewart, T. J. (2002). *Multiple criteria decision analysis: an integrated approach*. Springer.
