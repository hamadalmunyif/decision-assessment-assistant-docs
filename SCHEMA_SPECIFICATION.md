_DRAFT: Pack Schema Specification_

# DAA Pack Schema Specification

**Version:** 1.0
**Last Updated:** January 2026

---

## 1. Introduction

This document provides a detailed specification for the Decision Assessment Assistant (DAA) Pack schema. All Packs submitted to the DAA Marketplace **must** adhere to this schema to ensure consistency, interoperability, and a high-quality user experience.

Schema stability is a core principle of the DAA ecosystem. This specification will be versioned, and any future changes will be made in a backward-compatible manner where possible.

---

## 2. Core Files

A DAA Pack is a directory containing a set of YAML files that define its structure and behavior. The core files are:

- `pack.yaml`: Contains metadata about the Pack.
- `criteria.yaml`: Defines the criteria used for assessment.
- `templates.yaml`: Contains the recommendation templates.

---

## 3. `pack.yaml` Specification

The `pack.yaml` file contains essential metadata about the Pack.

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | String | Yes | A unique, lowercase, hyphenated identifier (e.g., `career-decision-pack`). |
| `name` | String | Yes | The human-readable name of the Pack (e.g., "Career Decision Pack"). |
| `version` | String | Yes | The version of the Pack, following Semantic Versioning (e.g., `1.0.0`). |
| `author` | String | Yes | The name and email of the developer or organization. |
| `description` | String | Yes | A brief, one-sentence description of the Pack. |
| `tags` | List[String] | Yes | A list of relevant keywords (e.g., `["career", "jobs", "employment"]`). |

### Example `pack.yaml`:

```yaml
id: career-decision-pack
name: "Career Decision Pack"
version: 1.0.0
author: "Manus AI <hamad_almunif@icloud.com>"
description: "A comprehensive pack to assist with career-related decisions."
tags: ["career", "jobs", "employment"]
```

---

## 4. `criteria.yaml` Specification

The `criteria.yaml` file defines the set of criteria that the DAA will use to evaluate a decision.

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | String | Yes | The name of the criterion. |
| `description` | String | Yes | A clear explanation of what the criterion measures. |
| `category` | String | Yes | The category of the criterion (e.g., `Financial`, `Personal`, `Technical`). |
| `default_weight` | Float | Yes | A default importance weight between 0.0 and 1.0. The sum of all weights must be 1.0. |

### Example `criteria.yaml`:

```yaml
- name: "Financial Impact"
  description: "The overall financial impact of the decision, including salary, benefits, and other compensation."
  category: "Financial"
  default_weight: 0.4

- name: "Career Growth"
  description: "The potential for career advancement and skill development."
  category: "Career"
  default_weight: 0.3

- name: "Work-Life Balance"
  description: "The expected impact on the balance between professional and personal life."
  category: "Lifestyle"
  default_weight: 0.3
```

---

## 5. `templates.yaml` Specification

The `templates.yaml` file contains templates for generating recommendations based on the assessment score.

| Field | Type | Required | Description |
|---|---|---|---|
| `recommendation` | List[Object] | Yes | A list of recommendation templates. |
| `type` | String | Yes | The type of recommendation (`positive`, `negative`, `neutral`). |
| `template` | String | Yes | The template string for the recommendation. |

### Example `templates.yaml`:

```yaml
recommendation:
  - type: "positive"
    template: "Based on your inputs, this decision appears to be highly favorable and aligns well with your stated priorities."
  - type: "negative"
    template: "Based on your inputs, this decision may not be the best choice for you at this time. There are significant misalignments with your priorities."
  - type: "neutral"
    template: "The assessment is inconclusive. There are both strong advantages and disadvantages to consider. Further reflection is recommended."
```

---

## 6. Schema Versioning

This schema is versioned to allow for future enhancements. The current version is **1.0**. Any changes to the schema will be documented in this file and reflected in the version number.

- **Major Version (e.g., 2.0):** Indicates a backward-incompatible change.
- **Minor Version (e.g., 1.1):** Indicates a backward-compatible change.
- **Patch Version (e.g., 1.0.1):** Indicates a bug fix or clarification.

---

## 7. Validation

All Packs will be validated against this schema using an automated script. The validation script will check for:

- The presence of all required files.
- The presence of all required fields in each file.
- The correct data type for each field.
- Compliance with any additional constraints (e.g., the sum of weights in `criteria.yaml` must be 1.0).

A JSON Schema file (`schema.json`) will be provided to facilitate automated validation.
