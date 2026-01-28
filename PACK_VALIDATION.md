_DRAFT: Pack Validation and Compliance Checklist_

# Decision Assessment Assistant (DAA) - Pack Validation Criteria

This document outlines the technical and methodological requirements that every Pack must meet to be approved for publication on the official DAA Marketplace.

---

## 1. Purpose

The goal of this validation process is to ensure that all Packs on the Marketplace are:

- **High-Quality**: Well-built, tested, and reliable.
- **Consistent**: Adhere to the DAA's core scientific methodology.
- **Secure**: Free from vulnerabilities and malicious code.
- **Well-Documented**: Easy for end-users to understand and use.

---

## 2. Automated Validation Checklist

A submitted Pack must pass all of the following automated checks. A validation script (`scripts/validate_pack.py`) will be used to perform these checks.

### 2.1. Directory Structure

The Pack must follow this exact directory structure:

```
my-awesome-pack/
├── pack.yaml              # Metadata file for the Pack
├── criteria.yaml          # Domain-specific criteria definitions
├── templates.yaml         # Custom prompt templates for the LLM
├── docs/
│   └── README.md          # Detailed documentation for the Pack
├── tests/
│   ├── test_criteria.py   # Tests for the criteria
│   └── test_templates.py  # Tests for the prompt templates
└── examples/
    └── sample_decision.json # A sample decision scenario
```

### 2.2. Metadata File (`pack.yaml`)

The `pack.yaml` file must exist and contain the following fields:

- `id`: A unique, lowercase, hyphenated identifier (e.g., `career-decision-pack`).
- `name`: The human-readable name of the Pack (e.g., "Career Decision Pack").
- `version`: The version of the Pack (e.g., `1.0.0`), following Semantic Versioning.
- `author`: The name and email of the developer/organization.
- `description`: A brief, one-sentence description of the Pack.
- `tags`: A list of relevant keywords (e.g., `["career", "jobs", "employment"]`).

### 2.3. Criteria File (`criteria.yaml`)

- The file must be valid YAML.
- It must contain a list of criteria, each with the following fields:
  - `name`: The name of the criterion.
  - `description`: A clear explanation of what the criterion measures.
  - `category`: The category of the criterion (e.g., `financial`, `personal`).
  - `default_weight`: A default importance weight (0.0 to 1.0).

### 2.4. Templates File (`templates.yaml`)

- The file must be valid YAML.
- It must contain at least one custom prompt template for the LLM.
- Each template must use the `{{placeholder}}` syntax for dynamic values.

### 2.5. Testing Requirements

- The `tests/` directory must exist.
- The test suite must run without errors using `pytest`.
- **Minimum Test Coverage**: The test suite must achieve at least **90%** code coverage for the Pack's logic (if any custom Python code is included).

### 2.6. Documentation Requirements

- The `docs/README.md` file must exist.
- It must be at least 500 characters long.
- It must contain the following sections: "Overview", "Features", "How to Use", and "Example".

---

## 3. Manual Review Checklist

After passing the automated checks, the Pack will undergo a manual review based on the following criteria.

### 3.1. Methodological Compliance

- **Alignment with DAA Principles**: Do the criteria and prompts align with the core principles of structured, evidence-based decision-making?
- **Objectivity**: Are the criteria defined in an objective and measurable way?
- **Bias Mitigation**: Does the Pack actively work to mitigate common cognitive biases?
- **Clarity and Logic**: Is the logic of the Pack clear, sound, and easy for an end-user to follow?

### 3.2. Quality and Usefulness

- **Value Proposition**: Does the Pack solve a real-world problem for a specific audience?
- **User Experience**: Is the Pack easy to understand and use? Is the documentation clear?
- **Originality**: Does the Pack offer unique value, or is it a simple duplicate of an existing Pack?

### 3.3. Security Review

- **No Malicious Code**: The code will be reviewed for any signs of malicious activity.
- **Data Privacy**: The Pack must not collect or transmit any user data without explicit consent.
- **Dependencies**: All external dependencies must be from trusted sources.

---

## 4. The Validation Process

1.  **Submission**: Developer submits the Pack via the official portal.
2.  **Automated Validation**: The `validate_pack.py` script is run.
    - If it fails, a report is sent to the developer.
    - If it passes, it moves to manual review.
3.  **Manual Review**: A DAA team member reviews the Pack against the manual checklist.
    - If it fails, feedback is sent to the developer.
    - If it passes, it is approved for the Marketplace.
4.  **Publication**: The Pack is signed, packaged, and published.

---

**Last Updated:** January 2026
