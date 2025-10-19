from core import SecurityTool, SecurityToolsCollection


class Aircrack_ng(SecurityTool):
    TITLE = "Aircrack-ng Suite"
    DESCRIPTION = "Complete suite of tools to assess WiFi network security"
    INSTALL_COMMANDS = ["sudo apt-get install -y aircrack-ng"]
    RUN_COMMANDS = ["aircrack-ng --help"]
    PROJECT_URL = "https://www.aircrack-ng.org"


class Wifite(SecurityTool):
    TITLE = "Wifite - Automated Wireless Auditor"
    DESCRIPTION = "Automated wireless attack tool for Linux"
    INSTALL_COMMANDS = [
        "git clone https://github.com/derv82/wifite2.git",
        "cd wifite2 && sudo python3 setup.py install"
    ]
    RUN_COMMANDS = ["sudo wifite"]
    PROJECT_URL = "https://github.com/derv82/wifite2"


class Reaver(SecurityTool):
    TITLE = "Reaver - WPS Attack Tool"
    DESCRIPTION = "Brute force attack against WiFi Protected Setup"
    INSTALL_COMMANDS = ["sudo apt-get install -y reaver"]
    RUN_COMMANDS = ["reaver -h"]
    PROJECT_URL = "https://github.com/t6x/reaver-wps-fork-t6x"


class Fern(SecurityTool):
    TITLE = "Fern WiFi Cracker"
    DESCRIPTION = "Wireless security auditing and attack software"
    INSTALL_COMMANDS = ["sudo apt-get install -y fern-wifi-cracker"]
    RUN_COMMANDS = ["sudo fern-wifi-cracker"]
    PROJECT_URL = "https://github.com/savio-code/fern-wifi-cracker"


class Wireshark(SecurityTool):
    TITLE = "Wireshark - Network Protocol Analyzer"
    DESCRIPTION = "The world's foremost network protocol analyzer"
    INSTALL_COMMANDS = ["sudo apt-get install -y wireshark"]
    RUN_COMMANDS = ["sudo wireshark"]
    PROJECT_URL = "https://www.wireshark.org"


class WirelessTools(SecurityToolsCollection):
    TITLE = "Wireless Network Security Tools"
    DESCRIPTION = "Advanced tools for wireless network penetration testing"
    TOOLS = [
        Aircrack_ng(),
        Wifite(),
        Reaver(),
        Fern(),
        Wireshark()
    ]
