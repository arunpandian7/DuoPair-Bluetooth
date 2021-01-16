param([switch]$Elevated)

function Test-Admin {
    $currentUser = New-Object Security.Principal.WindowsPrincipal $([Security.Principal.WindowsIdentity]::GetCurrent())
    $currentUser.IsInRole([Security.Principal.WindowsBuiltinRole]::Administrator)
}

if ((Test-Admin) -eq $false)  {
    if ($elevated) {
        # tried to elevate, did not work, aborting
    } else {
        Start-Process powershell.exe -Verb RunAs -ArgumentList ('-noprofile -noexit -file "{0}" -elevated' -f ($myinvocation.MyCommand.Definition))
    }
    exit
}

'Running with full privileges'
Write-Host "Downloading PSExec..."
Invoke-WebRequest http://live.sysinternals.com/psexec.exe -OutFile psexec.exe
Write-Host "Downloaded PSExec.exe"
.\psexec.exe -s -i regedit /e C:\BTKeys.reg HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\BTHPORT\Parameters\Keys
Write-Host "Extracted and stored Bluetooth Keys at C:\BTKeys.reg"