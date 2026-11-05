#!/usr/bin/env python3
import sys
import gc
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer

EXPERTS = {
    "algo": {
        "repo": "Safinul/CYBERBRAIN-14M",
        "name": "Phase 1: Algorithms & Core Logic",
        "keywords": ["sort", "tree", "graph", "dp", "vector", "c++", "algorithm", "complexity", "pointer"]
    },
    "systems": {
        "repo": "Safinul/CYBERBRAIN-PHASE2-FINAL",
        "name": "Phase 2: Systems & Memory Safety",
        "keywords": ["malloc", "free", "buffer", "memory", "bounds", "posix", "thread", "concurrency", "leak"]
    },
    "network": {
        "repo": "Safinul/CYBERBRAIN-PHASE3-FINAL",
        "name": "Phase 3: Networking & Protocols",
        "keywords": ["socket", "pcap", "packet", "tcp", "udp", "scapy", "ethernet", "ip", "raw_socket"]
    },
    "web": {
        "repo": "Safinul/CYBERBRAIN-PHASE4-FINAL",
        "name": "Phase 4: Web Exploits & AppSec",
        "keywords": ["sqli", "xss", "jwt", "payload", "url", "http", "api", "sanitize", "injection", "parameter"]
    },
    "kernel": {
        "repo": "Safinul/CYBERBRAIN-PHASE5-FINAL",
        "name": "Phase 5: Kernel & Cryptography",
        "keywords": ["ebpf", "bpf", "kernel", "syscall", "openssl", "aes", "crypto", "seccomp", "gcm", "evp"]
    },
    "re": {
        "repo": "Safinul/CYBERBRAIN-PHASE6-FINAL",
        "name": "Phase 6: Binary Reverse Engineering",
        "keywords": ["capstone", "unicorn", "radare", "elf", "pe", "disassemble", "assembly", "rop", "x86", "arm"]
    },
    "defense": {
        "repo": "Safinul/CYBERBRAIN-PHASE7-FINAL",
        "name": "Phase 7: Threat Intelligence & Active Defense",
        "keywords": ["yara", "sigma", "volatility", "forensic", "incident", "malware", "detect", "hunting", "rule"]
    }
}

class CyberBrainEngine:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.active_key = None
        self.model = None
        self.tokenizer = None

    def route(self, text: str) -> str:
        t = text.lower()
        scores = {k: 0 for k in EXPERTS}
        for k, v in EXPERTS.items():
            for kw in v["keywords"]:
                if kw in t:
                    scores[k] += 1
        best = max(scores, key=scores.get)
        return best if scores[best] > 0 else "algo"

    def switch_expert(self, key: str):
        if self.active_key == key and self.model is not None:
            return

        info = EXPERTS[key]
        print(f"\n[🔄 ROUTER] Loading {info['name']} ({key.upper()})...")

        if self.model is not None:
            del self.model
            del self.tokenizer
            self.model = None
            self.tokenizer = None
            gc.collect()
            if torch.cuda.is_available():
                torch.cuda.empty_cache()

        try:
            self.tokenizer = AutoTokenizer.from_pretrained(info["repo"], trust_remote_code=True)
        except Exception:
            self.tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-Coder-0.5B", trust_remote_code=True)

        self.model = AutoModelForCausalLM.from_pretrained(
            info["repo"],
            dtype=torch.float32,
            device_map=self.device,
            trust_remote_code=True
        )
        self.model.eval()
        self.active_key = key
        print(f"[✓ READY] {info['name']} is active.\n")

    def run(self, prompt: str, override_expert: str = None, max_tokens: int = 512):
        target = override_expert if override_expert in EXPERTS else self.route(prompt)
        self.switch_expert(target)

        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        streamer = TextStreamer(self.tokenizer, skip_prompt=True, skip_special_tokens=True)

        print("-" * 60)
        with torch.no_grad():
            self.model.generate(
                **inputs,
                max_new_tokens=max_tokens,
                temperature=0.2,
                top_p=0.9,
                repetition_penalty=1.1,
                do_sample=True,
                pad_token_id=self.tokenizer.eos_token_id,
                streamer=streamer
            )
        print("-" * 60)

def main():
    engine = CyberBrainEngine()

    if len(sys.argv) > 1:
        user_prompt = " ".join(sys.argv[1:])
        engine.run(user_prompt)
        return

    print("=" * 60)
    print("  CYBERBRAIN: Modular Terminal AI for Cybersecurity & C++")
    print("  Type '/algo', '/web', '/kernel', etc. to force domains.")
    print("  Type '/auto' for dynamic routing. Type 'exit' to quit.")
    print(f"  Backend: [{engine.device.upper()}]")
    print("=" * 60)

    manual_mode = None
    while True:
        try:
            inp = input("\ncyberbrain> ").strip()
            if not inp:
                continue
            if inp.lower() in ["exit", "quit", "/bye"]:
                break
            if inp.startswith("/") and not inp.startswith("//"):
                cmd = inp[1:].lower().strip()
                if cmd in EXPERTS:
                    manual_mode = cmd
                    print(f"[*] Locked domain: {cmd.upper()}")
                    continue
                elif cmd == "auto":
                    manual_mode = None
                    print("[*] Dynamic auto-routing active.")
                    continue

            engine.run(inp, override_expert=manual_mode)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
