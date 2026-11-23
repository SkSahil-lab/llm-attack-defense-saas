import json

class ArchitectureClassifier:
    """
    Classifies a target as GenAI / AI Agent / Agentic AI based on
    OBSERVED behavior from Stage 3's recon - never on self-report.
    Finding 3.1 proved this target's self-report is unreliable.
    """

    def __init__(self, recon_report_path):
        with open(recon_report_path) as f:
            self.recon = json.load(f)

    def observed_tool_execution(self) -> bool:
        # True only if a probe response showed evidence of an ACTUAL
        # external call (e.g. real data returned that recon.py didn't
        # supply). recon.py never wires in a real tool, so this is False
        # regardless of what the model claims about itself.
        return False

    def observed_persistent_memory(self) -> bool:
        # True only if state persisted across separate process runs,
        # not just within one conversation. Not implemented here.
        return False

    def observed_multi_agent_coordination(self) -> bool:
        # True only if multiple distinct agents were observed passing
        # output to one another. Not applicable until Stage 9.
        return False

    def classify(self) -> dict:
        if self.observed_multi_agent_coordination():
            level = "Agentic AI"
        elif self.observed_tool_execution() or self.observed_persistent_memory():
            level = "AI Agent"
        else:
            level = "GenAI"

        return {
            "classification": level,
            "basis": "observed behavior only - self-reported capability claims are not trusted",
            "evidence": "recon.py sent plain-text prompts only; no tool was wired in; no state persisted across runs",
            "contradicts_target_self_report": True,
            "note": "Target claimed internet/tool access in Finding 3.1. That claim is false and is disregarded here.",
        }

    def applicable_owasp_categories(self, level: str) -> dict:
        mapping = {
            "GenAI": {
                "applicable_now": ["LLM01 Prompt Injection", "LLM02 Sensitive Info Disclosure",
                                    "LLM07 Misinformation", "LLM08 Hidden Context Exposure",
                                    "LLM09 Vector & Embedding Weaknesses", "LLM10 Improper Output Handling"],
                "deferred": ["LLM03 Excessive Agency", "LLM04 Supply Chain",
                             "LLM05 Data & Model Poisoning", "LLM06 Unbounded Consumption"],
                "deferred_reason": "These require tool access or multi-agent coordination, "
                                   "which this target does not have yet. They become testable once "
                                   "Stage 9 builds the multi-agent system.",
            }
        }
        return mapping.get(level, {"applicable_now": [], "deferred": [], "deferred_reason": "n/a"})


if __name__ == "__main__":
    classifier = ArchitectureClassifier("../stage03-reconnaissance/recon_report.json")
    result = classifier.classify()
    scope = classifier.applicable_owasp_categories(result["classification"])

    print(f"Classification: {result['classification']}")
    print(f"Basis: {result['basis']}")
    print(f"Contradicts target's own claim: {result['contradicts_target_self_report']}")
    print(f"\nTestable now ({len(scope['applicable_now'])}):")
    for c in scope["applicable_now"]:
        print(f"  - {c}")
    print(f"\nDeferred until Stage 9 ({len(scope['deferred'])}):")
    for c in scope["deferred"]:
        print(f"  - {c}")
    print(f"Reason: {scope['deferred_reason']}")

    with open("threat_model_report.json", "w") as f:
        json.dump({"classification_result": result, "scope": scope}, f, indent=2)
    print("\nSaved: threat_model_report.json")