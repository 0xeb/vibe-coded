# ============================================================================
# Marp PPTX Generator (PowerShell Version)
# ============================================================================
# Generates editable PowerPoint presentations from Marp markdown files
# Usage: .\marp-pptx.ps1 input.md [output.pptx]
# ============================================================================

param(
    [Parameter(Mandatory=$true, Position=0)]
    [string]$InputFile,

    [Parameter(Mandatory=$false, Position=1)]
    [string]$OutputFile
)

# Add LibreOffice to PATH if not already there
$env:Path = $env:Path + ";C:\Program Files\LibreOffice\program"

# If no output file specified, derive from input filename
if ([string]::IsNullOrEmpty($OutputFile)) {
    $OutputFile = [System.IO.Path]::ChangeExtension($InputFile, ".pptx")
}

# Check if input file exists
if (-not (Test-Path $InputFile)) {
    Write-Host "Error: Input file '$InputFile' not found" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "============================================================================" -ForegroundColor Cyan
Write-Host "Generating PPTX from: $InputFile" -ForegroundColor Cyan
Write-Host "Output file: $OutputFile" -ForegroundColor Cyan
Write-Host "============================================================================" -ForegroundColor Cyan
Write-Host ""

# Run Marp with editable PPTX option (OUR STANDARD)
marp "$InputFile" --pptx --pptx-editable -o "$OutputFile" --allow-local-files

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "============================================================================" -ForegroundColor Green
    Write-Host "Success! PPTX created: $OutputFile" -ForegroundColor Green
    Write-Host "============================================================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "The PPTX is fully editable in PowerPoint."
    Write-Host "Note: Warnings about LibreOffice are normal."
    Write-Host ""
} else {
    Write-Host ""
    Write-Host "============================================================================" -ForegroundColor Red
    Write-Host "Error: Failed to generate PPTX" -ForegroundColor Red
    Write-Host "============================================================================" -ForegroundColor Red
    Write-Host ""
    Write-Host "Make sure LibreOffice is installed:" -ForegroundColor Yellow
    Write-Host "  winget install TheDocumentFoundation.LibreOffice"
    Write-Host ""
    Write-Host "Then restart your terminal and try again."
    exit 1
}
