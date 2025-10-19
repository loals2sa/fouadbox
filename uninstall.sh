#!/bin/bash

# Fouad Box Uninstallation Script
# Author: Fouad Zulof

echo "╔══════════════════════════════════════════════════════════╗"
echo "║          FOUAD BOX UNINSTALLATION SCRIPT                ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""
echo "Author: Fouad Zulof"
echo "Email: zalaffouad37@gmail.com"
echo ""

# Check if running as root
if [ "$EUID" -ne 0 ]; then
    echo "[!] Please run as root: sudo ./uninstall.sh"
    exit 1
fi

echo "[*] This will uninstall Fouad Box from your system."
echo ""
read -p "Are you sure you want to continue? (yes/no): " confirm

if [ "$confirm" != "yes" ]; then
    echo "[*] Uninstallation cancelled."
    exit 0
fi

echo ""
echo "[*] Starting uninstallation..."

# Remove symbolic link
if [ -f "/usr/local/bin/fouadbox" ]; then
    echo "[*] Removing symbolic link..."
    rm -f /usr/local/bin/fouadbox
    echo "[✓] Symbolic link removed"
fi

# Remove installation path file
if [ -f "$HOME/fouadboxpath.txt" ]; then
    echo "[*] Removing installation path file..."
    rm -f "$HOME/fouadboxpath.txt"
    echo "[✓] Path file removed"
fi

# Ask about removing installed tools
echo ""
read -p "Do you want to remove all installed tools? (yes/no): " remove_tools

if [ "$remove_tools" == "yes" ]; then
    if [ -f "$HOME/fouadboxpath.txt" ]; then
        TOOLS_PATH=$(cat "$HOME/fouadboxpath.txt")
        if [ -d "$TOOLS_PATH" ]; then
            echo "[*] Removing tools from $TOOLS_PATH..."
            rm -rf "$TOOLS_PATH"
            echo "[✓] Tools removed"
        fi
    fi
fi

# Ask about removing Fouad Box directory
echo ""
read -p "Do you want to remove the Fouad Box directory? (yes/no): " remove_dir

if [ "$remove_dir" == "yes" ]; then
    CURRENT_DIR=$(pwd)
    cd ..
    echo "[*] Removing Fouad Box directory..."
    rm -rf "fouadbox"
    echo "[✓] Directory removed"
else
    echo "[*] Fouad Box directory kept at: $(pwd)"
fi

echo ""
echo "╔══════════════════════════════════════════════════════════╗"
echo "║         UNINSTALLATION COMPLETED                         ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""
echo "Thank you for using Fouad Box!"
echo ""
echo "Contact: zalaffouad37@gmail.com"
echo "Instagram: @1.pvl | @fod1v"
echo ""
