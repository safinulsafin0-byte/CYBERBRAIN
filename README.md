<div align="center">

# 🧠 CYBERBRAIN (v1.0.0)
### Terminal-Native Modular AI Engine for Modern C++ & Cybersecurity

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Architecture: Dynamic MoE](https://img.shields.io/badge/Architecture-Dynamic%20MoE-red.svg)]()
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Safinul-yellow)](https://huggingface.co/Safinul)

**CYBERBRAIN** is a modular Mixture-of-Experts (MoE) CLI engine purpose-built for high-performance C++ algorithmic logic, kernel internals, binary exploitation, and active cyber defense.

</div>

---

## ⚡ Overview

General-purpose code LLMs often hallucinate low-level systems logic, modern C++ idioms, kernel primitives, and binary analysis routines. **CYBERBRAIN** solves this using a **7-Phase Mixture-of-Experts (MoE)** architecture. 

It routes domain-specific technical queries to specialized fine-tuned models on demand and actively flushes device memory between swaps, running seamlessly on consumer hardware.

---

## 🚀 The 7 Specialized Sub-Brains

| Phase | Expert Sub-Brain | Domain Specialization | Public Hugging Face Weights |
|:---:|:---|:---|:---|
| **01** | **Algo & Core Logic** | Modern C++ (C++20/23), STL, DP, Trees, Graph Algorithms, Complexity Optimization | [`Safinul/CYBERBRAIN-14M`](https://huggingface.co/Safinul/CYBERBRAIN-14M) |
| **02** | **Systems & Memory** | POSIX system APIs, Memory Safety, Bounds Enforcement, Concurrency & Threads | [`Safinul/CYBERBRAIN-PHASE2-FINAL`](https://huggingface.co/Safinul/CYBERBRAIN-PHASE2-FINAL) |
| **03** | **Network & Protocols** | Raw Sockets, Packet Crafting, Scapy, PCAP Deep Packet Inspection, Protocol Internals | [`Safinul/CYBERBRAIN-PHASE3-FINAL`](https://huggingface.co/Safinul/CYBERBRAIN-PHASE3-FINAL) |
| **04** | **Web Application Security** | Injections (SQLi/XSS/SSTI), Parameter Tampering, Logic Flaws, JWT & AppSec Sanitization | [`Safinul/CYBERBRAIN-PHASE4-FINAL`](https://huggingface.co/Safinul/CYBERBRAIN-PHASE4-FINAL) |
| **05** | **Kernel & Cryptography** | eBPF bytecode, Syscall Tracing, gVisor Sandboxing, OpenSSL EVP Primitives, AES-GCM | [`Safinul/CYBERBRAIN-PHASE5-FINAL`](https://huggingface.co/Safinul/CYBERBRAIN-PHASE5-FINAL) |
| **06** | **Binary Reverse Engineering** | Capstone/Unicorn Disassembly, PE/ELF Header Parsing, ROP Chain Formulation, x86/ARM | [`Safinul/CYBERBRAIN-PHASE6-FINAL`](https://huggingface.co/Safinul/CYBERBRAIN-PHASE6-FINAL) |
| **07** | **Active Defense & Threat Intel** | High-fidelity YARA Rules, Sigma Detections, Volatility Memory Triage, Threat Hunting | [`Safinul/CYBERBRAIN-PHASE7-FINAL`](https://huggingface.co/Safinul/CYBERBRAIN-PHASE7-FINAL) |

---

## 🛠️ Installation

Clone the repository and install the CLI globally:

```bash
git clone [https://github.com/safinulsafin0-byte/CYBERBRAIN.git](https://github.com/safinulsafin0-byte/CYBERBRAIN.git)
cd CYBERBRAIN
pip install -r requirements.txt
pip install .
