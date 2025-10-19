from core import SecurityTool, SecurityToolsCollection


class Tor(SecurityTool):
    TITLE = "Tor - The Onion Router"
    DESCRIPTION = "Free software for enabling anonymous communication"
    INSTALL_COMMANDS = ["sudo apt-get install -y tor"]
    RUN_COMMANDS = ["sudo service tor start"]
    PROJECT_URL = "https://www.torproject.org"


class Proxychains(SecurityTool):
    TITLE = "ProxyChains - Proxy Tunneling"
    DESCRIPTION = "Force any TCP connection through proxy servers"
    INSTALL_COMMANDS = ["sudo apt-get install -y proxychains4"]
    RUN_COMMANDS = ["proxychains4"]
    PROJECT_URL = "https://github.com/haad/proxychains"


class AnonSurf(SecurityTool):
    TITLE = "AnonSurf - Anonymous Surfing"
    DESCRIPTION = "System-wide anonymous browsing through Tor"
    INSTALL_COMMANDS = [
        "git clone https://github.com/Und3rf10w/kali-anonsurf.git",
        "cd kali-anonsurf && sudo ./installer.sh"
    ]
    RUN_COMMANDS = ["sudo anonsurf start"]
    PROJECT_URL = "https://github.com/Und3rf10w/kali-anonsurf"


class MacChanger(SecurityTool):
    TITLE = "MacChanger - MAC Address Spoofer"
    DESCRIPTION = "Utility for manipulating network interface MAC addresses"
    INSTALL_COMMANDS = ["sudo apt-get install -y macchanger"]
    RUN_COMMANDS = ["macchanger --help"]
    PROJECT_URL = "https://github.com/alobbs/macchanger"


class I2P(SecurityTool):
    TITLE = "I2P - Invisible Internet Project"
    DESCRIPTION = "Anonymous network layer for secure communication"
    INSTALL_COMMANDS = ["sudo apt-get install -y i2p"]
    RUN_COMMANDS = ["i2prouter start"]
    PROJECT_URL = "https://geti2p.net"


class AnonymityTools(SecurityToolsCollection):
    TITLE = "Anonymity & Privacy Tools"
    DESCRIPTION = "Tools for anonymous and private online operations"
    TOOLS = [
        Tor(),
        Proxychains(),
        AnonSurf(),
        MacChanger(),
        I2P()
    ]
