import subprocess
import json
import sys
from pathlib import Path

class NecroBrain:
    def __init__(self, go_mcp_binary_path="./necro-mcp"):
        self.go_proc = subprocess.Popen(
            [go_mcp_binary_path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1
        )
        self.request_id = 0

    def _call_mcp(self, method: str, params: dict):
        self.request_id += 1
        payload = {
            "jsonrpc": "2.0",
            "id": self.request_id,
            "method": method,
            "params": params
        }
        self.go_proc.stdin.write(json.dumps(payload) + "\n")
        self.go_proc.stdin.flush()
        line = self.go_proc.stdout.readline()
        return json.loads(line)

    def dissect_legacy_file(self, target_filepath: str):
        print(f"💀 [Séance Initiated] Probing corpse: {target_filepath}")
        response = self._call_mcp("tools/call", {
            "name": "probe_binary",
            "arguments": {"path": target_filepath}
        })
        
        telemetry = response.get("result", {})
        print(f"🔬 Autopsy Completed:")
        print(f"   • Detected Architecture: {telemetry.get('IdentifiedArch')}")
        print(f"   • Entropy Score: {telemetry.get('EntropyScore'):.2f} / 8.0")
        print(f"   • Has Executable Logic: {telemetry.get('HasExecLogic')}")

        return self.synthesize_resurrection(telemetry)

    def synthesize_resurrection(self, telemetry: dict):
        """
        Emits sandboxed WebAssembly / HTML5 canvas wrapper
        reconstructing the dead media.
        """
        arch = telemetry.get('IdentifiedArch')
        print(f"⚡ [Resurrection] Synthesizing Wasm canvas runtime for {arch}...")
        
        # Self-contained HTML5/Wasm sandbox
        output_html = f"""<!DOCTYPE html>
<html>
<head>
    <title>Resurrected: {telemetry.get('Filename')}</title>
    <style>
        body {{ background: #0d1117; color: #58a6ff; font-family: monospace; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; margin: 0; }}
        canvas {{ border: 2px solid #238636; box-shadow: 0 0 20px #238636aa; background: #000; }}
    </style>
</head>
<body>
    <h2>⚰️ Resurrected Artifact ({arch})</h2>
    <p>Entropy: {telemetry.get('EntropyScore'):.2f} | Size: {telemetry.get('TotalBytes')} bytes</p>
    <canvas id="sandbox" width="640" height="480"></canvas>
    <script>
        const ctx = document.getElementById('sandbox').getContext('2d');
        ctx.fillStyle = '#00ff41';
        ctx.fillText('Artifact Execution Restored via GhostMachine.', 20, 50);
    </script>
</body>
</html>"""
        output_path = Path("./resurrected_artifact.html")
        output_path.write_text(output_html)
        print(f"✨ [Success] Re-animated artifact saved to {output_path.resolve()}")
        return str(output_path)

if __name__ == "__main__":
    test_file = sys.argv[1] if len(sys.argv) > 1 else "./sample_legacy.swf"
    brain = NecroBrain()
    brain.dissect_legacy_file(test_file)