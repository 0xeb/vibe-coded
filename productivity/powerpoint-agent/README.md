# Starter Materials - Marp Presentation Course

This folder contains everything you need to get started with creating presentations using Marp.

## Quick Start

### 1. Install Prerequisites

**Two-Step Installation:**

1. **Double-click** `install-step1.bat` (installs system tools)
2. **Wait for Step 1 to complete and close the window**
3. **Double-click** `install-step2.bat` (installs npm packages)

**Why two steps?** After Step 1 installs Node.js, environment variables need to refresh. A brand new process (Step 2) will have Node.js in its PATH.

This will install:
- **Node.js** - JavaScript runtime for Marp CLI
- **Marp CLI** - Markdown to presentation converter
- **GitHub Copilot CLI** - AI-powered command-line assistant (requires GitHub Copilot subscription)
- **LibreOffice** - Required for editable PPTX generation
- **Python 3.12+** - Optional, for web scraping and automation
- **Visual Studio Code** - Code editor with Markdown preview
- **CMake** - Build system for C/C++ projects
- **Git** - Version control system
- **GitHub Desktop** - Graphical interface for Git
- **PowerShell (latest)** - Modern PowerShell with cross-platform features

**IMPORTANT:** After installation completes, close your terminal and open a new one to ensure environment variables are loaded.

### 2. Verify Installation

Open a **new terminal** and run:

```cmd
node --version
npm --version
marp --version
copilot --version
python --version
where soffice
code --version
cmake --version
git --version
pwsh --version
```

All commands should return version numbers or paths (no errors).

Also, as part of the verification, let's generate a test presentation first:

Let's test your setup by rendering the included "Hello" slide:

**Command Prompt (cmd):**
```cmd
marp-pptx.bat hello.md
```

**PowerShell:**
```powershell
.\marp-pptx.ps1 hello.md
```

This will create `hello.pptx` - a simple slide with white "Hello" text on a black background.

**Open `hello.pptx` in PowerPoint to verify:**
- The file opens correctly
- You can edit the text (it's not an image)
- The slide has a black background with white text

If this works, you're all set! See the `presentation/` folder for step-by-step tutorials.

## 3. Using LLMs to build your slides

Run your agentic tool, like Copilot CLI or VS Copilot from the Terminal folder:

```bash
copilot --allow-all-tools
```

Then prompt it as such 'Please load the agent-pptx.md' file. When the Agent responds, you are ready to interact.
