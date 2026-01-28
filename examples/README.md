# DAA Pack Examples

This directory contains example Packs to help you understand the structure and format of a DAA Pack.

---

## Basic Examples

These examples demonstrate the fundamental structure of a DAA Pack:

### 1. Should I Buy a Car?
**Path:** `basic/should-i-buy-a-car/`

A simple Pack to help users decide if they should buy a car. This example demonstrates:
- Basic Pack structure with all required files
- Simple criteria with clear categories
- Standard recommendation templates

**Key Criteria:**
- Financial Cost (40%)
- Convenience (30%)
- Alternatives (20%)
- Environmental Impact (10%)

---

### 2. Should I Start Freelancing?
**Path:** `basic/should-i-freelance/`

A Pack to help users decide if they should start a freelance career. This example demonstrates:
- Career-focused decision criteria
- Balanced weighting across multiple categories
- Practical recommendation templates

**Key Criteria:**
- Financial Stability (40%)
- Market Demand (30%)
- Work-Life Balance (20%)
- Entrepreneurial Spirit (10%)

---

### 3. Should I Relocate?
**Path:** `basic/should-i-relocate/`

A Pack to help users decide if they should relocate to a new city. This example demonstrates:
- Lifestyle-focused decision criteria
- Multiple category types (Financial, Career, Lifestyle, Personal)
- Balanced weighting approach

**Key Criteria:**
- Cost of Living (30%)
- Career Opportunities (30%)
- Quality of Life (20%)
- Social Network (20%)

---

## Advanced Examples

These examples demonstrate more complex Pack structures:

### 1. Choose a Tech Stack
**Path:** `advanced/choose-tech-stack/`

An advanced Pack to help developers choose a tech stack for a new project. This example demonstrates:
- Technical decision-making criteria
- Multiple categories (Technical, Business, Financial)
- Complex weighting with 5+ criteria

**Key Criteria:**
- Scalability (25%)
- Community & Ecosystem (20%)
- Talent Pool (20%)
- Development Velocity (20%)
- Cost (15%)

---

### 2. Invest in a Stock
**Path:** `advanced/invest-in-stock/`

An advanced Pack to help users decide if they should invest in a stock. This example demonstrates:
- Financial decision-making criteria
- Risk assessment integration
- Multiple categories (Financial, Business, Risk)

**Key Criteria:**
- Valuation (30%)
- Financial Health (25%)
- Competitive Advantage (20%)
- Market Outlook (15%)
- Risk Factors (10%)

---

## Using These Examples

To validate any of these examples, use the validation script:

```bash
python3 scripts/validate_pack.py examples/basic/should-i-buy-a-car
```

To create your own Pack, copy one of these examples and modify it to fit your needs:

```bash
cp -r examples/basic/should-i-buy-a-car my-new-pack
cd my-new-pack
# Edit pack.yaml, criteria.yaml, and templates.yaml
```

---

## Schema Compliance

All examples in this directory comply with the official DAA Pack Schema v1.0. For more information, see:
- `SCHEMA_SPECIFICATION.md` - Complete schema documentation
- `schemas/` - JSON Schema files for automated validation
- `scripts/validate_pack.py` - Validation script

---

**Last Updated:** January 2026
