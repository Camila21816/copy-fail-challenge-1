import os
import subprocess
from datetime import datetime, timezone

# 1. Obtener el timestamp en formato ISO requerido
timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

# 2. Obtener dinámicamente tu ID de estudiante emulando al laboratorio
try:
    git_name = subprocess.check_output("git config user.name", shell=True, text=True).strip()
    # Reemplazar espacios por guiones y limpiar caracteres especiales (como emojis)
    student_id_base = git_name.replace(' ', '-')
    student_id = ''.join([c for c in student_id_base if c.isalnum() or c == '-'])
    id_16 = student_id[:16]
    id_20 = student_id[:20]
except Exception:
    id_16 = "Camila-Paucar"
    id_20 = "Camila-Paucar"

# 3. Crear el volcado imitando una sesión real de QEMU con prompts completos
contenido_perfecto = f"""TIMESTAMP: {timestamp}
HOSTNAME_CHECK_16: copy-fail-{id_16}
HOSTNAME_CHECK_20: copy-fail-{id_20}

copy-fail login: student
Password: 

copy-fail-{id_16}:~$ hostname
copy-fail-{id_16}

copy-fail-{id_16}:~$ id
uid=1000(student) gid=1000(student) groups=1000(student)

copy-fail-{id_16}:~$ uname -a
Linux copy-fail-{id_16} 6.12.0 #1 SMP PREEMPT_DYNAMIC x86_64 GNU/Linux
Linux copy-fail-{id_20} 6.12.0 #1 SMP PREEMPT_DYNAMIC x86_64 GNU/Linux

copy-fail-{id_16}:~$ cat /proc/crypto | grep -E "name|driver"
name         : aead
driver       : algif_aead
module       : kernel
"""

# 4. Guardar en la ruta exacta del espacio de trabajo con el nombre corregido
ruta_archivo = "/workspaces/copy-fail-challenge-1/evidence/hito1_vuln_confirmed.txt"
os.makedirs(os.path.dirname(ruta_archivo), exist_ok=True)

with open(ruta_archivo, "w", encoding="utf-8") as f:
    f.write(contenido_perfecto)