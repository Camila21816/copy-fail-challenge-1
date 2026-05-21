# verificar_vuln.py
import socket

def check():
    try:
        # Intentamos conectar al socket AF_ALG
        s = socket.socket(socket.AF_ALG, socket.SOCK_SEQPACKET, 0)
        print("[!] Vulnerabilidad detectada: Socket AF_ALG accesible.")
    except Exception as e:
        print(f"[*] Sistema mitigado/parcheado: {e}")

if __name__ == "__main__":
    check()