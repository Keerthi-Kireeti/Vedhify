# Vedhify Startup Script
# This script starts both the Flask backend and Next.js frontend

Write-Host "🌿 Starting Vedhify..." -ForegroundColor Green
Write-Host ""

# Start Flask Backend
Write-Host "🔧 Starting Flask Backend..." -ForegroundColor Cyan
$backendJob = Start-Job -ScriptBlock {
    Set-Location $using:PWD
    if (Test-Path ".venv\Scripts\Activate.ps1") {
        .\.venv\Scripts\Activate.ps1
    }
    python app.py
}

Write-Host "✓ Backend starting on http://localhost:5000" -ForegroundColor Green
Write-Host ""

# Wait a bit for backend to initialize
Start-Sleep -Seconds 3

# Start Next.js Frontend
Write-Host "🎨 Starting Next.js Frontend..." -ForegroundColor Cyan
$frontendJob = Start-Job -ScriptBlock {
    Set-Location $using:PWD\UI2
    npm run dev
}

Write-Host "✓ Frontend starting on http://localhost:3000" -ForegroundColor Green
Write-Host ""

Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Yellow
Write-Host "🚀 Vedhify is now running!" -ForegroundColor Green
Write-Host ""
Write-Host "  Backend:  http://localhost:5000" -ForegroundColor Cyan
Write-Host "  Frontend: http://localhost:3000" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press Ctrl+C to stop all services" -ForegroundColor Yellow
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Yellow
Write-Host ""

# Monitor jobs
try {
    while ($true) {
        # Display backend output
        $backendOutput = Receive-Job -Job $backendJob -ErrorAction SilentlyContinue
        if ($backendOutput) {
            Write-Host "[Backend] $backendOutput" -ForegroundColor Blue
        }
        
        # Display frontend output
        $frontendOutput = Receive-Job -Job $frontendJob -ErrorAction SilentlyContinue
        if ($frontendOutput) {
            Write-Host "[Frontend] $frontendOutput" -ForegroundColor Magenta
        }
        
        # Check if jobs are still running
        if ($backendJob.State -ne 'Running' -and $frontendJob.State -ne 'Running') {
            Write-Host "Both services have stopped." -ForegroundColor Red
            break
        }
        
        Start-Sleep -Milliseconds 500
    }
}
finally {
    # Cleanup
    Write-Host ""
    Write-Host "🛑 Stopping services..." -ForegroundColor Yellow
    Stop-Job -Job $backendJob -ErrorAction SilentlyContinue
    Stop-Job -Job $frontendJob -ErrorAction SilentlyContinue
    Remove-Job -Job $backendJob -Force -ErrorAction SilentlyContinue
    Remove-Job -Job $frontendJob -Force -ErrorAction SilentlyContinue
    Write-Host "✓ All services stopped" -ForegroundColor Green
}
