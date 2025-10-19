# Fouad Box - Project Structure

```
fouadbox/
├── 📁 fouadbox.py                 # Main application entry point
├── 📁 core.py                     # Core framework classes
├── 📁 install.py                  # Installation script
├── 📁 setup.py                    # Python package setup
├── 📁 __init__.py                 # Package initialization
│
├── 📁 tools/                      # Tool modules directory
│   ├── __init__.py
│   ├── reconnaissance.py          # OSINT & recon tools
│   ├── exploitation.py            # Exploitation frameworks
│   ├── web_tools.py               # Web security tools
│   ├── wireless.py                # Wireless attack tools
│   ├── password_tools.py          # Password cracking tools
│   ├── social_engineering.py      # Social engineering tools
│   ├── anonymity.py               # Anonymity & privacy tools
│   ├── forensics.py               # Digital forensics tools
│   └── tool_manager.py            # Tool management utilities
│
├── 📁 images/                     # Project images
│   └── logo.txt                   # Logo placeholder
│
├── 📄 Documentation Files
│   ├── README.md                  # Main documentation
│   ├── QUICKSTART.md              # Quick start guide
│   ├── CONTRIBUTING.md            # Contribution guidelines
│   ├── CHANGELOG.md               # Version history
│   ├── SECURITY.md                # Security policy
│   └── PROJECT_STRUCTURE.md       # This file
│
├── 📄 Configuration Files
│   ├── requirements.txt           # Python dependencies
│   ├── .gitignore                 # Git ignore patterns
│   ├── .dockerignore              # Docker ignore patterns
│   ├── Dockerfile                 # Docker image definition
│   ├── docker-compose.yml         # Docker compose config
│   ├── MANIFEST.in                # Package manifest
│   └── LICENSE                    # MIT License
│
└── 📊 Project Statistics
    ├── Total Files: 25+
    ├── Python Modules: 11
    ├── Tool Categories: 8
    ├── Integrated Tools: 50+
    └── Lines of Code: 2000+
```

## Module Descriptions

### Core Modules

#### `fouadbox.py`
Main application entry point with:
- ASCII logo and branding
- Main menu interface
- Tool category navigation
- User interaction handling
- Path configuration

#### `core.py`
Framework foundation providing:
- `SecurityTool` base class
- `SecurityToolsCollection` base class
- Menu system utilities
- Screen clearing functions
- Input validation

#### `install.py`
Automated installation script:
- Root privilege checking
- OS detection
- Dependency installation
- Python package management
- Symbolic link creation

### Tool Modules

#### `reconnaissance.py`
Information gathering tools:
- Nmap - Network scanner
- TheHarvester - OSINT gathering
- Recon-ng - Reconnaissance framework
- Sherlock - Social media hunter
- Sublist3r - Subdomain enumeration

#### `exploitation.py`
Exploitation frameworks:
- Metasploit - Penetration testing framework
- SQLMap - SQL injection tool
- SearchSploit - Exploit database
- Commix - Command injection
- BeEF - Browser exploitation

#### `web_tools.py`
Web application security:
- Burp Suite - Web security toolkit
- OWASP ZAP - Web app scanner
- Nikto - Web server scanner
- Dirb - Directory bruteforcer
- WPScan - WordPress scanner
- XSSer - XSS framework

#### `wireless.py`
Wireless security testing:
- Aircrack-ng - WiFi security suite
- Wifite - Automated wireless auditor
- Reaver - WPS attack tool
- Fern - WiFi cracker
- Wireshark - Protocol analyzer

#### `password_tools.py`
Password cracking suite:
- John the Ripper - Password cracker
- Hashcat - Advanced password recovery
- THC-Hydra - Login cracker
- Medusa - Parallel password cracker
- Crunch - Wordlist generator
- CeWL - Custom wordlist creator

#### `social_engineering.py`
Social engineering tools:
- SET - Social Engineering Toolkit
- Gophish - Phishing framework
- HiddenEye - Phishing tool
- King Phisher - Phishing campaign toolkit

#### `anonymity.py`
Privacy and anonymity:
- Tor - Anonymous network
- ProxyChains - Proxy tunneling
- AnonSurf - Anonymous surfing
- MacChanger - MAC address spoofer
- I2P - Anonymous network layer

#### `forensics.py`
Digital forensics:
- Autopsy - Forensics platform
- Volatility - Memory forensics
- Bulk Extractor - Data extraction
- Binwalk - Firmware analysis
- Foremost - File recovery

#### `tool_manager.py`
Management utilities:
- Update Fouad Box
- Uninstall Fouad Box
- About information

## Architecture Overview

```
┌─────────────────────────────────────────┐
│         User Interface (Rich UI)        │
│         fouadbox.py - Main Menu         │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│      Core Framework (core.py)           │
│  ┌─────────────────────────────────┐   │
│  │   SecurityToolsCollection       │   │
│  └─────────────────────────────────┘   │
│  ┌─────────────────────────────────┐   │
│  │      SecurityTool               │   │
│  └─────────────────────────────────┘   │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│         Tool Categories                 │
│  ┌──────────────┐  ┌──────────────┐    │
│  │ Recon Tools  │  │  Exploit     │    │
│  └──────────────┘  └──────────────┘    │
│  ┌──────────────┐  ┌──────────────┐    │
│  │  Web Tools   │  │  Wireless    │    │
│  └──────────────┘  └──────────────┘    │
│         ... (8 categories total)        │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│      Individual Security Tools          │
│    (50+ integrated third-party tools)   │
└─────────────────────────────────────────┘
```

## Data Flow

1. **User launches** `fouadbox.py`
2. **Initialization** checks/creates installation path
3. **Main menu** displays categories
4. **User selects** category
5. **Category menu** shows available tools
6. **User selects** tool
7. **Tool options** displayed (Install/Run)
8. **Commands executed** via `os.system()`
9. **Results** shown to user
10. **Return** to menu or exit

## Technology Stack

- **Language**: Python 3.6+
- **UI Framework**: Rich (terminal UI)
- **Package Management**: pip/apt/pacman
- **Containerization**: Docker
- **Version Control**: Git
- **License**: MIT

## Design Patterns

### 1. Template Method Pattern
`SecurityTool` class defines template with hooks:
- `before_install()` / `after_install()`
- `before_run()` / `after_run()`
- `before_uninstall()` / `after_uninstall()`

### 2. Collection Pattern
`SecurityToolsCollection` groups related tools

### 3. Factory Pattern
Tool instances created in category modules

## File Naming Conventions

- **Python files**: `lowercase_with_underscores.py`
- **Documentation**: `UPPERCASE.md`
- **Config files**: `.lowercase` or `lowercase.ext`

## Author Information

**Fouad Zulof**
- Email: zalaffouad37@gmail.com
- Instagram: @1.pvl | @fod1v

## Version

Current: **v1.0.0** (Initial Release)

---

*Last Updated: 2024-10-20*
