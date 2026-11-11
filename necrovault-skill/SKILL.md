---
name: necrovault-archeology-engine
description: Autonomous on-premise legacy binary archeology and WebAssembly runtime resurrection skill for UGREEN AI NAS.
---

# NecroVault Archeology Engine

## 1. User Goal
Provide creative professionals, digital archivists, and NAS owners with an autonomous background skill that identifies unreadable or obsolete legacy media files (e.g., Macromedia Flash SWF, vintage Win32 PE, Macromedia Director), computes byte-level entropy, and synthesizes sandboxed, interactive WebAssembly canvases viewable directly within the UGOS desktop environment without cloud data leakage.

## 2. Required Inputs
- `watch_directory` (string): Absolute path on the UGREEN NAS filesystem to monitor for legacy media ingest.
- `output_directory` (string): Absolute path where reconstructed HTML5/WebAssembly interactive artifacts are saved.
- `entropy_threshold` (float): Sensitivity threshold between 0.0 and 8.0 to differentiate raw executable bytecode from compressed asset blocks (default: `7.1`).
- `memory_limit_pages` (integer): Maximum WebAssembly memory allocation in 64KB pages to ensure sandboxed containment (default: `16`).

## 3. Supported CLI Capabilities
The skill interacts with the following local NAS environment tools:
- `ugos-fs-watch`: Subscribes to directory write-complete events across mapped NAS storage volumes.
- `necro-cli`: Low-level compiled inspection utility providing sub-millisecond Shannon entropy scoring and magic byte slicing.
- `ugos-notify`: Pushes status alerts and direct interactive preview links to the UGOS desktop notification center.

## 4. Expert Agent Orchestration Workflow

[Dormant File Dropped on NAS]
│
▼
[ugos-fs-watch Event]
│
▼
[Byte Header Forensic Autopsy]
│
▼
[Shannon Entropy Scoring]
│
┌──────┴──────┐
▼ ▼
[High Entropy] [Low Entropy]
(Decompress) (Disassemble)
│ │
└──────┬──────┘
▼
[Agent Asset Reconstruction]
│
▼
[WebAssembly Sandbox Synthesis]
│
▼
[ugos-notify: Preview Ready]

1. **Ingest Detection:** Watches configured directories for incoming legacy archive files.
2. **Forensic Autopsy:** Extracts magic numbers, verifies container signatures, and computes byte entropy distribution.
3. **Cognitive Asset Recovery:** Orchestrates the reconstruction of damaged or obsolete headers and unpacks embedded vector assets.
4. **Wasm Sandbox Synthesis:** Emits a standalone, memory-bounded WebAssembly binary and HTML5 player wrapper.
5. **Notification:** Alerts the user with a direct launch link inside UGOS.

## 5. Completion and Failure Handling
- **Success:** Writes `[filename]_resurrected.html` to the destination directory and triggers a desktop notification.
- **Corrupted / Truncated Files:** If an archive contains invalid offsets or unrecoverable bit-rot, the file is safely tagged `.cadaver_unrecoverable`. An incident log is written, and the engine skips to the next file without panicking.
- **Resource Protection:** If host CPU or RAM utilization exceeds 80%, the orchestration agent throttles processing priority to guarantee zero degradation of primary NAS file services.

## 6. Disclosures & Attribution
- **Principal Functionality Developed for this Hackathon:** Hexagonal architecture domain, Shannon entropy algorithm, binary signature heuristics, WebAssembly binary header emitter, and Property-Based Test suites.
- **Third-Party Components & Libraries:** Standard Go Runtime (BSD-3-Clause), TinyGo Wasm target definitions (BSD-3-Clause).
- **AI Tools Used:** Kiro IDE used for Spec-Driven interface definitions, agent hook automation, and Model Context Protocol (MCP) tool integration.