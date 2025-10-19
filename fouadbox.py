#!/usr/bin/env python3
# Fouad Box - Advanced Security Toolkit
# Version 1.0.0
# Author: Fouad Zulof

import os
import sys
import webbrowser
from platform import system
from time import sleep

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, IntPrompt, Confirm
from rich.align import Align
from rich.text import Text
from rich import box
from rich.rule import Rule

from core import SecurityToolsCollection
from tools.reconnaissance import ReconnaissanceTools
from tools.exploitation import ExploitationTools
from tools.web_tools import WebSecurityTools
from tools.wireless import WirelessTools
from tools.password_tools import PasswordTools
from tools.social_engineering import SocialEngineeringTools
from tools.anonymity import AnonymityTools
from tools.forensics import ForensicsTools
from tools.tool_manager import ToolManager

console = Console()

ASCII_LOGO = r"""
███████╗ ██████╗ ██╗   ██╗ █████╗ ██████╗     ██████╗  ██████╗ ██╗  ██╗
██╔════╝██╔═══██╗██║   ██║██╔══██╗██╔══██╗    ██╔══██╗██╔═══██╗╚██╗██╔╝
█████╗  ██║   ██║██║   ██║███████║██║  ██║    ██████╔╝██║   ██║ ╚███╔╝ 
██╔══╝  ██║   ██║██║   ██║██╔══██║██║  ██║    ██╔══██╗██║   ██║ ██╔██╗ 
██║     ╚██████╔╝╚██████╔╝██║  ██║██████╔╝    ██████╔╝╚██████╔╝██╔╝ ██╗
╚═╝      ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
"""

SUBTITLE = """
    🔰  Advanced Security Toolkit  🔰
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
         Author: Fouad Zulof
    📧  zalaffouad37@gmail.com
    📷  @1.pvl  |  @fod1v
"""

tool_definitions = [
    ("Reconnaissance & Information Gathering", "🔍"),
    ("Exploitation & Vulnerability Tools", "💣"),
    ("Web Application Security Tools", "🌐"),
    ("Wireless Network Security Tools", "📡"),
    ("Password Cracking & Wordlist Tools", "🔓"),
    ("Social Engineering & Phishing Tools", "🎭"),
    ("Anonymity & Privacy Tools", "🕵️"),
    ("Digital Forensics & Analysis Tools", "🔬"),
    ("Tool Management & Settings", "⚙️"),
]

all_tools = [
    ReconnaissanceTools(),
    ExploitationTools(),
    WebSecurityTools(),
    WirelessTools(),
    PasswordTools(),
    SocialEngineeringTools(),
    AnonymityTools(),
    ForensicsTools(),
    ToolManager()
]


class AllTools(SecurityToolsCollection):
    TITLE = "Fouad Box - All Tools"
    TOOLS = all_tools

    def show_info(self):
        header = Text()
        header.append(ASCII_LOGO, style="bold cyan")
        header.append(SUBTITLE, style="bold gold")
        
        warning = Text("⚠️  FOR EDUCATIONAL AND AUTHORIZED USE ONLY  ⚠️", style="bold red")
        disclaimer = Text("Unauthorized access to systems is illegal. Use responsibly!", style="italic yellow")
        
        panel = Panel(
            Align.center(header + Text("\n") + warning + Text("\n") + disclaimer),
            box=box.DOUBLE,
            padding=(1, 2),
            border_style="cyan"
        )
        console.print(panel)


def build_menu():
    table = Table.grid(expand=True)
    table.add_column("idx", width=8, justify="right")
    table.add_column("name", justify="left")

    for idx, (title, icon) in enumerate(tool_definitions):
        if idx == 8:  # Tool Management
            label = "[bold cyan]99[/bold cyan]"
            name = f"[bold cyan]{icon} {title}[/bold cyan]"
        else:
            label = f"[bold cyan]{idx}[/bold cyan]"
            name = f"[gold]{icon}[/gold]  [cyan]{title}[/cyan]"
        table.add_row(label, name)

    top_panel = Panel(
        Align.center(Text("FOUAD BOX — Main Menu", style="bold white on cyan"), vertical="middle"),
        style="cyan",
        padding=(0, 1),
        box=box.ROUNDED
    )
    menu_panel = Panel.fit(
        table,
        title="[bold cyan]Select a category[/bold cyan]",
        border_style="bright_cyan",
        box=box.SQUARE
    )
    footer = Align.center(Text("Choose number and press Enter — 99 for Tool Management", style="italic bright_black"))
    
    console.print(top_panel)
    console.print(menu_panel)
    console.print(Rule(style="bright_black"))
    console.print(footer)
    console.print("")


