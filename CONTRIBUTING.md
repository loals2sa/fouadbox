# Contributing to Fouad Box

First off, thank you for considering contributing to Fouad Box! It's people like you that make Fouad Box such a great tool.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples**
- **Describe the behavior you observed and what you expected**
- **Include screenshots if possible**
- **Include your environment details** (OS, Python version, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Use a clear and descriptive title**
- **Provide a detailed description of the suggested enhancement**
- **Explain why this enhancement would be useful**
- **List any similar features in other tools**

### Adding New Tools

Want to add a new security tool to Fouad Box? Great! Here's how:

1. **Fork the repository**
2. **Create a new branch** (`git checkout -b add-new-tool`)
3. **Add your tool** to the appropriate category in `/tools/`
4. **Update the README** with information about the new tool
5. **Test your changes** thoroughly
6. **Commit your changes** (`git commit -m 'Add XYZ tool'`)
7. **Push to the branch** (`git push origin add-new-tool`)
8. **Open a Pull Request**

#### Tool Template

```python
from core import SecurityTool

class YourTool(SecurityTool):
    TITLE = "Tool Name - Short Description"
    DESCRIPTION = "Detailed description of what the tool does"
    INSTALL_COMMANDS = [
        "installation command 1",
        "installation command 2"
    ]
    RUN_COMMANDS = ["tool_command --help"]
    PROJECT_URL = "https://github.com/author/tool"
```

### Pull Request Process

1. Ensure your code follows Python PEP 8 style guidelines
2. Update the README.md with details of changes if applicable
3. Add your changes to the CHANGELOG.md (if exists)
4. The PR will be merged once you have the approval of a maintainer

## Style Guidelines

### Python Style Guide

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use 4 spaces for indentation (not tabs)
- Keep lines under 100 characters when possible
- Use meaningful variable and function names
- Add docstrings to functions and classes

### Git Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests after the first line

Example:
```
Add Nmap integration to reconnaissance tools

- Implement Nmap class in reconnaissance.py
- Add installation and run commands
- Update README with Nmap documentation
- Fixes #123
```

### Documentation

- Keep documentation up to date
- Use clear and concise language
- Include examples where appropriate
- Add screenshots for visual features

## Code of Conduct

### Our Pledge

We pledge to make participation in our project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

### Our Standards

**Positive behavior includes:**
- Using welcoming and inclusive language
- Being respectful of differing viewpoints
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

**Unacceptable behavior includes:**
- Trolling, insulting/derogatory comments, and personal attacks
- Public or private harassment
- Publishing others' private information
- Other conduct which could reasonably be considered inappropriate

## Questions?

Feel free to contact the project maintainer:

- **Email**: zalaffouad37@gmail.com
- **Instagram**: [@1.pvl](https://instagram.com/1.pvl) | [@fod1v](https://instagram.com/fod1v)

## Recognition

Contributors will be recognized in the project README. Thank you for your contributions!

---

**Happy Contributing! 🎉**
