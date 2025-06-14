# GenAI-EHR-Predictor
GenAI-powered readmission risk prediction from EHR + claims data using AWS

# 🧠 GenAI-EHR-Predictor: Explainable Clinical Cost Prediction with LLMs

This project demonstrates how to combine **machine learning**, **structured EHR + insurance claims data**, and **LLM-powered explanations** to predict high-cost hospitalizations and make those predictions **clinician-friendly**.

Built entirely in **AWS SageMaker**, the project simulates a real-world healthcare analytics workflow used by data science teams at leading hospitals like MSKCC.

---

## 🚀 What It Does

- ✅ Simulates real-world **EHR + claims data**
- ✅ Preprocesses & merges **patients, encounters, FHIR, and billing**
- ✅ Trains a **binary classification model** (high-cost vs. low-cost)
- ✅ Adds **Generative AI explanations** per patient (Claude/GPT style)
- ✅ Uploads full pipeline results to **GitHub**
- ✅ Ready for dashboard or API deployment

---

## 📊 Sample Output

| Age | Length of Stay | Claim | Prediction | GenAI Explanation |
|-----|----------------|--------|-------------|-------------------|
| 82  | 7 days         | $20,000 | High-Risk | Advanced age with extended stay and high cost suggests comorbidities and future risk. |
| 65  | 5 days         | $12,000 | High-Risk | Moderate LOS and complex billing indicate elevated clinical burden. |

---

## 🧠 Technologies Used

- 🧮 **XGBoost** via AWS SageMaker
- 🧾 **Synthetic FHIR + claims data**
- 🪄 **Generative AI (Claude/GPT-style)** explanations
- 📦 **Git + GitHub** for reproducibility
- 🛠️ (Optional) Ready for Streamlit, FastAPI, or Bedrock integration

---

## 🧑‍⚕️ Why It Matters

> Traditional ML models are often black boxes. In healthcare, that’s not acceptable. This project adds **transparent, GenAI-powered explanations** to support clinical decision-making — bridging the gap between model and medicine.

---

## 🛠️ Project Structure

```
GenAI-EHR-Predictor/
│
├── data/ # Input and output CSVs
├── notebooks/ # SageMaker notebooks
├── scripts/ # Preprocessing & training logic
├── README.md # You’re here!
```


---

## 🙋 Author

**Hadi Ghahremannezhad**  
Machine Learning Engineer | MSKCC  
[LinkedIn](https://www.linkedin.com/in/hg20) | [GitHub](https://github.com/hadign20)

