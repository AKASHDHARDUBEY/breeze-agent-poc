import subprocess

def run_command(cmd):
    print("\nRunning:", cmd)
    result = subprocess.run(cmd, shell=True)
    return result.returncode == 0
