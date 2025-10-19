#!/bin/bash

# Fouad Box Update Script
# Author: Fouad Zulof

echo "╔══════════════════════════════════════════════════════════╗"
echo "║             FOUAD BOX UPDATE SCRIPT                      ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""
echo "Author: Fouad Zulof"
echo "Email: zalaffouad37@gmail.com"
echo ""

# Check if running as root
if [ "$EUID" -ne 0 ]; then
    echo "[!] Please run as root: sudo ./update.sh"
    exit 1
fi

echo "[*] Starting Fouad Box update..."
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "[!] Git is not installed. Installing..."
    apt-get update && apt-get install -y git
fi

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    echo "[!] This is not a git repository."
    echo "[*] Please run this script from the Fouad Box directory."
    exit 1
fi

# Stash local changes
echo "[*] Saving local changes..."
git stash

# Fetch updates
echo "[*] Fetching updates from repository..."
git fetch origin

# Check if updates are available
LOCAL=$(git rev-parse @)
REMOTE=$(git rev-parse @{u})

if [ $LOCAL = $REMOTE ]; then
    echo "[✓] Fouad Box is already up to date!"
else
    echo "[*] Updates available. Pulling changes..."
    git pull origin main || git pull origin master
    
    # Update Python dependencies
    echo "[*] Updating Python dependencies..."
    pip3 install -r requirements.txt --upgrade
    
    # Make scripts executable
    echo "[*] Setting permissions..."
    chmod +x fouadbox.py install.py update.sh uninstall.sh test_fouadbox.py
    
    # Update symbolic link
    echo "[*] Updating symbolic link..."
    ln -sf $(pwd)/fouadbox.py /usr/local/bin/fouadbox
    
    echo ""
    echo "╔══════════════════════════════════════════════════════════╗"
    echo "║            UPDATE COMPLETED SUCCESSFULLY! 🎉             ║"
    echo "╚══════════════════════════════════════════════════════════╝"
    echo ""
    echo "[✓] Fouad Box has been updated to the latest version!"
    echo "[*] Run 'sudo fouadbox' to start"
fi

echo ""
