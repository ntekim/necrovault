import socket
import json
import sys

def start_reasoning_server(host="127.0.0.1", port=9999):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(5)
    print(f"🧠 [Kiro Python Brain] Listening for Go Engine telemetries on {host}:{port}...")

    while True:
        conn, addr = server.accept()
        try:
            data = conn.recv(4096).decode("utf-8")
            if not data:
                continue

            telemetry = json.loads(data)
            print(f"💀 [Reasoning Request Received] Target: {telemetry['filename']}")
            print(f"   • Arch: {telemetry['identified_arch']} | Entropy: {telemetry['entropy_score']:.2f}")

            # Synthesize Instruction Set Architecture (IR)
            ir_instructions = []
            if telemetry["identified_arch"] == "Adobe_Flash_SWF":
                ir_instructions = [
                    {"opcode": "ALLOC_VECTOR_CANVAS", "param": "640x480"},
                    {"opcode": "EMBED_DECOMPRESSED_ASSETS", "param": "zlib_stream"},
                    {"opcode": "RESTORE_ACTION_SCRIPT_1_LOOP", "param": "30fps"}
                ]
            else:
                ir_instructions = [
                    {"opcode": "INIT_CONSOLE_VGA", "param": "80x25"},
                    {"opcode": "HOOK_INTERRUPT_VECTOR", "param": "int_21h"}
                ]

            conn.sendall(json.dumps(ir_instructions).encode("utf-8"))
            print(f"⚡ Dispatched {len(ir_instructions)} semantic IR directives back to Go Compiler.")
        except Exception as e:
            print(f"❌ Error during reasoning cycle: {e}")
        finally:
            conn.close()

if __name__ == "__main__":
    start_reasoning_server()