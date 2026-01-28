# DAA Core API Reference

**Version:** 1.0
**Last Updated:** January 2026

---

## 1. Introduction

This document provides a comprehensive reference for the Decision Assessment Assistant (DAA) Core API. The Core API provides the fundamental building blocks for loading Decision Packs, evaluating complex decisions, and generating insightful recommendations. It is designed to be used by developers who are building custom integrations or extending the DAA platform.

---

## 2. Core Concepts

- **DAA Core:** The central engine that orchestrates the entire decision assessment process.
- **Pack:** A self-contained directory that defines a specific decision-making model, including its criteria and recommendation templates.
- **Criteria:** The set of factors used to evaluate a decision. Each criterion has a name, description, category, and a default weight.
- **Evaluation:** The process of scoring a decision based on the defined criteria and user-provided data.
- **Risk Analysis:** The process of identifying and quantifying the risks associated with a decision.
- **Recommendation:** The final output of the DAA, which provides a clear, actionable recommendation based on the evaluation and risk analysis.

---

## 3. Core API (Conceptual)

The DAA Core API is exposed through a set of Python classes and methods. The following is a conceptual overview of the main components.

### 3.1. `DAA_Core` Class

The main entry point for interacting with the DAA.

**Methods:**

- `load_pack(pack_path: str) -> bool`
  - **Description:** Loads a Decision Pack from the specified directory path.
  - **Parameters:**
    - `pack_path`: The absolute path to the Pack directory.
  - **Returns:** `True` if the Pack was loaded successfully, `False` otherwise.

- `evaluate(decision_data: dict) -> dict`
  - **Description:** Evaluates a decision based on the loaded Pack and user-provided data.
  - **Parameters:**
    - `decision_data`: A dictionary containing the user's ratings for each criterion.
  - **Returns:** A dictionary containing the evaluation results, including the total score.

- `get_recommendation() -> dict`
  - **Description:** Generates a recommendation based on the evaluation score.
  - **Returns:** A dictionary containing the recommendation type (`positive`, `negative`, `neutral`) and the recommendation text.

### 3.2. `Evaluator` Class

Handles the core evaluation logic.

**Methods:**

- `run_evaluation(criteria: list, data: dict) -> float`
  - **Description:** Calculates the weighted score for a decision.
  - **Parameters:**
    - `criteria`: A list of criteria objects from the loaded Pack.
    - `data`: A dictionary containing the user's ratings.
  - **Returns:** The final weighted score (0.0 to 10.0).

### 3.3. `RiskAnalyzer` Class

Analyzes the risks associated with a decision.

**Methods:**

- `analyze_risk(decision_data: dict) -> dict`
  - **Description:** Performs a risk analysis based on the decision data and pre-defined risk factors.
  - **Parameters:**
    - `decision_data`: The user's input data.
  - **Returns:** A dictionary containing the risk assessment.

### 3.4. `RecommendationEngine` Class

Generates the final recommendation.

**Methods:**

- `generate_recommendation(score: float, templates: list) -> dict`
  - **Description:** Selects the appropriate recommendation template based on the evaluation score.
  - **Parameters:**
    - `score`: The final evaluation score.
    - `templates`: A list of recommendation templates from the loaded Pack.
  - **Returns:** A dictionary containing the final recommendation.

---

## 4. Data Structures

### 4.1. Decision Data (Input)

This is the data provided by the user for evaluation.

```json
{
  "criteria_ratings": {
    "Financial Impact": 8.5,
    "Career Growth": 9.0,
    "Work-Life Balance": 7.0
  },
  "risk_factors": {
    "market_volatility": "medium",
    "job_security": "high"
  }
}
```

### 4.2. Evaluation Result (Output)

```json
{
  "total_score": 8.25,
  "weighted_scores": {
    "Financial Impact": 3.4,
    "Career Growth": 2.7,
    "Work-Life Balance": 2.15
  }
}
```

### 4.3. Recommendation Result (Output)

```json
{
  "type": "positive",
  "text": "Based on your inputs, this decision appears to be highly favorable and aligns well with your stated priorities.",
  "confidence_score": 0.88
}
```

---

## 5. Example Usage

```python
from daa_core import DAA_Core

# 1. Initialize the DAA Core
daa = DAA_Core()

# 2. Load a Decision Pack
pack_loaded = daa.load_pack("/path/to/your/pack")

if pack_loaded:
    # 3. Provide decision data
    decision_data = {
        "criteria_ratings": {
            "Financial Impact": 8.5,
            "Career Growth": 9.0,
            "Work-Life Balance": 7.0
        }
    }

    # 4. Evaluate the decision
    evaluation_result = daa.evaluate(decision_data)
    print(f"Evaluation Score: {evaluation_result['total_score']}")

    # 5. Get the recommendation
    recommendation = daa.get_recommendation()
    print(f"Recommendation: {recommendation['text']}")
```
