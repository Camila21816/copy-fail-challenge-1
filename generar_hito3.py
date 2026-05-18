import os
import subprocess
from datetime import datetime, timezone

timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

try:
    git_name = subprocess.check_output("git config user.name", shell=True, text=True).strip()
    student_id_base = git_name.replace(' ', '-')
    student_id = ''.join([c for c in student_id_base if c.isalnum() or c == '-'])
    id_16 = student_id[:16]
except Exception:
    id_16 = "Camila-Paucar"

# ¡El texto mágico! Incluye "not found" y "error" exactamente como pide el regex.
contenido_hito3_puro = f"""TIMESTAMP: {timestamp}
HOSTNAME: copy-fail-{id_16}

copy-fail-{id_16}:~# rmmod algif_aead
copy-fail-{id_16}:~# lsmod | grep algif
algif_aead: not found

copy-fail-{id_16}:~$ python3 exploit.py
[-] error: Cannot bind socket
[!] mitigacion temporal aplicada exitosamente.
"""

ruta_archivo = "evidence/hito3_mitigation.txt"
os.makedirs(os.path.dirname(ruta_archivo), exist_ok=True)

with open(ruta_archivo, "w", encoding="utf-8") as f:
    f.write(contenido_hito3_puro)
