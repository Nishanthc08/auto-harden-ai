import json
from pathlib import Path

def load_report():
    report_path = Path("reports/latest_report.json")
    if not report_path.exists():
        raise FileNotFoundError("System scan report not found. Run system_scan.py first.")
    with open(report_path) as f:
        return json.load(f)

def generate_suggestions(report):
    suggestions = {}

    # SSH Config
    ssh_issues = report.get("ssh_config_issues", [])
    ssh_fixes = []
    for issue in ssh_issues:
        if "PermitRootLogin" in issue:
            ssh_fixes.append("Set `PermitRootLogin no` in /etc/ssh/sshd_config")
        if "PasswordAuthentication" in issue:
            ssh_fixes.append("Set `PasswordAuthentication no` to enforce key-based auth")
        if "Protocol 1" in issue:
            ssh_fixes.append("Use SSH protocol 2 only")

    suggestions["SSH Config"] = ssh_fixes if ssh_fixes else ["No action needed."]

    # Firewall
    fw = report.get("firewall_status", "")
    if "not active" in fw:
        suggestions["Firewall"] = ["Run `ufw enable` to activate firewall."]
    else:
        suggestions["Firewall"] = ["No action needed."]

    # World-writable files
    ww_files = report.get("world_writable_files", "")
    if "World-writable files found" in ww_files:
        suggestions["World-Writable Files"] = ["Manually audit listed files and remove write permissionswith `chmod o-w <file>`."]
    else:
        suggestions["World-Writable Files"] = ["No action needed."]

    # UID 0 Users
    uid0 = report.get("uid_0_users", "")
    if "Non-root" in uid0:
        suggestions["UID 0 Users"] = ["Remove UID 0 from non-root users unless absolutely necessary."]
    else:
        suggestions["UID 0 Users"] = ["No action needed."]

    # Sudoers
    sudoers = report.get("sudoers_check", "")
    if "ALL" in sudoers and "NOPASSWD" in sudoers:
        suggestions["Sudoers File"] = ["Avoid using NOPASSWD directive unless essential."]
    else:
        suggestions["Sudoers File"] = ["No action needed."]

    # Running services
    suggestions["Running Services"] = ["Review services listed in the report. Disable unnecessary ones using `systemctl disable <service>`"]

    return suggestions

def save_suggestions(suggestions):
    with open("reports/suggestions.json", "w") as f:
        json.dump(suggestions, f, indent=4)
    print("Suggestions saved to reports/suggestions.json")

if __name__ == "__main__":
    report = load_report()
    suggestions = generate_suggestions(report)
    save_suggestions(suggestions)
