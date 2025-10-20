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


def write_log(action, message=""):
    """Send an action/message line to the logger process."""
    if logger_proc.stdin:
        entry = f"{action} {message}".strip()
        logger_proc.stdin.write(entry + "\n")
        logger_proc.stdin.flush()


def send_encrypt_command(cmd):
    """Send command to encryptor and read its response."""
    if encrypt_proc.stdin:
        encrypt_proc.stdin.write(cmd + "\n")
        encrypt_proc.stdin.flush()
        response = encrypt_proc.stdout.readline()
        return response.strip()
    return None
