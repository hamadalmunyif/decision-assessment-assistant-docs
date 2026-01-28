#!/usr/bin/env python3
"""
DAA Pack Validation Script
Version: 1.0
Last Updated: January 2026

This script validates a DAA Pack against the official schema specification.
It checks for:
- The presence of all required files
- Schema compliance for pack.yaml, criteria.yaml, and templates.yaml
- Correct data types and constraints
- Sum of weights in criteria.yaml equals 1.0
"""

import os
import sys
import yaml
import json
from pathlib import Path
from jsonschema import validate, ValidationError


def load_yaml(file_path):
    """Load a YAML file and return its contents."""
    try:
        with open(file_path, 'r') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"❌ Error loading {file_path}: {e}")
        return None


def load_json_schema(schema_path):
    """Load a JSON schema file."""
    try:
        with open(schema_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ Error loading schema {schema_path}: {e}")
        return None


def validate_file_structure(pack_dir):
    """Check if all required files are present."""
    required_files = ['pack.yaml', 'criteria.yaml', 'templates.yaml']
    missing_files = []
    
    for file in required_files:
        file_path = os.path.join(pack_dir, file)
        if not os.path.exists(file_path):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing required files: {', '.join(missing_files)}")
        return False
    
    print("✅ All required files are present")
    return True


def validate_schema_compliance(pack_dir, schema_dir):
    """Validate all YAML files against their JSON schemas."""
    files_to_validate = [
        ('pack.yaml', 'pack.schema.json'),
        ('criteria.yaml', 'criteria.schema.json'),
        ('templates.yaml', 'templates.schema.json')
    ]
    
    all_valid = True
    
    for yaml_file, schema_file in files_to_validate:
        yaml_path = os.path.join(pack_dir, yaml_file)
        schema_path = os.path.join(schema_dir, schema_file)
        
        # Load the YAML file
        data = load_yaml(yaml_path)
        if data is None:
            all_valid = False
            continue
        
        # Load the JSON schema
        schema = load_json_schema(schema_path)
        if schema is None:
            all_valid = False
            continue
        
        # Validate
        try:
            validate(instance=data, schema=schema)
            print(f"✅ {yaml_file} is valid")
        except ValidationError as e:
            print(f"❌ {yaml_file} validation failed: {e.message}")
            all_valid = False
    
    return all_valid


def validate_criteria_weights(pack_dir):
    """Check that the sum of weights in criteria.yaml equals 1.0."""
    criteria_path = os.path.join(pack_dir, 'criteria.yaml')
    criteria = load_yaml(criteria_path)
    
    if criteria is None:
        return False
    
    total_weight = sum(c['default_weight'] for c in criteria)
    
    if abs(total_weight - 1.0) > 0.001:  # Allow for small floating-point errors
        print(f"❌ Sum of criteria weights is {total_weight}, but it must equal 1.0")
        return False
    
    print(f"✅ Sum of criteria weights is {total_weight:.3f}")
    return True


def main():
    if len(sys.argv) != 2:
        print("Usage: python validate_pack.py <path_to_pack_directory>")
        sys.exit(1)
    
    pack_dir = sys.argv[1]
    
    if not os.path.isdir(pack_dir):
        print(f"❌ {pack_dir} is not a valid directory")
        sys.exit(1)
    
    # Determine the schema directory (relative to this script)
    script_dir = Path(__file__).parent
    schema_dir = script_dir.parent / 'schemas'
    
    print(f"\n🔍 Validating Pack: {pack_dir}\n")
    print("=" * 60)
    
    # Step 1: Check file structure
    print("\n1. Checking file structure...")
    if not validate_file_structure(pack_dir):
        print("\n❌ Validation failed: Missing required files")
        sys.exit(1)
    
    # Step 2: Validate schema compliance
    print("\n2. Validating schema compliance...")
    if not validate_schema_compliance(pack_dir, schema_dir):
        print("\n❌ Validation failed: Schema compliance errors")
        sys.exit(1)
    
    # Step 3: Validate criteria weights
    print("\n3. Validating criteria weights...")
    if not validate_criteria_weights(pack_dir):
        print("\n❌ Validation failed: Criteria weights do not sum to 1.0")
        sys.exit(1)
    
    print("\n" + "=" * 60)
    print("✅ Pack validation successful!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
