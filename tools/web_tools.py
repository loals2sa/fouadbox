from core import SecurityTool, SecurityToolsCollection


class BurpSuite(SecurityTool):
    TITLE = "Burp Suite Community"
    DESCRIPTION = "The leading web security testing toolkit"
    INSTALL_COMMANDS = ["sudo apt-get install -y burpsuite"]
    RUN_COMMANDS = ["burpsuite"]
    PROJECT_URL = "https://portswigger.net/burp"


class OWASP_ZAP(SecurityTool):
    TITLE = "OWASP ZAP - Web App Scanner"
    DESCRIPTION = "The world's most widely used web app scanner"
    INSTALL_COMMANDS = ["sudo apt-get install -y zaproxy"]
    RUN_COMMANDS = ["zaproxy"]
    PROJECT_URL = "https://www.zaproxy.org"


class Nikto(SecurityTool):
    TITLE = "Nikto - Web Server Scanner"
    DESCRIPTION = "Web server vulnerability scanner"
    INSTALL_COMMANDS = ["sudo apt-get install -y nikto"]
    RUN_COMMANDS = ["nikto -h"]
    PROJECT_URL = "https://cirt.net/Nikto2"


class Dirb(SecurityTool):
    TITLE = "Dirb - Web Content Scanner"
    DESCRIPTION = "Web content directory scanner and bruteforcer"
    INSTALL_COMMANDS = ["sudo apt-get install -y dirb"]
    RUN_COMMANDS = ["dirb"]
    PROJECT_URL = "http://dirb.sourceforge.net"


class WPScan(SecurityTool):
    TITLE = "WPScan - WordPress Security Scanner"
    DESCRIPTION = "Black box WordPress vulnerability scanner"
    INSTALL_COMMANDS = ["sudo apt-get install -y wpscan"]
    RUN_COMMANDS = ["wpscan --help"]
    PROJECT_URL = "https://wpscan.com"


class XSSer(SecurityTool):
    TITLE = "XSSer - Cross Site Scripting Framework"
    DESCRIPTION = "Automatic framework to detect, exploit and report XSS vulnerabilities"
    INSTALL_COMMANDS = [
        "git clone https://github.com/epsylon/xsser.git",
        "cd xsser && sudo python3 setup.py install"
    ]
    RUN_COMMANDS = ["xsser --help"]
    PROJECT_URL = "https://github.com/epsylon/xsser"


class WebSecurityTools(SecurityToolsCollection):
    TITLE = "Web Application Security Tools"
    DESCRIPTION = "Comprehensive web application security testing toolkit"
    TOOLS = [
        BurpSuite(),
        OWASP_ZAP(),
        Nikto(),
        Dirb(),
        WPScan(),
        XSSer()
    ]