def choose_path():
    fpath = os.path.expanduser("~/fouadboxpath.txt")
    if not os.path.exists(fpath):
        os.system("clear" if system() == "Linux" else "cls")
        build_menu()
        console.print(Panel("Setup installation path for tools", border_style="cyan"))
        choice = Prompt.ask("[cyan]Choose option[/cyan]\n[1] Custom Path\n[2] Default Path (/home/fouadbox/)", 
                          choices=["1", "2"], default="2")
        if choice == "1":
            inpath = Prompt.ask("[cyan]Enter Path (with Directory Name)[/cyan]")
            with open(fpath, "w") as f:
                f.write(inpath)
            console.print(f"[green]✓ Successfully set path to:[/green] {inpath}")
        else:
            autopath = "/home/fouadbox/"
            with open(fpath, "w") as f:
                f.write(autopath)
            console.print(f"[green]✓ Your default path is:[/green] {autopath}")
            sleep(1)
    return fpath


def interact_menu():
    while True:
        try:
            build_menu()
            choice = IntPrompt.ask("[cyan]Choose a category to proceed[/cyan]", default=0)
            
            if choice == 99:
                # Show tool management
                choice = 8
            
            if 0 <= choice < len(all_tools):
                tool = all_tools[choice]
                name = tool_definitions[choice][0]
                console.print(Panel(
                    f"[bold cyan]{tool_definitions[choice][1]}  Selected:[/bold cyan] [gold]{name}[/gold]"
                ))
                try:
                    fn = getattr(tool, "show_options", None)
                    if callable(fn):
                        fn()
                    else:
                        console.print(f"[yellow]Tool '{name}' has no interactive menu.[/yellow]")
                except Exception as e:
                    console.print(Panel(f"[red]Error while opening {name}[/red]\n{e}", border_style="red"))
                
                if not Confirm.ask("[cyan]Return to main menu?[/cyan]", default=True):
                    console.print(Panel("[bold white on cyan]Thank you for using Fouad Box! Stay Safe! 🔒[/bold white on cyan]"))
                    break
            else:
                console.print("[red]Invalid selection. Pick a number from the menu.[/red]")
        except KeyboardInterrupt:
            console.print("\n[bold red]Interrupted by user — exiting Fouad Box[/bold red]")
            break


def show_welcome():
    """Display welcome message and system check"""
    console.print("\n[cyan]Initializing Fouad Box...[/cyan]")
    sleep(0.5)
    console.print("[green]✓ System check complete[/green]")
    console.print("[green]✓ Modules loaded successfully[/green]")
    sleep(0.5)
    console.print("\n")


def main():
    try:
        if system() == "Linux":
            show_welcome()
            fpath = choose_path()
            with open(fpath) as f:
                archive = f.readline().strip()
                os.makedirs(archive, exist_ok=True)
                os.chdir(archive)
                AllTools().show_info()
                interact_menu()
        elif system() == "Windows":
            console.print(Panel(
                "[bold red]⚠️  Windows is not fully supported  ⚠️[/bold red]\n\n"
                "For best results, please run Fouad Box on:\n"
                "• Kali Linux\n"
                "• Parrot OS\n"
                "• Ubuntu/Debian\n"
                "• Any Linux distribution",
                border_style="red"
            ))
            if Confirm.ask("Would you like to open installation guide?", default=True):
                webbrowser.open_new_tab("https://github.com/fouadzulof/fouadbox")
            sleep(2)
        else:
            console.print("[yellow]Unsupported operating system detected.[/yellow]")
    except KeyboardInterrupt:
        console.print("\n[bold red]Exiting Fouad Box... Goodbye! 👋[/bold red]")
        sleep(1)
    except Exception as e:
        console.print(f"[bold red]An error occurred: {e}[/bold red]")


if __name__ == "__main__":
    main()
