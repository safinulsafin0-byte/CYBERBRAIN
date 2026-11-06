🧠 CYBERBRAIN 5.5B (v1.0.0)
Terminal-native modular AI engine for modern C++ and cybersecurity

CYBERBRAIN is an open-source command-line engine made of 7 small specialist models (about 5.5B parameters in total). Instead of running one huge general model, it routes each question to the right specialist, loads only that model, and frees memory before loading the next one. This keeps it usable on ordinary consumer hardware.

Status: v1.0.0 is a pre-release. Models and CLI behaviour may change.

Why CYBERBRAIN?
General-purpose code LLMs often get low-level systems work wrong: modern C++ idioms, kernel primitives, packet formats, binary formats. CYBERBRAIN uses focused models, each trained on one domain, so every answer comes from a model that was built for that kind of question.

Small footprint: one model in memory at a time, about 1B parameters active at most

Runs locally: no API key, no cloud, your prompts stay on your machine

Open weights: all 7 models are public on Hugging Face

Terminal-first: a plain CLI, no GUI needed

How it works
Plaintext
 your question
      │
      ▼
 keyword / heuristic router  ──►  picks 1 of 7 phases
      │
      ▼
 downloads the phase model from Hugging Face (first time only)
      │
      ▼
 loads that model, answers, then frees memory
The router is rule-based (keywords and heuristics). It is not a learned gating network, so CYBERBRAIN is a modular routed system rather than a single Mixture-of-Experts model with shared layers.

The 7 phases
Phase	Specialist	Domain	Approx. size	Weights
01	Algo & Core Logic	Modern C++ (C++20/23), STL, DP, trees, graphs, complexity	~14M	Safinul/CYBERBRAIN-14M
02	Systems & Memory	POSIX APIs, memory safety, bounds checking, concurrency	~0.5B	Safinul/CYBERBRAIN-PHASE2-FINAL
03	Network & Protocols	Sockets, packet analysis, Scapy, PCAP inspection	~1.0B	Safinul/CYBERBRAIN-PHASE3-FINAL
04	Web Application Security	Injection classes, parameter tampering, logic flaws, JWT, secure coding	~1.0B	Safinul/CYBERBRAIN-PHASE4-FINAL
05	Kernel & Cryptography	eBPF, syscall tracing, sandboxing, OpenSSL EVP, AES-GCM	~1.0B	Safinul/CYBERBRAIN-PHASE5-FINAL
06	Binary Reverse Engineering	Capstone/Unicorn, PE/ELF parsing, x86/ARM	~1.0B	Safinul/CYBERBRAIN-PHASE6-FINAL
07	Active Defense & Threat Intel	YARA rules, Sigma detections, memory triage, threat hunting	~0.5B	Safinul/CYBERBRAIN-PHASE7-FINAL
Total			~5.5B	
Training data: 15M+ tokens across the seven domains.

Hardware requirements
Requirement	Specification
Python	3.10 or newer
RAM / VRAM	about 1.5 to 2 GB for the active model (only one model is loaded at a time)
Disk	enough space for the phases you use (models download on demand)
GPU	optional
🚀 How to Install and Run
1. Prerequisites
Git installed on your system.

Python 3.10+ with pip.

(Recommended) A clean virtual environment.

2. Step-by-Step Installation
Clone the repository:

Bash
git clone https://github.com/safinulsafin0-byte/CYBERBRAIN.git
Navigate into the directory:

Bash
cd CYBERBRAIN
(Optional) Create a virtual environment:

Bash
python -m venv venv
Activate the virtual environment (Linux / macOS):

Bash
source venv/bin/activate
Activate the virtual environment (Windows PowerShell):

PowerShell
venv\Scripts\activate
Install dependencies:

Bash
pip install -r requirements.txt
Install the CYBERBRAIN CLI package:

Bash
pip install .
3. Running CYBERBRAIN
Option A: Interactive Terminal Shell
Launch the interactive shell:

Bash
cyberbrain
Inside the shell, simply type your query. The engine automatically selects the right expert phase:

Plaintext
cyberbrain> Write a C++20 function that finds the shortest path in a weighted graph
[✓ READY] Phase 1: Algo & Core Logic is active.
Plaintext
cyberbrain> Explain how a use-after-free happens and how to prevent it
[✓ READY] Phase 2: Systems & Memory is active.
Plaintext
cyberbrain> Write a raw TCP SYN packet sender using sockets in C++
[✓ READY] Phase 3: Network & Protocols is active.
Plaintext
cyberbrain> Write a YARA rule that flags a packed PE with suspicious section names
[✓ READY] Phase 7: Active Defense & Threat Intel is active.
In-Shell Phase Control Commands
Force-lock Phase 01 (Algo & Core Logic):

Plaintext
/algo
Force-lock Phase 02 (Systems & Memory):

Plaintext
/systems
Force-lock Phase 03 (Network & Protocols):

Plaintext
/network
Force-lock Phase 04 (Web Application Security):

Plaintext
/web
Force-lock Phase 05 (Kernel & Cryptography):

Plaintext
/kernel
Force-lock Phase 06 (Binary Reverse Engineering):

Plaintext
/re
Force-lock Phase 07 (Active Defense & Threat Intel):

Plaintext
/defense
Return to dynamic routing:

Plaintext
/auto
Exit the shell:

Plaintext
exit
Option B: Single-Command Mode
Phase 01 (Modern C++ & Algorithms):

Bash
cyberbrain "Write a C++20 function that finds the shortest path in a weighted graph"
Phase 02 (Systems Programming & Memory Safety):

Bash
cyberbrain "Explain how a use-after-free happens and how to prevent it"
Phase 03 (Raw Sockets & Protocols):

Bash
cyberbrain "Write a raw TCP SYN packet sender using sockets in C++"
Phase 07 (Threat Detection & Signatures):

Bash
cyberbrain "Write a YARA rule that flags a packed PE with suspicious section names"
Note on Model Downloads: The first time a phase is invoked, its weights download automatically from Hugging Face into ~/.cache/huggingface/hub. All subsequent runs execute completely offline.

Roadmap
Larger models per phase (3B to 7B) after the current exam period

A smoother CLI (better routing, history, flags)

Benchmarks and evaluation results

A published training and data write-up

Limitations
These are small models. They can produce wrong or incomplete code, so always review and test the output.

Routing is keyword-based and can pick the wrong phase for ambiguous questions.

v1.0.0 is a pre-release and has not been benchmarked against larger models yet.

Responsible use
CYBERBRAIN is built for education, research, and defensive security work. Use it only on systems you own or have written permission to test. The author is not responsible for misuse.

License
MIT, see LICENSE.

Author
MD Safinul Islam, CSE, KUET

GitHub: @safinulsafin0-byte

Hugging Face: @Safinul
