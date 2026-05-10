# Contributing to FLAME Detections

Thank you for contributing detection rules to the FLAME detection pack. To maintain quality and consistency, every submitted rule must meet the bar described below.

## Quality Bar

### Required Fields

Every detection rule YAML file must include the following:

1. **`sigma_compatible`** -- Must be explicitly set to `true` or `false`.
   - `true`: The rule uses only standard Sigma fields and can be auto-converted to SPL, EQL, and KQL.
   - `false`: The rule requires stateful correlation, aggregation, or temporal logic that Sigma cannot express.

2. **`falsepositives`** -- At least one entry describing known false positive scenarios.
   ```yaml
   falsepositives:
     - Legitimate bulk account creation by onboarding teams
   ```

3. **`references`** -- At least one external source or reference.
   ```yaml
   references:
     - https://example.com/research-on-this-technique
   ```

4. **`threat_paths`** -- At least one threat path ID from the [FLAME taxonomy](https://github.com/elchacal801/flame-fraud). Threat path IDs follow the format `TP-XXXX`.
   ```yaml
   threat_paths:
     - TP-0042
   ```

### Native Query Requirements

Rules with `sigma_compatible: false` must also include:

5. **`native_query_required: true`** -- Explicitly declared.

6. **`queries`** block -- At least one native query. CQL and SPL are required; KQL and EQL are optional but encouraged.
   ```yaml
   native_query_required: true
   queries:
     cql: |
       event.category = "authentication"
       | stats count() by user.id
       | where count > 50
     spl: |
       index=auth
       | stats count by user_id
       | where count > 50
   ```

### Enrichment Fields

Rules that reference enrichment fields (fields not present in raw log data) must include:

7. **`data_sources`** block -- Documents each enrichment field and its source system.
   ```yaml
   data_sources:
     - field: user.risk_score
       source: Identity Risk Engine
       description: Real-time risk score computed from behavioral analytics
     - field: device.trust_level
       source: Device Trust API
       description: Device posture assessment from endpoint management
   ```

## Submission Process

1. Fork this repository.
2. Create a branch: `detection/TP-XXXX-short-description`.
3. Add your rule YAML file under `DetectionLogic/`.
4. Run `python scripts/validate_rules.py` to verify your rule passes validation.
5. Open a pull request. Use the [Detection Rule Submission](../../issues/new?template=detection-rule-submission.yml) issue template if you want to discuss the rule before submitting a PR.

## Rule File Naming

Detection rule files should follow this naming convention:

```
DetectionLogic/TP-XXXX_short_description.yml
```

Example: `DetectionLogic/TP-0042_rapid_account_creation.yml`

## Questions?

Open an issue or refer to the [FLAME Exchange](https://github.com/elchacal801/flame-fraud) for taxonomy and threat path context.
