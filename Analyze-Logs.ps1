# Analyze CI/CD logs using GitHub Copilot CLI
# Requires Copilot CLI installed (npm install -g @githubnext/copilot-cli)

$logFile = "sample_logs.txt"

if (-Not (Test-Path $logFile)) {
    Write-Host "Log file not found!"
    exit
}

$logs = Get-Content $logFile -Raw

Write-Host "Analyzing logs with Copilot CLI..."
copilot explain $logs
