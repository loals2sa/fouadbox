# Security Policy

## Supported Versions

Currently supported versions of Fouad Box:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

The security of Fouad Box is taken seriously. If you discover a security vulnerability, please follow these steps:

### 1. Do Not Public Disclose

Please do not publicly disclose the vulnerability until it has been addressed. Public disclosure could put users at risk.

### 2. Contact Information

Report security vulnerabilities via email to:
- **Email**: zalaffouad37@gmail.com
- **Subject**: [SECURITY] Fouad Box Vulnerability Report

### 3. What to Include

Please include the following information in your report:

- **Description**: A clear description of the vulnerability
- **Impact**: What could an attacker potentially do?
- **Steps to Reproduce**: Detailed steps to reproduce the issue
- **Affected Versions**: Which versions are affected
- **Proposed Fix**: If you have suggestions for fixing the issue
- **Your Contact Info**: So we can follow up with questions

### 4. Response Time

- **Initial Response**: Within 48 hours
- **Status Update**: Within 7 days
- **Fix Timeline**: Depends on severity (critical issues within 30 days)

### 5. Recognition

Security researchers who responsibly disclose vulnerabilities will be:
- Acknowledged in the CHANGELOG (unless they prefer to remain anonymous)
- Listed in the project's security contributors
- Given credit for the discovery

## Security Best Practices

When using Fouad Box, please follow these security best practices:

### For Users

1. **Always run as root only when necessary**
2. **Use in isolated environments** (VMs or dedicated systems)
3. **Keep Fouad Box updated** to the latest version
4. **Verify tool sources** before installation
5. **Use strong passwords** for any services
6. **Enable logging** for audit trails
7. **Follow legal guidelines** and obtain proper authorization

### For Developers

1. **Code Review**: All contributions are reviewed for security issues
2. **Input Validation**: Always validate and sanitize user inputs
3. **Dependency Management**: Keep dependencies updated
4. **Secure Defaults**: Use secure default configurations
5. **Error Handling**: Don't expose sensitive information in errors
6. **Authentication**: Implement strong authentication when needed
7. **Encryption**: Use encryption for sensitive data

## Known Security Considerations

### Tool Execution

Fouad Box executes third-party security tools. Users should:
- Understand what each tool does before running it
- Review tool documentation and source code
- Be aware of tool capabilities and risks
- Use only in authorized testing environments

### Installation Process

The installation process requires root privileges because:
- System-wide tool installation
- Creating symbolic links in `/usr/local/bin/`
- Installing system dependencies
- Setting proper file permissions

### Network Activity

Many tools perform network operations including:
- Port scanning
- Web crawling
- Remote connections
- Data transmission

Always ensure you have authorization before performing network operations.

## Security Updates

Security updates will be released as soon as possible after a vulnerability is confirmed. Users will be notified via:
- GitHub Security Advisories
- Release notes
- README updates
- Email notifications (for registered users)

## Third-Party Tool Security

Fouad Box integrates many third-party security tools. We:
- Use only reputable, well-maintained tools
- Verify tool sources when possible
- Keep tool lists updated
- Remove deprecated or insecure tools

However, we cannot guarantee the security of third-party tools. Users should:
- Review third-party tool documentation
- Understand tool capabilities and risks
- Keep tools updated
- Report any suspicious tool behavior

## Legal and Ethical Use

**IMPORTANT**: Fouad Box is for educational and authorized use only.

### Legal Requirements

- Obtain written authorization before testing
- Comply with all applicable laws
- Respect privacy and data protection regulations
- Follow responsible disclosure practices

### Prohibited Activities

- Unauthorized access to systems
- Malicious activities
- Privacy violations
- Illegal surveillance
- Any form of cybercrime

## Compliance

Fouad Box development follows:
- Secure coding practices
- OWASP guidelines
- Industry security standards
- Open source best practices

## Contact

For security-related questions or concerns:
- **Email**: zalaffouad37@gmail.com
- **Subject**: [SECURITY] Fouad Box Security Inquiry

---

**Thank you for helping keep Fouad Box and its users safe!**
