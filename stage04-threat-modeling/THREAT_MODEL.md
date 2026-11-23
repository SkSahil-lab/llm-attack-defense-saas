# Stage 4 — Threat Modeling

**PTES:** Threat Modeling | **Kill Chain:** Reconnaissance (continued)

## Classification: GenAI (Level 1)

Based on observed behavior only, not the target's self-report. The target has no real tool access, no persistent memory across sessions, and no multi-agent coordination — despite Finding 3.1 showing it falsely claims internet/tool access when asked.

## Scope for the remaining engagement

**Testable now (GenAI-level):** LLM01, LLM02, LLM07, LLM08, LLM09, LLM10
**Deferred until Stage 9:** LLM03, LLM04, LLM05, LLM06 — these require tool access or multi-agent coordination the target does not yet have

## Third framework added: MITRE ATLAS

Alongside PTES and the Cyber Kill Chain, this engagement now references **MITRE ATLAS** — a framework built specifically for adversary tactics against AI systems (16 tactics as of the current release, adapted from MITRE ATT&CK with two AI-specific additions).

Stage 3's reconnaissance activity maps to ATLAS's **Reconnaissance** and **Discovery** tactics: gathering target identity, capability claims, and session behavior before any attack payload was sent.

*(Exact ATLAS tactic IDs will be verified against atlas.mitre.org before the final Stage 14 report — secondary sources show inconsistent numbering for some tactics.)*