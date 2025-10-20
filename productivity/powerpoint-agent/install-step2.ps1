# ============================================================================
# Step 2: Install npm Packages
# ============================================================================

Write-Host ""
Write-Host "===========================================================================" -ForegroundColor Cyan
Write-Host "  Marp Presentation Course - Installation Step 2 of 2" -ForegroundColor Cyan
Write-Host "===========================================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Installing npm packages: Marp CLI, GitHub Copilot CLI"
Write-Host ""
Write-Host "Press Ctrl+C to cancel, or any key to continue..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
Write-Host ""

# Refresh environment variables
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

# Verify Node.js
Write-Host "Verifying Node.js..." -ForegroundColor Yellow
try {
    $nodeVersion = node --version 2>&1
    $npmVersion = npm --version 2>&1
    if ($LASTEXITCODE -ne 0) { throw "Node.js not found" }
    Write-Host "  [OK] Node $nodeVersion, npm $npmVersion" -ForegroundColor Green
} catch {
    Write-Host "  [ERROR] Node.js not found!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please run install-step1.bat first, then restart your terminal." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Press any key to exit..."
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
    exit 1
}
Write-Host ""

# Install Marp CLI
Write-Host "Installing Marp CLI..." -ForegroundColor Yellow
try {
    npm install -g @marp-team/marp-cli 2>&1 | Out-Null
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  [OK] Marp CLI" -ForegroundColor Green
    } else {
        Write-Host "  [ERROR] Marp CLI failed" -ForegroundColor Red
        Write-Host ""
        Write-Host "Try manually: npm install -g @marp-team/marp-cli" -ForegroundColor Yellow
        Write-Host ""
        Write-Host "Press any key to exit..."
        $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
        exit 1
    }
} catch {
    Write-Host "  [ERROR] Marp CLI failed" -ForegroundColor Red
    exit 1
}

# Install GitHub Copilot CLI (optional)
Write-Host "Installing GitHub Copilot CLI..." -ForegroundColor Yellow
Write-Host "  Note: Requires GitHub Copilot subscription" -ForegroundColor Gray
try {
    npm install -g @github/copilot 2>&1 | Out-Null
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  [OK] GitHub Copilot CLI" -ForegroundColor Green
    } else {
        Write-Host "  [SKIP] GitHub Copilot CLI" -ForegroundColor Yellow
    }
} catch {
    Write-Host "  [SKIP] GitHub Copilot CLI" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "===========================================================================" -ForegroundColor Green
Write-Host "Installation Complete!" -ForegroundColor Green
Write-Host "===========================================================================" -ForegroundColor Green
Write-Host ""
Write-Host "Test your setup with: .\marp-pptx.ps1 hello.md" -ForegroundColor Cyan
Write-Host ""
Write-Host "For GitHub Copilot CLI, authenticate with: copilot" -ForegroundColor Gray
Write-Host ""
Write-Host "Press any key to exit..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
