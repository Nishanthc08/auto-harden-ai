import os
import subprocess
import json
from pathlib import Path

report = {}

def run_command(command):
    try:
        return subprocess.check_output(command, shell=True, text=True).strip()
    except subprocess.CalledProcessError:
        return "Command failed"

def check_ssh_config():
    ssh_config_path = "/etc/ssh/sshd_config"
    insecure = []

    if Path(ssh_config_path).exists():
        with open(ssh_config_path) as f:
            config = f.read()

        if "PermitRootLogin yes" in config:
            insecure.append("PermitRootLogin is enabled.")
        if "PasswordAuthentication yes" in config:
            insecure.append("Password authentication is enabled. Use SSH keys instead.")
        if "Protocol 1" in config:
            insecure.append("Using old SSH protocol version 1.")

    return insecure if insecure else ["SSH config appears secure."]

def check_firewall_status():
    status = run_command("ufw status")
    if "inactive" in status:
        return "UFW is not active. Enable firewall."
    return "UFW is active."

def check_world_writable_files():
    output = run_command("find / -type f -perm -0002 -ls 2>/dev/null | head -n 10")
    if output:
        return "World-writable files found:\n" + output
    return "No world-writable files found."

def check_users_with_uid_0():
    output = run_command("awk -F: '$3 == 0 { print $1 }' /etc/passwd")
    if output and output.strip() != "root":
        return f"Non-root users with UID 0: {output}"
    return "Only root has UID 0."

def check_sudoers_file():
    output = run_command("cat /etc/sudoers | grep -v '^#'")
    return output if output else "No unusual entries in sudoers."

def check_running_services():
    output = run_command("systemctl list-units --type=service --state=running")
    return output.splitlines()[:10] # return first 10 lines only

def collect_report():
    report['ssh_config_issues'] = check_ssh_config()
    report['firewall_status'] = check_firewall_status()
    report['world_writable_files'] = check_world_writable_files()
    report['uid_0_users'] = check_users_with_uid_0()
    report['sudoers_check'] = check_sudoers_file()
    report['running_services'] = check_running_services()

    os.makedirs("reports", exist_ok=True)
    with open("reports/latest_report.json", "w") as f:
        json.dump(report, f, indent=4)
    print("System scan complete. Report saved to reports/latest_report.json")

if __name__ == "__main__":
    collect_report()
