from core import SecurityTool, SecurityToolsCollection


class JohnTheRipper(SecurityTool):
    TITLE = "John the Ripper"
    DESCRIPTION = "The most popular password cracker"
    INSTALL_COMMANDS = ["sudo apt-get install -y john"]
    RUN_COMMANDS = ["john"]
    PROJECT_URL = "https://www.openwall.com/john/"


class Hashcat(SecurityTool):
    TITLE = "Hashcat - Advanced Password Recovery"
    DESCRIPTION = "World's fastest and most advanced password recovery utility"
    INSTALL_COMMANDS = ["sudo apt-get install -y hashcat"]
    RUN_COMMANDS = ["hashcat --help"]
    PROJECT_URL = "https://hashcat.net/hashcat/"


class Hydra(SecurityTool):
    TITLE = "THC-Hydra - Network Login Cracker"
    DESCRIPTION = "Parallelized login cracker which supports numerous protocols to attack"
    INSTALL_COMMANDS = ["sudo apt-get install -y hydra"]
    RUN_COMMANDS = ["hydra -h"]
    PROJECT_URL = "https://github.com/vanhauser-thc/thc-hydra"


class Medusa(SecurityTool):
    TITLE = "Medusa - Speedy Password Cracker"
    DESCRIPTION = "Fast, parallel, modular, login brute-forcer"
    INSTALL_COMMANDS = ["sudo apt-get install -y medusa"]
    RUN_COMMANDS = ["medusa -h"]
    PROJECT_URL = "http://www.foofus.net/goons/jmk/medusa/medusa.html"


class Crunch(SecurityTool):
    TITLE = "Crunch - Wordlist Generator"
    DESCRIPTION = "Generate custom wordlists from a character set"
    INSTALL_COMMANDS = ["sudo apt-get install -y crunch"]
    RUN_COMMANDS = ["crunch"]
    PROJECT_URL = "https://sourceforge.net/projects/crunch-wordlist/"


class CeWL(SecurityTool):
    TITLE = "CeWL - Custom Word List Generator"
    DESCRIPTION = "Spider websites to generate custom wordlists"
    INSTALL_COMMANDS = ["sudo apt-get install -y cewl"]
    RUN_COMMANDS = ["cewl --help"]
    PROJECT_URL = "https://github.com/digininja/CeWL"


class PasswordTools(SecurityToolsCollection):
    TITLE = "Password Cracking & Wordlist Tools"
    DESCRIPTION = "Powerful password cracking and wordlist generation tools"
    TOOLS = [
        JohnTheRipper(),
        Hashcat(),
        Hydra(),
        Medusa(),
        Crunch(),
        CeWL()
    ]
