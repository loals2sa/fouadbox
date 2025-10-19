# 🔰 Fouad Box - Advanced Security Toolkit

<p align="center">
  <img src="https://img.shields.io/badge/Version-1.0.0-brightgreen" alt="Version">
  <img src="https://img.shields.io/badge/Python-3.6+-blue" alt="Python">
  <img src="https://img.shields.io/badge/Platform-Linux-orange" alt="Platform">
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License">
  <img src="https://img.shields.io/badge/Maintained-Yes-green" alt="Maintained">
</p>

<p align="center">
  <img src="./images/logo.svg" alt="Fouad Box Logo" width="400"/>
</p>

```
███████╗ ██████╗ ██╗   ██╗ █████╗ ██████╗     ██████╗  ██████╗ ██╗  ██╗
██╔════╝██╔═══██╗██║   ██║██╔══██╗██╔══██╗    ██╔══██╗██╔═══██╗╚██╗██╔╝
█████╗  ██║   ██║██║   ██║███████║██║  ██║    ██████╔╝██║   ██║ ╚███╔╝ 
██╔══╝  ██║   ██║██║   ██║██╔══██║██║  ██║    ██╔══██╗██║   ██║ ██╔██╗ 
██║     ╚██████╔╝╚██████╔╝██║  ██║██████╔╝    ██████╔╝╚██████╔╝██╔╝ ██╗
╚═╝      ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
```

<h2 align="center">🔥 The Ultimate All-in-One Security Testing Framework 🔥</h2>

---

## 📋 Table of Contents

