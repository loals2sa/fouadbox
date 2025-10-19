# 🚀 Fouad Box Quick Start Guide

Get up and running with Fouad Box in minutes!

## ⚡ Super Quick Install

```bash
git clone https://github.com/fouadzulof/fouadbox.git
cd fouadbox
sudo python3 install.py
sudo fouadbox
```

## 📋 Step-by-Step Guide

### Step 1: Install Fouad Box

```bash
# Clone the repository
git clone https://github.com/fouadzulof/fouadbox.git

# Navigate to directory
cd fouadbox

# Run installation
sudo python3 install.py
```

### Step 2: Launch Fouad Box

```bash
sudo fouadbox
```

Or alternatively:

```bash
sudo python3 fouadbox.py
```

### Step 3: Set Installation Path

On first run, choose where to install tools:
- **Option 1**: Custom path (e.g., `/opt/security-tools/`)
- **Option 2**: Default path (`/home/fouadbox/`)

**Recommendation**: Use the default path for simplicity.

### Step 4: Navigate the Menu

```
Main Menu
├── 0 - Reconnaissance & Information Gathering 🔍
├── 1 - Exploitation & Vulnerability Tools 💣
├── 2 - Web Application Security Tools 🌐
├── 3 - Wireless Network Security Tools 📡
├── 4 - Password Cracking & Wordlist Tools 🔓
├── 5 - Social Engineering & Phishing Tools 🎭
├── 6 - Anonymity & Privacy Tools 🕵️
├── 7 - Digital Forensics & Analysis Tools 🔬
└── 99 - Tool Management & Settings ⚙️
```

### Step 5: Install and Run Your First Tool

Example: Installing Nmap

1. Select category `0` (Reconnaissance)
2. Select tool `0` (Nmap)
3. Choose option `1` (Install)
4. Wait for installation to complete
5. Choose option `2` (Run)

## 🎯 Common Use Cases

### Case 1: Network Reconnaissance

```
Category: 0 (Reconnaissance)
Tool: 0 (Nmap)
Action: Install → Run
Command: nmap -sV target.com
```

### Case 2: Web Application Testing

```
Category: 2 (Web Security)
Tool: 1 (OWASP ZAP)
Action: Install → Run
```

### Case 3: Password Testing

```
Category: 4 (Password Tools)
Tool: 2 (Hydra)
Action: Install → Run
Command: hydra -l admin -P passwords.txt ssh://target.com
```

### Case 4: WiFi Security Audit

```
Category: 3 (Wireless Tools)
Tool: 0 (Aircrack-ng)
Action: Install → Run
```

## 💡 Pro Tips

### Tip 1: Update Regularly
```bash
cd fouadbox
git pull
sudo python3 install.py
```

### Tip 2: Use Custom Paths for Organization
Organize tools by project:
```
/opt/pentest-projects/
├── client1/
├── client2/
└── training/
```

### Tip 3: Create Aliases
Add to your `~/.bashrc` or `~/.zshrc`:
```bash
alias fb='sudo fouadbox'
alias fb-update='cd ~/fouadbox && git pull'
```

### Tip 4: Quick Tool Access
Some tools can be run directly after installation:
```bash
nmap -sV target.com
sqlmap -u "http://target.com/page?id=1"
hydra -l admin -P pass.txt ssh://target
```

### Tip 5: Combine with Other Tools
```bash
# Use Nmap with Fouad Box tools
nmap -sV target.com -oX scan.xml
# Import into Metasploit
```

## 🔧 Troubleshooting

### Problem: Permission Denied
**Solution**: Always run with `sudo`
```bash
sudo fouadbox
```

### Problem: Tool Not Found After Install
**Solution**: Reload shell or use full path
```bash
source ~/.bashrc
# or
/usr/bin/tool-name
```

### Problem: Installation Fails
**Solution**: Update system and install dependencies
```bash
sudo apt-get update
sudo apt-get install -y python3-pip git
pip3 install -r requirements.txt
```

### Problem: Python Version Too Old
**Solution**: Install Python 3.6+
```bash
sudo apt-get install python3.8
```

## 📚 Next Steps

1. **Read the Full README**: `cat README.md`
2. **Explore Tool Categories**: Try each category
3. **Learn Tools**: Read tool documentation
4. **Practice Ethically**: Set up a test lab
5. **Contribute**: Add your favorite tools

## ⚠️ Important Reminders

- ✅ **Always get written authorization** before testing
- ✅ **Use only on systems you own** or have permission to test
- ✅ **Keep tools updated** for latest features and security
- ✅ **Follow local laws** and regulations
- ❌ **Never use for illegal activities**

## 🆘 Getting Help

### Documentation
- **README**: Main documentation
- **CONTRIBUTING**: How to contribute
- **SECURITY**: Security policy
- **CHANGELOG**: Version history

### Community
- **GitHub Issues**: Report bugs or request features
- **Email**: zalaffouad37@gmail.com
- **Instagram**: [@1.pvl](https://instagram.com/1.pvl) | [@fod1v](https://instagram.com/fod1v)

## 🎓 Learning Resources

### Recommended Labs
- **HackTheBox**: https://hackthebox.eu
- **TryHackMe**: https://tryhackme.com
- **VulnHub**: https://vulnhub.com
- **PentesterLab**: https://pentesterlab.com

### Certifications
- **CEH**: Certified Ethical Hacker
- **OSCP**: Offensive Security Certified Professional
- **PNPT**: Practical Network Penetration Tester

### Books
- "The Web Application Hacker's Handbook"
- "Metasploit: The Penetration Tester's Guide"
- "The Hacker Playbook Series"

## 🎉 You're Ready!

You now have everything you need to start using Fouad Box. Remember to:
- Use responsibly and legally
- Keep learning and practicing
- Contribute to the community
- Have fun (ethically)!

**Happy Hacking! 🔥**

---

<div align="center">

**Made with ❤️ by Fouad Zulof**

[⬆ Back to Top](#-fouad-box-quick-start-guide)

</div>
