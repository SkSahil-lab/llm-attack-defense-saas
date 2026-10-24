# Rules of Engagement

**Engagement ID:** AI-RT-03
**Document version:** 1.0
**Date:** 24/10/2026
**Prepared by:** Shaik Sahil
**Methodology:** PTES (engagement process) cross-referenced with the Cyber Kill Chain (attack sequence)

---

## 1. Engagement Overview

**Objective:** Conduct a full AI red team engagement against a self-built, locally hosted LLM environment, demonstrating the complete lifecycle: reconnaissance, threat modeling, vulnerability analysis, exploitation, persistence, post-exploitation, defense validation, and formal reporting.

**Why this engagement exists:** Phases 1 and 2 of this project proved individual exploits and defenses against the OWASP LLM Top 10 (2026). This phase tests whether those findings hold together as a repeatable, professional process against a real model, rather than isolated demonstrations.

## 2. Authorization

This is a self-owned laboratory engagement. The client, the tester, and the owner of every in-scope asset are the same person. No third-party authorization is required because no third-party system is touched.

> **Authorizing party:** Shaik Sahil, owner of all in-scope assets
> **Testing authorized for:** the assets listed in Section 3, and only those assets

## 3. In-Scope Assets

| Asset | Description | Active in stages |
|---|---|---|
| Local LLM | Ollama running `llama3.2:1b`, bound to localhost | 2 to 12 |
| Ollama API endpoint | `http://localhost:11434`, the model-serving interface | 3 to 13 |
| Phase 1 target applications | The deliberately vulnerable apps in `llm-redteam-framework` | 6, 8 |
| Phase 2 defense gateway | The nine defenses in `llm-defense-gateway` | 12 |
| Multi-agent test system | The 2-3 agent orchestrated system built in Stage 9 | 9 to 11 |
| Container and cluster infrastructure | Docker images and the local Kubernetes deployment | 13, 15 |
| Synthetic data | Fake credentials, fake policies, and fake documents created for testing | All |

## 4. Out-of-Scope (Explicitly Prohibited)

Testing against any of the following is a violation of this engagement and must not occur:

- Any system, API, or model not owned and run locally by the tester
- Hosted or commercial AI services (OpenAI, Anthropic, Google, and similar), including their APIs
- Any cloud account, cloud-hosted resource, or paid infrastructure
- Real personal data, real credentials, real payment details, or real customer information
- Any public internet target, including websites and third-party repositories
- Other people's models, datasets, or deployments, including those encountered during research
- Denial-of-service testing that could destabilize the host machine beyond the resource limits in Section 5

## 5. Rules and Constraints

1. **Local only.** All traffic stays on the loopback interface. No scan, probe, or payload leaves the machine.
2. **Synthetic data only.** Every secret, credential, and "customer record" in the lab is fabricated.
3. **Resource safety.** Close unrelated applications before any automated scan. Begin with a small probe subset, monitor memory live, and scale only if the host stays stable. The Ollama keep-alive is set to 30 seconds so the model unloads when idle.
4. **Time-boxing.** If a tool's installation or configuration blocks progress beyond one working session, the attempt is documented honestly and an equivalent approach is used instead.
5. **Everything is logged.** Commands, tool versions, outputs, and findings are recorded so every result can be reproduced.
6. **No scope creep.** Anything that appears useful but falls outside Section 3 is recorded as a recommendation and not tested.

## 6. Tools Authorized

| Tool | Purpose | Stage |
|---|---|---|
| Ollama | Local model hosting | 2 |
| Garak | Automated LLM vulnerability scanning | 5 |
| PyRIT | Multi-turn attack orchestration | 8, 10, 11 |
| Promptfoo | Defense regression testing and reporting | 12, 14 |
| Custom scripts | Reconnaissance, classification, delivery, agent system | 3, 4, 7, 9 |

Tools outside this list may be evaluated, but adoption requires a documented reason in the final report.

## 7. Stop Conditions

Testing halts immediately, and the event is documented, if any of the following occur:

- A tool attempts to contact a host outside localhost
- Real personal data or real credentials appear in any input or output
- The host machine becomes unstable (sustained memory exhaustion, freezing)
- A finding or action falls outside the scope defined in Section 3

## 8. Deliverables

- Stage-by-stage documentation and tool output in this repository
- A formal engagement report: executive summary, severity-rated findings, remediation mapped to the Phase 2 defenses, and reproduction steps
- A Docker and Kubernetes deployment of the final platform
- A recorded end-to-end demonstration

## 9. Acknowledgment

I confirm that this engagement is limited to the assets in Section 3, that all data is synthetic, and that testing will stop under any condition in Section 7.

**Signed:** Shaik Sahil
**Date:** 24/10/2026