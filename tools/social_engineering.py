from core import SecurityTool, SecurityToolsCollection


class SET(SecurityTool):
    TITLE = "Social Engineering Toolkit (SET)"
    DESCRIPTION = "Open-source penetration testing framework for social-engineering"
    INSTALL_COMMANDS = [
        "git clone https://github.com/trustedsec/social-engineer-toolkit.git",
        "cd social-engineer-toolkit && pip3 install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd social-engineer-toolkit && sudo python3 setoolkit"]
    PROJECT_URL = "https://github.com/trustedsec/social-engineer-toolkit"


class Gophish(SecurityTool):
    TITLE = "Gophish - Phishing Framework"
    DESCRIPTION = "Open-source phishing simulation framework"
    INSTALL_COMMANDS = [
        "wget https://github.com/gophish/gophish/releases/download/v0.12.1/gophish-v0.12.1-linux-64bit.zip",
        "unzip gophish-v0.12.1-linux-64bit.zip -d gophish",
        "chmod +x gophish/gophish"
    ]
    RUN_COMMANDS = ["cd gophish && ./gophish"]
    PROJECT_URL = "https://getgophish.com"


class HiddenEye(SecurityTool):
    TITLE = "HiddenEye - Advanced Phishing Tool"
    DESCRIPTION = "Modern phishing tool with advanced functionality"
    INSTALL_COMMANDS = [
        "git clone https://github.com/DarkSecDevelopers/HiddenEye.git",
        "cd HiddenEye && pip3 install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd HiddenEye && python3 HiddenEye.py"]
    PROJECT_URL = "https://github.com/DarkSecDevelopers/HiddenEye"


class King_Phisher(SecurityTool):
    TITLE = "King Phisher"
    DESCRIPTION = "Phishing campaign toolkit for testing and promoting user awareness"
    INSTALL_COMMANDS = [
        "wget -q https://github.com/rsmusllp/king-phisher/raw/master/tools/install.sh",
        "sudo bash install.sh"
    ]
    RUN_COMMANDS = ["king-phisher"]
    PROJECT_URL = "https://github.com/rsmusllp/king-phisher"


class SocialEngineeringTools(SecurityToolsCollection):
    TITLE = "Social Engineering & Phishing Tools"
    DESCRIPTION = "Advanced social engineering and phishing simulation tools"
    TOOLS = [
        SET(),
        Gophish(),
        HiddenEye(),
        King_Phisher()
    ]