- [About](#about)
- [Features](#features)
- [Tool Categories](#tool-categories)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Author](#author)
- [Legal Disclaimer](#legal-disclaimer)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 About

**Fouad Box** is a comprehensive, advanced security toolkit designed for penetration testers, security researchers, and ethical hackers. It provides a unified interface to access and manage over **50+ security tools** organized into 8 specialized categories.

Built with Python and featuring a beautiful Rich UI interface, Fouad Box streamlines your security testing workflow by providing easy access to industry-standard tools, automated installation, and intuitive navigation.

### ✨ Key Highlights

- 🎨 **Beautiful Rich UI** - Modern terminal interface with color-coded menus
- 🔧 **Automated Installation** - One-click installation for all tools
- 📦 **Modular Architecture** - Well-organized tool categories
- 🚀 **Easy to Use** - Intuitive menu-driven interface
- 🔄 **Regular Updates** - Continuously updated with new tools
- 💻 **Cross-Platform** - Supports all major Linux distributions

---

## 🚀 Features

- ✅ **50+ Security Tools** pre-configured and ready to use
- ✅ **8 Specialized Categories** for different security testing needs
- ✅ **Automated Tool Installation** with dependency management
- ✅ **Interactive Menu System** with Rich UI
- ✅ **Tool Update Management** built-in
- ✅ **Comprehensive Documentation** for each tool
- ✅ **Custom Installation Paths** support
- ✅ **Color-Coded Interface** for better navigation
- ✅ **Quick Access** via command-line shortcuts

---

## 🛠️ Tool Categories

### 🔍 1. Reconnaissance & Information Gathering
Advanced OSINT and reconnaissance tools for information gathering
- **Nmap** - Network mapper and port scanner
- **TheHarvester** - Email, subdomain, and name harvester
- **Recon-ng** - Web reconnaissance framework
- **Sherlock** - Hunt social media accounts by username
- **Sublist3r** - Fast subdomain enumeration tool

### 💣 2. Exploitation & Vulnerability Tools
Powerful exploitation frameworks and vulnerability testing tools
- **Metasploit Framework** - Penetration testing platform
- **SQLMap** - Automatic SQL injection tool
- **SearchSploit** - Exploit database search
- **Commix** - Command injection exploiter
- **BeEF** - Browser Exploitation Framework

### 🌐 3. Web Application Security Tools
Comprehensive web application security testing toolkit
- **Burp Suite** - Web security testing toolkit
- **OWASP ZAP** - Web application scanner
- **Nikto** - Web server scanner
- **Dirb** - Web content scanner
- **WPScan** - WordPress security scanner
- **XSSer** - Cross-site scripting framework

### 📡 4. Wireless Network Security Tools
Advanced tools for wireless network penetration testing
- **Aircrack-ng Suite** - WiFi security auditing tools
- **Wifite** - Automated wireless attack tool
- **Reaver** - WPS attack tool
- **Fern WiFi Cracker** - Wireless security auditing
- **Wireshark** - Network protocol analyzer

### 🔓 5. Password Cracking & Wordlist Tools
Powerful password cracking and wordlist generation tools
- **John the Ripper** - Password cracker
- **Hashcat** - Advanced password recovery
- **THC-Hydra** - Network login cracker
- **Medusa** - Speedy password cracker
- **Crunch** - Wordlist generator
- **CeWL** - Custom wordlist generator

### 🎭 6. Social Engineering & Phishing Tools
Advanced social engineering and phishing simulation tools
- **Social Engineering Toolkit (SET)** - SE framework
- **Gophish** - Phishing simulation platform
- **HiddenEye** - Advanced phishing tool
- **King Phisher** - Phishing campaign toolkit

### 🕵️ 7. Anonymity & Privacy Tools
Tools for anonymous and private online operations
- **Tor** - Anonymous communication network
- **ProxyChains** - Proxy tunneling tool
- **AnonSurf** - System-wide anonymous browsing
- **MacChanger** - MAC address spoofer
- **I2P** - Anonymous network layer

### 🔬 8. Digital Forensics & Analysis Tools
Comprehensive digital forensics and incident response tools
- **Autopsy** - Digital forensics platform
- **Volatility** - Memory forensics framework
- **Bulk Extractor** - Digital forensics tool
- **Binwalk** - Firmware analysis tool
- **Foremost** - File recovery tool

---

## 📥 Installation

### Prerequisites
- **Operating System**: Linux (Kali Linux, Parrot OS, Ubuntu, Debian, Arch, etc.)
- **Python**: Version 3.6 or higher
- **Root Access**: Required for installation

### Quick Install

```bash
# Clone the repository
git clone https://github.com/loals2sa/fouadbox.git

# Navigate to directory
cd fouadbox

# Give execute permissions
chmod +x fouadbox.py
chmod +x install.py

# Run installation script
sudo python3 install.py
```

### Manual Installation

```bash
# Install dependencies
sudo apt-get update
sudo apt-get install -y python3-pip git

# Install Python packages
pip3 install -r requirements.txt

# Make executable
chmod +x fouadbox.py

# Create symbolic link (optional)
sudo ln -s $(pwd)/fouadbox.py /usr/local/bin/fouadbox
```

---

## 🎮 Usage

### Running Fouad Box

After installation, you can run Fouad Box in two ways:

**Method 1: Using the command shortcut**
```bash
sudo fouadbox
```

**Method 2: Direct execution**
```bash
sudo python3 fouadbox.py
```

### First Run

On the first run, Fouad Box will ask you to set up an installation path for tools:
- **Option 1**: Custom path (specify your own directory)
- **Option 2**: Default path (`/home/fouadbox/`)

### Navigation

1. **Main Menu**: Select a category by entering its number
2. **Tool Selection**: Choose a specific tool from the category
3. **Tool Options**: Install, run, or get information about the tool
4. **Return**: Press 99 to go back or exit

### Example Workflow

```bash
# Start Fouad Box
sudo fouadbox

# Select category (e.g., 0 for Reconnaissance)
> 0

# Select tool (e.g., 0 for Nmap)
> 0

# Choose action (e.g., 1 to Install)
> 1

# Run the tool (e.g., 2 to Run)
> 2
```

---

## 📸 Screenshots

<p align="center">
  <img src="./images/main_menu.png" alt="Main Menu" width="700"/>
  <br><em>Main Menu Interface</em>
</p>

<p align="center">
  <img src="./images/tool_category.png" alt="Tool Category" width="700"/>
  <br><em>Tool Category Selection</em>
</p>

<p align="center">
  <img src="./images/tool_options.png" alt="Tool Options" width="700"/>
  <br><em>Tool Installation & Execution</em>
</p>

---

## 👨‍💻 Author

<div align="center">

### **Fouad Zulof**

Cybersecurity Enthusiast | Penetration Tester | Tool Developer

[![Email](https://img.shields.io/badge/Email-zalaffouad37%40gmail.com-red?style=for-the-badge&logo=gmail)](mailto:zalaffouad37@gmail.com)
[![Instagram](https://img.shields.io/badge/Instagram-%401.pvl-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/1.pvl)
[![Instagram](https://img.shields.io/badge/Instagram-%40fod1v-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/fod1v)

---

📧 **Email:** zalaffouad37@gmail.com  
📷 **Instagram:** [@1.pvl](https://instagram.com/1.pvl) | [@fod1v](https://instagram.com/fod1v)

</div>

---

## ⚖️ Legal Disclaimer

<div align="center">

### ⚠️ IMPORTANT - READ CAREFULLY ⚠️

</div>

**Fouad Box** is developed for **EDUCATIONAL PURPOSES ONLY**. This toolkit is designed to help security professionals, researchers, and students learn about cybersecurity and penetration testing in a legal and ethical manner.

### Legal Usage Guidelines

✅ **ALLOWED:**
- Educational purposes and learning
- Authorized security assessments
- Testing your own systems and networks
- Security research with proper authorization
- Penetration testing with written permission

❌ **PROHIBITED:**
- Unauthorized access to computer systems
- Attacking networks without permission
- Illegal activities of any kind
- Violating computer fraud and abuse laws
- Any malicious or harmful activities

### Your Responsibilities

By using Fouad Box, you agree to:
1. Use this tool only for legal and ethical purposes
2. Obtain proper authorization before testing any systems
3. Comply with all applicable laws and regulations
4. Take responsibility for your own actions
5. Not use this tool for malicious purposes

### Disclaimer

The author (**Fouad Zulof**) is **NOT RESPONSIBLE** for any misuse or damage caused by this tool. Use at your own risk and responsibility. Unauthorized access to computer systems is **ILLEGAL** and punishable by law.

Always ensure you have explicit written permission before conducting any security testing activities.

---

## 🤝 Contributing

Contributions are welcome! If you'd like to contribute to Fouad Box, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

### Contribution Guidelines

- Follow Python PEP 8 style guidelines
- Add proper documentation for new features
- Test your changes thoroughly
- Update README if necessary
- Ensure all tools work properly

---

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Fouad Zulof

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 🙏 Acknowledgments

Special thanks to all the developers and contributors of the security tools included in Fouad Box:
- Metasploit Team
- OWASP Foundation
- Aircrack-ng Team
- And all other amazing tool creators

---

## 📊 Project Stats

<p align="center">
  <img src="https://img.shields.io/github/stars/fouadzulof/fouadbox?style=social" alt="Stars">
  <img src="https://img.shields.io/github/forks/fouadzulof/fouadbox?style=social" alt="Forks">
  <img src="https://img.shields.io/github/issues/fouadzulof/fouadbox" alt="Issues">
  <img src="https://img.shields.io/github/last-commit/fouadzulof/fouadbox" alt="Last Commit">
</p>

---

## 🔗 Quick Links

- [Installation Guide](#installation)
- [Usage Guide](#usage)
- [Tool Categories](#tool-categories)
- [Legal Disclaimer](#legal-disclaimer)
- [Report Issues](https://github.com/fouadzulof/fouadbox/issues)

---

<div align="center">

### 🔥 Made with ❤️ by Fouad Zulof 🔥

**If you find this tool helpful, please give it a ⭐ on GitHub!**

[![Star](https://img.shields.io/github/stars/fouadzulof/fouadbox?style=social)](https://github.com/fouadzulof/fouadbox)

</div>

---

<p align="center">
  <strong>Happy Hacking! Stay Legal, Stay Ethical! 🛡️</strong>
</p>
