# 📦 Fouad Box - Complete Installation Guide

## 🎯 Quick Installation (Recommended)

```bash
cd /home/kali/Desktop/hh/fouadbox
sudo python3 install.py
sudo fouadbox
```

## 📋 Detailed Installation Steps

### Step 1: Verify Requirements

**Check Python version:**
```bash
python3 --version
# Should be 3.6 or higher
```

**Check if you're on Linux:**
```bash
uname -a
```

### Step 2: Navigate to Fouad Box Directory

```bash
cd /home/kali/Desktop/hh/fouadbox
```

### Step 3: Make Scripts Executable

```bash
chmod +x fouadbox.py install.py test_fouadbox.py update.sh uninstall.sh
```

### Step 4: Run Installation Script

```bash
sudo python3 install.py
```

The installer will:
- ✅ Check root privileges
- ✅ Detect your operating system
- ✅ Install system dependencies
- ✅ Install Python packages (rich, requests)
- ✅ Create symbolic link for easy access
- ✅ Set up the environment

### Step 5: Launch Fouad Box

```bash
sudo fouadbox
```

Or:

```bash
sudo python3 fouadbox.py
```

## 🔧 Manual Installation (Alternative)

If the automated installer doesn't work, try manual installation:

### For Debian/Ubuntu/Kali Linux:

```bash
# Update system
sudo apt-get update

# Install dependencies
sudo apt-get install -y python3 python3-pip git

# Install Python packages
pip3 install rich requests

# Make executable
chmod +x fouadbox.py

# Create symbolic link
sudo ln -sf $(pwd)/fouadbox.py /usr/local/bin/fouadbox

# Run
sudo fouadbox
```

### For Arch Linux:

```bash
# Update system
sudo pacman -Sy

# Install dependencies
sudo pacman -S --noconfirm python python-pip git

# Install Python packages
pip3 install rich requests

# Make executable
chmod +x fouadbox.py

# Create symbolic link
sudo ln -sf $(pwd)/fouadbox.py /usr/local/bin/fouadbox

# Run
sudo fouadbox
```

## 🐳 Docker Installation

### Build Docker Image:

```bash
cd /home/kali/Desktop/hh/fouadbox
docker build -t fouadbox:latest .
```

### Run with Docker Compose:

```bash
docker-compose up -d
docker exec -it fouadbox bash
fouadbox
```

### Run with Docker directly:

```bash
docker run -it --rm --privileged fouadbox:latest
```

## ✅ Verify Installation

Run the test script:

```bash
python3 test_fouadbox.py
```

This will check:
- Module imports
- Dependencies
- File structure

## 🔄 Post-Installation

### First Run Configuration

1. Launch Fouad Box:
   ```bash
   sudo fouadbox
   ```

2. Choose installation path:
   - **Option 1**: Custom path (e.g., `/opt/security-tools/`)
   - **Option 2**: Default path (`/home/fouadbox/`)

3. Start using tools!

### Add Shell Alias (Optional)

Add to `~/.bashrc` or `~/.zshrc`:

```bash
alias fb='sudo fouadbox'
alias fb-update='cd /home/kali/Desktop/hh/fouadbox && sudo ./update.sh'
alias fb-test='cd /home/kali/Desktop/hh/fouadbox && python3 test_fouadbox.py'
```

Then reload:
```bash
source ~/.bashrc
```

## 📝 Installation Locations

After installation, you'll have:

- **Main script**: `/home/kali/Desktop/hh/fouadbox/fouadbox.py`
- **Symbolic link**: `/usr/local/bin/fouadbox`
- **Tools directory**: Path you chose during setup
- **Config file**: `~/fouadboxpath.txt`

## 🔍 Troubleshooting

### Problem: "Permission denied"

**Solution:**
```bash
sudo python3 install.py
# Always use sudo
```

### Problem: "Module 'rich' not found"

**Solution:**
```bash
pip3 install rich requests
# or
sudo apt-get install python3-rich
```

### Problem: "Command 'fouadbox' not found"

**Solution:**
```bash
# Recreate symbolic link
sudo ln -sf /home/kali/Desktop/hh/fouadbox/fouadbox.py /usr/local/bin/fouadbox

# Or use full path
sudo python3 /home/kali/Desktop/hh/fouadbox/fouadbox.py
```

### Problem: "Python version too old"

**Solution:**
```bash
# Install Python 3.8+
sudo apt-get install python3.8
# or
sudo apt-get install python3.9
```

### Problem: Installation fails

**Solution:**
```bash
# Check logs
sudo python3 install.py 2>&1 | tee install.log

# Manual dependency installation
sudo apt-get update
sudo apt-get install -y python3 python3-pip git wget curl
pip3 install -r requirements.txt
```

## 🆕 Updating Fouad Box

```bash
cd /home/kali/Desktop/hh/fouadbox
sudo ./update.sh
```

Or manually:
```bash
cd /home/kali/Desktop/hh/fouadbox
git pull
pip3 install -r requirements.txt --upgrade
sudo python3 install.py
```

## 🗑️ Uninstalling Fouad Box

```bash
cd /home/kali/Desktop/hh/fouadbox
sudo ./uninstall.sh
```

Or manually:
```bash
# Remove symbolic link
sudo rm -f /usr/local/bin/fouadbox

# Remove config
rm -f ~/fouadboxpath.txt

# Remove directory
cd ..
rm -rf fouadbox
```

## 📞 Support

If you encounter issues:

- **Email**: zalaffouad37@gmail.com
- **Instagram**: [@1.pvl](https://instagram.com/1.pvl) | [@fod1v](https://instagram.com/fod1v)
- **Check**: README.md, QUICKSTART.md

## ✨ Next Steps

After successful installation:

1. Read the [Quick Start Guide](QUICKSTART.md)
2. Explore tool categories
3. Install your first tool
4. Set up a test environment
5. Start learning!

---

**Happy Hacking! 🔥**

*Author: Fouad Zulof*
