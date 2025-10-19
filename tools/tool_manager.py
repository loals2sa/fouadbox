from core import SecurityTool, SecurityToolsCollection
import os
import sys


class UpdateFouadBox(SecurityTool):
    TITLE = "Update Fouad Box"
    DESCRIPTION = "Update Fouad Box to the latest version"
    
    def __init__(self):
        super().__init__(installable=False, runnable=False)
        self.OPTIONS = [("Update", self.update)]
    
    def update(self):
        print("Updating Fouad Box...")
        os.system("git pull")
        print("Update complete!")


class UninstallFouadBox(SecurityTool):
    TITLE = "Uninstall Fouad Box"
    DESCRIPTION = "Remove Fouad Box from your system"
    
    def __init__(self):
        super().__init__(installable=False, runnable=False)
        self.OPTIONS = [("Uninstall", self.uninstall_fouadbox)]
    
    def uninstall_fouadbox(self):
        confirm = input("Are you sure you want to uninstall Fouad Box? (yes/no): ")
        if confirm.lower() == "yes":
            print("Uninstalling Fouad Box...")
            os.system("rm -rf ~/fouadboxpath.txt")
            print("Fouad Box has been uninstalled. You can manually remove the directory.")
        else:
            print("Uninstall cancelled.")


class AboutFouadBox(SecurityTool):
    TITLE = "About Fouad Box"
    DESCRIPTION = "Information about Fouad Box and its author"
    
    def __init__(self):
        super().__init__(installable=False, runnable=False)
        self.OPTIONS = [("Show Info", self.show_about)]
    
    def show_about(self):
        about_text = """
        ╔════════════════════════════════════════════════════════════╗
        ║                      FOUAD BOX v1.0                        ║
        ║              Advanced Security Toolkit                     ║
        ╚════════════════════════════════════════════════════════════╝
        
        Author: Fouad Zulof
        Email: zalaffouad37@gmail.com
        
        Social Media:
        📷 Instagram: @1.pvl
        📷 Instagram: @fod1v
        
        Description:
        Fouad Box is a comprehensive security toolkit designed for
        penetration testing, security auditing, and ethical hacking.
        It includes a wide range of tools organized into categories
        for reconnaissance, exploitation, web security, wireless
        security, password cracking, social engineering, anonymity,
        and digital forensics.
        
        ⚠️  LEGAL DISCLAIMER:
        This tool is for educational and authorized security testing
        purposes only. Unauthorized access to computer systems is illegal.
        The author is not responsible for any misuse of this tool.
        
        ╔════════════════════════════════════════════════════════════╗
        ║           Thank you for using Fouad Box! 🔥                ║
        ╚════════════════════════════════════════════════════════════╝
        """
        print(about_text)


class ToolManager(SecurityToolsCollection):
    TITLE = "Tool Management"
    DESCRIPTION = "Update, uninstall, or get information about Fouad Box"
    TOOLS = [
        UpdateFouadBox(),
        UninstallFouadBox(),
        AboutFouadBox()
    ]
