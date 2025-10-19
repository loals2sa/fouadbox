from core import SecurityTool, SecurityToolsCollection


class Nmap(SecurityTool):
    TITLE = "Nmap - Network Scanner"
    DESCRIPTION = "The industry standard network mapper for security auditing and network discovery"
    INSTALL_COMMANDS = ["sudo apt-get install -y nmap"]
    RUN_COMMANDS = ["nmap --help"]
    PROJECT_URL = "https://nmap.org"


class Recon_ng(SecurityTool):
    TITLE = "Recon-ng - Web Reconnaissance Framework"
    DESCRIPTION = "A full-featured Web Reconnaissance framework written in Python"
    INSTALL_COMMANDS = [
        "git clone https://github.com/lanmaster53/recon-ng.git",
        "cd recon-ng && pip3 install -r REQUIREMENTS"
    ]
    RUN_COMMANDS = ["cd recon-ng && ./recon-ng"]
    PROJECT_URL = "https://github.com/lanmaster53/recon-ng"


class TheHarvester(SecurityTool):
    TITLE = "TheHarvester - OSINT Gathering"
    DESCRIPTION = "E-mails, subdomains and names harvester - OSINT"
    INSTALL_COMMANDS = [
        "git clone https://github.com/laramies/theHarvester.git",
        "cd theHarvester && pip3 install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd theHarvester && python3 theHarvester.py -h"]
    PROJECT_URL = "https://github.com/laramies/theHarvester"


class Sherlock(SecurityTool):
    TITLE = "Sherlock - Hunt Social Media Accounts"
    DESCRIPTION = "Hunt down social media accounts by username across social networks"
    INSTALL_COMMANDS = [
        "git clone https://github.com/sherlock-project/sherlock.git",
        "cd sherlock && pip3 install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd sherlock && python3 sherlock --help"]
    PROJECT_URL = "https://github.com/sherlock-project/sherlock"


class Sublist3r(SecurityTool):
    TITLE = "Sublist3r - Subdomain Enumeration"
    DESCRIPTION = "Fast subdomains enumeration tool for penetration testers"
    INSTALL_COMMANDS = [
        "git clone https://github.com/aboul3la/Sublist3r.git",
        "cd Sublist3r && pip3 install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd Sublist3r && python3 sublist3r.py -h"]
    PROJECT_URL = "https://github.com/aboul3la/Sublist3r"


class ReconnaissanceTools(SecurityToolsCollection):
    TITLE = "Reconnaissance & Information Gathering"
    DESCRIPTION = "Advanced OSINT and reconnaissance tools for information gathering"
    TOOLS = [
        Nmap(),
        TheHarvester(),
        Recon_ng(),
        Sherlock(),
        Sublist3r()
    ]
