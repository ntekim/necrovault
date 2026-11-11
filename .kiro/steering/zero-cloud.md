# Steering Directive: Air-Gapped Local Operation

- All file analysis, byte extraction, and compilation must execute locally on the host hardware or NAS.
- Do not import external cloud SDKs or upload file streams to third-party endpoints.
- Any generated sandboxes must run in self-contained WebAssembly environments.