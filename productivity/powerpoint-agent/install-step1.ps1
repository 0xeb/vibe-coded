# ============================================================================
# Step 1: Install System Dependencies
# ============================================================================

Write-Host ""
Write-Host "===========================================================================" -ForegroundColor Cyan
Write-Host "  Marp Presentation Course - Installation Step 1 of 2" -ForegroundColor Cyan
Write-Host "===========================================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Installing system dependencies via winget:"
Write-Host "  - Node.js, LibreOffice (required)"
Write-Host "  - Python, VS Code, CMake, Git, GitHub Desktop, PowerShell (optional)"
Write-Host ""
Write-Host "Press Ctrl+C to cancel, or any key to continue..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
Write-Host ""

# Helper function to install packages
function Install-Package {
    param(
        [string]$Name,
        [string]$Id,
        [string]$Note = ""
    )

    Write-Host "Installing $Name..." -ForegroundColor Yellow
    if ($Note) { Write-Host "  $Note" -ForegroundColor Gray }

    try {
        winget install -e --id $Id --accept-source-agreements --accept-package-agreements 2>&1 | Out-Null
        if ($LASTEXITCODE -eq 0) {
            Write-Host "  [OK] $Name" -ForegroundColor Green
        } else {
            Write-Host "  [SKIP] $Name" -ForegroundColor Yellow
        }
    } catch {
        Write-Host "  [SKIP] $Name" -ForegroundColor Yellow
    }
}

# Install packages
Install-Package "Node.js" "OpenJS.NodeJS.LTS"
Install-Package "LibreOffice" "TheDocumentFoundation.LibreOffice" "Required for editable PPTX"
Install-Package "Python 3.12+" "Python.Python.3.12"
Install-Package "Visual Studio Code" "Microsoft.VisualStudioCode"
Install-Package "CMake" "Kitware.CMake"
Install-Package "Git" "Git.Git"
Install-Package "GitHub Desktop" "GitHub.GitHubDesktop"
Install-Package "PowerShell (latest)" "Microsoft.PowerShell"

Write-Host ""
Write-Host "===========================================================================" -ForegroundColor Green
Write-Host "Step 1 Complete!" -ForegroundColor Green
Write-Host "===========================================================================" -ForegroundColor Green
Write-Host ""
Write-Host "NEXT STEPS:" -ForegroundColor Yellow
Write-Host "  1. CLOSE this window" -ForegroundColor Cyan
Write-Host "  2. Double-click: install-step2.bat" -ForegroundColor Cyan
Write-Host ""
Write-Host "Why? Environment variables need to refresh." -ForegroundColor Gray
Write-Host ""
Write-Host "Press any key to exit..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
