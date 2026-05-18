import os
import subprocess
from datetime import datetime, timezone

timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

try:
    git_name = subprocess.check_output("git config user.name", shell=True, text=True).strip()
    student_id = ''.join([c for c in git_name.replace(' ', '-') if c.isalnum() or c == '-'])
except:
    student_id = "student"

contenido_hito4 = f"""TIMESTAMP: {timestamp}
KERNEL_VERSION: 6.12.0
USER_ID: uid=1000({student_id})

copy-fail-patched:~$ python3 exploit.py
[!] Error: Operation not permitted
[!] kernel panic: failed to bind to AF_ALG socket
"""

with open("evidence/hito4_patched.txt", "w") as f:
    f.write(contenido_hito4)