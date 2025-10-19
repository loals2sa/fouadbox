from core import SecurityTool, SecurityToolsCollection


class Autopsy(SecurityTool):
    TITLE = "Autopsy - Digital Forensics Platform"
    DESCRIPTION = "Digital forensics platform and GUI for The Sleuth Kit"
    INSTALL_COMMANDS = ["sudo apt-get install -y autopsy"]
    RUN_COMMANDS = ["autopsy"]
    PROJECT_URL = "https://www.autopsy.com"


class Volatility(SecurityTool):
    TITLE = "Volatility - Memory Forensics"
    DESCRIPTION = "Advanced memory forensics framework"
    INSTALL_COMMANDS = [
        "git clone https://github.com/volatilityfoundation/volatility3.git",
        "cd volatility3 && pip3 install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd volatility3 && python3 vol.py -h"]
    PROJECT_URL = "https://www.volatilityfoundation.org"


class BulkExtractor(SecurityTool):
    TITLE = "Bulk Extractor - Digital Forensics"
    DESCRIPTION = "Stream-based forensic tool for extracting information"
    INSTALL_COMMANDS = ["sudo apt-get install -y bulk-extractor"]
    RUN_COMMANDS = ["bulk_extractor -h"]
    PROJECT_URL = "https://github.com/simsong/bulk_extractor"


class Binwalk(SecurityTool):
    TITLE = "Binwalk - Firmware Analysis"
    DESCRIPTION = "Firmware analysis tool for reverse engineering and extracting embedded files"
    INSTALL_COMMANDS = ["sudo apt-get install -y binwalk"]
    RUN_COMMANDS = ["binwalk -h"]
    PROJECT_URL = "https://github.com/ReFirmLabs/binwalk"


class Foremost(SecurityTool):
    TITLE = "Foremost - File Recovery"
    DESCRIPTION = "Console program to recover files based on their headers and footers"
    INSTALL_COMMANDS = ["sudo apt-get install -y foremost"]
    RUN_COMMANDS = ["foremost -h"]
    PROJECT_URL = "http://foremost.sourceforge.net"


class ForensicsTools(SecurityToolsCollection):
    TITLE = "Digital Forensics & Analysis Tools"
    DESCRIPTION = "Comprehensive digital forensics and incident response tools"
    TOOLS = [
        Autopsy(),
        Volatility(),
        BulkExtractor(),
        Binwalk(),
        Foremost()
    ]
