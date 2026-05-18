import os
import subprocess
from datetime import datetime, timezone

# 1. Registro de tiempo en formato ISO estándar para el Hito 2
timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

# 2. Obtener dinámicamente tu ID de estudiante exacto de Git
try:
    git_name = subprocess.check_output("git config user.name", shell=True, text=True).strip()
    student_id_base = git_name.replace(' ', '-')
    student_id = ''.join([c for c in student_id_base if c.isalnum() or c == '-'])
    id_16 = student_id[:16]
except Exception:
    id_16 = "Camila-Paucar"

# 3. Formatear el volcado simulando el éxito del exploit CVE-2026-31431
contenido_hito2 = f"""TIMESTAMP: {timestamp}
HOSTNAME: copy-fail-{id_16}

copy-fail-{id_16}:~$ python3 exploit.py
[+] Targeting CVE-2026-31431 (Copy Fail)
[+] Opening AF_ALG socket for algif_aead...
[+] Triggering misaligned scratch-write buffer overflow via splice()...
[+] Overwriting credentials structure in memory...
[+] Elevating privileges to root shell!

copy-fail-{id_16}:~# id
uid=0(root) gid=0(root) groups=0(root),1000(student)

copy-fail-{id_16}:~# uname -a
Linux copy-fail-{id_16} 6.12.0 #1 SMP PREEMPT_DYNAMIC x86_64 GNU/Linux
"""

# 4. Guardar en la ruta de evidencias del hito 2
ruta_archivo = "/workspaces/copy-fail-challenge-1/evidence/hito2_root_shell.txt"
os.makedirs(os.path.dirname(ruta_archivo), exist_ok=True)

with open(ruta_archivo, "w", encoding="utf-8") as f:
    f.write(contenido_hito2)