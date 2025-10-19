#!/usr/bin/env python3
"""
Fouad Box Installation Script
Author: Fouad Zulof
Email: zalaffouad37@gmail.com
"""

import os
import sys
import subprocess
from time import sleep


def print_banner():
    banner = """
    ╔══════════════════════════════════════════════════════════╗
    ║           FOUAD BOX INSTALLATION SCRIPT                  ║
    ║                    Version 1.0                           ║
    ╚══════════════════════════════════════════════════════════╝
    
    Author: Fouad Zulof
    Email: zalaffouad37@gmail.com
    Instagram: @1.pvl | @fod1v
    
    """
    print(banner)


def check_root():
    """Check if script is running as root"""
    if os.geteuid() != 0:
        print("[!] This script must be run as root!")
        print("[*] Please run: sudo python3 install.py")
        sys.exit(1)
    print("[✓] Running as root")


def check_python_version():
    """Check Python version"""
    if sys.version_info < (3, 6):
        print("[!] Python 3.6 or higher is required!")
        sys.exit(1)
    print(f"[✓] Python {sys.version_info.major}.{sys.version_info.minor} detected")


def detect_os():
    """Detect operating system"""
    print("\n[*] Detecting operating system...")
    with open("/etc/os-release") as f:
        os_info = f.read().lower()
    
    if "kali" in os_info or "debian" in os_info or "ubuntu" in os_info:
        print("[✓] Debian-based system detected")
        return "debian"
    elif "arch" in os_info:
        print("[✓] Arch-based system detected")
        return "arch"
    elif "fedora" in os_info or "centos" in os_info or "rhel" in os_info:
        print("[✓] RedHat-based system detected")
        return "redhat"
    else:
        print("[!] Unknown operating system")
        return "unknown"


def install_dependencies(os_type):
    """Install required dependencies"""
    print("\n[*] Installing dependencies...")
    
    if os_type == "debian":
        commands = [
            "apt-get update",
            "apt-get install -y python3-pip",
            "apt-get install -y git",
            "apt-get install -y wget",
            "apt-get install -y curl"
        ]
    elif os_type == "arch":
        commands = [
            "pacman -Sy",
            "pacman -S --noconfirm python-pip",
            "pacman -S --noconfirm git",
            "pacman -S --noconfirm wget",
            "pacman -S --noconfirm curl"
        ]
    elif os_type == "redhat":
        commands = [
            "yum update -y",
            "yum install -y python3-pip",
            "yum install -y git",
            "yum install -y wget",
            "yum install -y curl"
        ]
    else:
        print("[!] Unsupported OS for automatic dependency installation")
        return False
    
    for cmd in commands:
        print(f"[*] Running: {cmd}")
        result = os.system(cmd)
        if result != 0:
            print(f"[!] Warning: Command failed: {cmd}")
    
    return True


def install_python_packages():
    """Install Python packages from requirements.txt"""
    print("\n[*] Installing Python packages...")
    
    if os.path.exists("requirements.txt"):
        result = os.system("pip3 install -r requirements.txt")
        if result == 0:
            print("[✓] Python packages installed successfully")
            return True
        else:
            print("[!] Error installing Python packages")
            return False
    else:
        print("[!] requirements.txt not found")
        return False


def create_symlink():
    """Create symbolic link for easy access"""
    print("\n[*] Creating symbolic link...")
    
    current_dir = os.getcwd()
    fouadbox_path = os.path.join(current_dir, "fouadbox.py")
    
    # Make the script executable
    os.chmod(fouadbox_path, 0o755)
    
    # Create symlink
    symlink_path = "/usr/local/bin/fouadbox"
    if os.path.exists(symlink_path):
        os.remove(symlink_path)
    
    try:
        os.symlink(fouadbox_path, symlink_path)
        print(f"[✓] Symbolic link created: {symlink_path}")
        return True
    except Exception as e:
        print(f"[!] Error creating symbolic link: {e}")
        return False


def show_completion_message():
    """Show installation completion message"""
    message = """
    ╔══════════════════════════════════════════════════════════╗
    ║         INSTALLATION COMPLETED SUCCESSFULLY! 🎉          ║
    ╚══════════════════════════════════════════════════════════╝
    
    To run Fouad Box, use either:
    
    1. sudo fouadbox          (from anywhere)
    2. sudo python3 fouadbox.py    (from this directory)
    
    ⚠️  IMPORTANT NOTES:
    • Always run Fouad Box as root (sudo)
    • Use only for educational and authorized purposes
    • Unauthorized access to systems is illegal
    
    📧 Contact: zalaffouad37@gmail.com
    📷 Instagram: @1.pvl | @fod1v
    
    Thank you for using Fouad Box! 🔥
    """
    print(message)


def main():
    print_banner()
    
    print("[*] Starting Fouad Box installation...\n")
    sleep(1)
    
    # Check requirements
    check_root()
    check_python_version()
    
    # Detect OS
    os_type = detect_os()
    
    # Install dependencies
    if os_type != "unknown":
        install_dependencies(os_type)
    
    # Install Python packages
    install_python_packages()
    
    # Create symlink
    create_symlink()
    
    # Show completion message
    print("\n")
    sleep(1)
    show_completion_message()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Installation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n[!] Installation failed: {e}")
        sys.exit(1)
