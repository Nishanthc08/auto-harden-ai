from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich import box
import json
from pathlib import Path

console = Console()

def load_json(path):
    try:
        with open(path) as f:
            return json.load(f)
    except FileNotFoundError:
        console.print(f"[bold red]Error:[/bold red] {path} not found.")
        return {}

def display_section(title, content):
    if isinstance(content, list):
        text = "\n".join(f"- {line}" for line in content)
    elif isinstance(content, str):
        text = content
    elif isinstance(content, dict):
        text = "\n".join(f"[bold cyan]{key}[/bold cyan]: {value}" for key, value in content.items())
    else:
        text = str(content)

    panel = Panel(text, title=f"[bold yellow]{title}[/bold yellow]", box=box.ROUNDED)
    console.print(panel)

def main():
    console.print("\n[bold green]AUTOHARDENAI - Terminal View[/bold green]\n", style="bold")

    report = load_json("reports/latest_report.json")
    suggestions = load_json("reports/suggestions.json")

    if not report or not suggestions:
        return

    console.rule("[bold red]System Scan Report")
    for section, data in report.items():
        display_section(section.replace("_", " ").title(), data)

    console.rule("[bold blue]AI Suggestions")
    for section, data in suggestions.items():
        display_section(section, data)

if __name__ == "__main__":
    main()
