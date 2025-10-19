#!/usr/bin/env python3
"""
Test script for Fouad Box
Verifies that all modules load correctly
"""

import sys
import os

def test_imports():
    """Test if all modules can be imported"""
    print("[*] Testing module imports...")
    
    try:
        import core
        print("  [✓] core module")
    except Exception as e:
        print(f"  [✗] core module: {e}")
        return False
    
    try:
        from tools import reconnaissance
        print("  [✓] reconnaissance module")
    except Exception as e:
        print(f"  [✗] reconnaissance module: {e}")
        return False
    
    try:
        from tools import exploitation
        print("  [✓] exploitation module")
    except Exception as e:
        print(f"  [✗] exploitation module: {e}")
        return False
    
    try:
        from tools import web_tools
        print("  [✓] web_tools module")
    except Exception as e:
        print(f"  [✗] web_tools module: {e}")
        return False
    
    try:
        from tools import wireless
        print("  [✓] wireless module")
    except Exception as e:
        print(f"  [✗] wireless module: {e}")
        return False
    
    try:
        from tools import password_tools
        print("  [✓] password_tools module")
    except Exception as e:
        print(f"  [✗] password_tools module: {e}")
        return False
    
    try:
        from tools import social_engineering
        print("  [✓] social_engineering module")
    except Exception as e:
        print(f"  [✗] social_engineering module: {e}")
        return False
    
    try:
        from tools import anonymity
        print("  [✓] anonymity module")
    except Exception as e:
        print(f"  [✗] anonymity module: {e}")
        return False
    
    try:
        from tools import forensics
        print("  [✓] forensics module")
    except Exception as e:
        print(f"  [✗] forensics module: {e}")
        return False
    
    try:
        from tools import tool_manager
        print("  [✓] tool_manager module")
    except Exception as e:
        print(f"  [✗] tool_manager module: {e}")
        return False
    
    return True

def test_dependencies():
    """Test if required dependencies are installed"""
    print("\n[*] Testing dependencies...")
    
    try:
        import rich
        print(f"  [✓] rich (version: {rich.__version__})")
    except ImportError:
        print("  [✗] rich - Please install: pip3 install rich")
        return False
    
    try:
        import requests
        print(f"  [✓] requests")
    except ImportError:
        print("  [✗] requests - Please install: pip3 install requests")
        return False
    
    return True

def test_file_structure():
    """Test if all required files exist"""
    print("\n[*] Testing file structure...")
    
    required_files = [
        "fouadbox.py",
        "core.py",
        "install.py",
        "requirements.txt",
        "README.md",
        "LICENSE",
    ]
    
    all_exist = True
    for filename in required_files:
        if os.path.exists(filename):
            print(f"  [✓] {filename}")
        else:
            print(f"  [✗] {filename} - MISSING")
            all_exist = False
    
    return all_exist

def main():
    print("=" * 60)
    print("        Fouad Box - Module Test Suite")
    print("=" * 60)
    
    results = []
    
    # Test imports
    results.append(("Module Imports", test_imports()))
    
    # Test dependencies
    results.append(("Dependencies", test_dependencies()))
    
    # Test file structure
    results.append(("File Structure", test_file_structure()))
    
    # Summary
    print("\n" + "=" * 60)
    print("                   TEST SUMMARY")
    print("=" * 60)
    
    all_passed = True
    for test_name, passed in results:
        status = "[✓] PASSED" if passed else "[✗] FAILED"
        print(f"{test_name:.<30} {status}")
        if not passed:
            all_passed = False
    
    print("=" * 60)
    
    if all_passed:
        print("\n[✓] All tests passed! Fouad Box is ready to use.")
        print("[*] Run 'sudo python3 fouadbox.py' to start")
        return 0
    else:
        print("\n[✗] Some tests failed. Please fix the issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
