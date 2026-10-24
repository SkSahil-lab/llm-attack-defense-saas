import requests
import time

OLLAMA_URL = "http://localhost:11434"
MODEL = "llama3.2:1b"
KEEP_ALIVE = "30s"  # unload the model 30s after each call (ROE section 5, rule 3)

def installed_models():
    r = requests.get(f"{OLLAMA_URL}/api/tags", timeout=5)
    r.raise_for_status()
    return [m["name"] for m in r.json().get("models", [])]

def ask(prompt):
    start = time.time()
    r = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={"model": MODEL, "prompt": prompt, "stream": False, "keep_alive": KEEP_ALIVE},
        timeout=120,
    )
    r.raise_for_status()
    return r.json()["response"], round(time.time() - start, 2)

if __name__ == "__main__":
    models = installed_models()
    print("Installed models:", models)
    assert any(MODEL in m for m in models), f"{MODEL} is not installed"
    reply, seconds = ask("Say hello in one sentence.")
    print(f"Reply ({seconds}s): {reply}")