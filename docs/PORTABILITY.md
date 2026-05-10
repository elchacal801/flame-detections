# Portability

## Honest Assessment

Not all detection rules in this pack are equally portable. Here is the breakdown.

### Sigma-Compatible Rules: 98 (44%)

These 98 rules use only standard Sigma fields and logic. They auto-convert to SPL, EQL, and KQL via pySigma backends:

- **SPL** via `pySigma-backend-splunk`
- **KQL** via `pySigma-backend-microsoft365defender`
- **EQL / Lucene** via `pySigma-backend-elasticsearch`

For these rules, you get multi-platform coverage out of the box.

### Native-Query-Required Rules: 123 (56%)

These 123 rules require stateful correlation, aggregation, temporal sequencing, or multi-event joins that Sigma cannot express. For these rules:

- **CQL** (CrowdStrike NGSIEM) -- Hand-written native queries provided in the `queries:` block.
- **SPL** (Splunk) -- Hand-written native queries provided in the `queries:` block.
- **KQL** (Microsoft Sentinel / Defender) -- Not yet provided. Tracked as roadmap.
- **EQL** (Elasticsearch) -- Not yet provided. Tracked as roadmap.

### Backend Caveats

**KQL output is not ASIM-aligned.** The KQL output is generated via pySigma's Microsoft 365 Defender backend. It targets the M365D advanced hunting schema, not the Azure Sentinel ASIM (Advanced Security Information Model) normalized schema.

**Elasticsearch output uses Lucene, not native EQL.** The `pySigma-backend-elasticsearch` backend generates Lucene query strings, not Elasticsearch Event Query Language (EQL). For correlation rules, this means you cannot use EQL sequences or joins in the generated output.

## Roadmap

- ASIM-aligned KQL backend for Azure Sentinel compatibility
- Native EQL backend for Elasticsearch sequence and join support
- SigmaHQ upstream curation for rules that meet SigmaHQ quality standards
