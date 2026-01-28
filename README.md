# Decision Assessment Assistant (DAA) Docs

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Schema Validation](https://github.com/hamadalmunyif/decision-assessment-assistant-docs/actions/workflows/deploy-docs.yml/badge.svg)](https://github.com/hamadalmunyif/decision-assessment-assistant-docs/actions)
[![Docs CI](https://github.com/hamadalmunyif/decision-assessment-assistant-docs/actions/workflows/docs-ci.yml/badge.svg)](https://github.com/hamadalmunyif/decision-assessment-assistant-docs/actions)
[![Version](https://img.shields.io/github/v/release/hamadalmunyif/decision-assessment-assistant-docs?label=version)](https://github.com/hamadalmunyif/decision-assessment-assistant-docs/releases)

**Official Documentation & Specifications for the Decision Assessment Assistant (DAA) Ecosystem.**

This repository serves as the **canonical reference** for building DAA Packs. It defines the schemas, methodologies, and standards required to create decision-support tools compatible with the DAA Runtime.

> **Note:** This repository contains **specifications and documentation**. The DAA Runtime (Core Engine) is a separate component that consumes these specifications.

---

## 🚀 Quickstart: Create Your First Pack

Get a decision pack up and running in 3 simple steps.

### 1. Create Pack Structure
Create a new directory for your pack and add the required files:
```bash
mkdir my-first-pack
cd my-first-pack
touch pack.yaml criteria.yaml templates.yaml
```

### 2. Define Metadata (pack.yaml)
```yaml
id: "should-i-buy-a-car"
version: "1.0.0"
name: "Should I Buy a Car?"
description: "Evaluate if you are ready to purchase a vehicle."
author: "Your Name"
```

### 3. Define Criteria (criteria.yaml)
```yaml
- id: "budget"
  name: "Budget Availability"
  weight: 0.5
  scale:
    min: 0
    max: 10
```

### 4. Validate
Use our validation script to check your pack:
```bash
python3 scripts/validate_pack.py my-first-pack
# ✅ Pack 'my-first-pack' is valid!
```

---

## 📚 Documentation

- **[Methodology](METHODOLOGY.md):** The scientific basis of DAA (MCDA, AHP, TOPSIS).
- **[Schema Specification](SCHEMA_SPECIFICATION.md):** Detailed JSON schemas for Packs.
- **[Developer Guide](DEVELOPER_GUIDE.md):** Comprehensive guide for Pack developers.
- **[API Reference](API_REFERENCE.md):** Documentation for the DAA Core API.
- **[Case Studies](CASE_STUDIES.md):** Real-world examples of DAA in action.

---

## 🧩 Examples

Explore ready-to-use examples in the [`examples/`](examples/) directory:
- **Basic:** `should-i-buy-a-car`, `should-i-freelance`
- **Advanced:** `choose-tech-stack`, `invest-in-stock`

---

## 🤝 Contributing

We welcome contributions! Please read our [Contributing Guide](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md).

## 📄 License

This documentation is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE).
