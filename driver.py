# Main driver program connecting logger and encryptor.

import sys
import subprocess

if len(sys.argv) != 2:
    print("Usage: controller.py <log_file>")
    sys.exit(1)

log_file = sys.argv[1]

logger_proc = subprocess.Popen(
    ['python', 'log_module.py', log_file],
    stdin=subprocess.PIPE,
    stdout=subprocess.DEVNULL,
    encoding='utf8'
)

encrypt_proc = subprocess.Popen(
    ['python', 'cipher_core.py'],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    encoding='utf8'
)