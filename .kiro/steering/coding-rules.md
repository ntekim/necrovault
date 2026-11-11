# Steering Directives

- Always keep `internal/core/domain` and `internal/core/ports` completely free of external third-party imports.
- Ensure all byte-slicing methods in Go handle EOF and boundary offsets safely without panic.
- Ensure all emitted WebAssembly or HTML sandboxes default to strict Content Security Policy (`default-src 'self'`).
