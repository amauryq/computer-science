Write-Output "Setting up Python Web Server"
# For Installer, Disable Admin Approval Mode for installing applications and open application port with firewall
New-ItemProperty -Path HKLM:Software\Microsoft\Windows\CurrentVersion\Policies\System -Name EnableLUA -PropertyType DWord -Value 0 -Force
cmd.exe /c netsh firewall add portopening TCP ${port} "Port ${port}"
# New-NetFirewallRule -Name 'OpenSSH-Server-In-TCP' -DisplayName 'OpenSSH Server (sshd)' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22
#Invoke-WebRequest -UseBasicParsing -Uri "https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe" -OutFile "$workingFolder\python-3.11.0-amd64.exe"
Start-Process cmd.exe -Wait -NoNewWindow -ArgumentList '/c', "gsutil cp gs://1-us-east1-taxcalc-binaries/python-3.11.0-amd64.exe $workingFolder\"
Start-Process -FilePath $workingFolder\python-3.11.0-amd64.exe -Wait -NoNewWindow -ArgumentList '/quiet', 'InstallAllUsers=1', 'PrependPath=1', 'Include_test=0'
$env:Path += ";$env:ProgramFiles\Python311"
[Environment]::SetEnvironmentVariable("Path", $env:Path, [System.EnvironmentVariableTarget]::Machine)
New-Item -ItemType file "$workingFolder\http-server.b64"
Set-Content $workingFolder\http-server.b64 '${http_server}'
certutil -decode $workingFolder\http-server.b64 $workingFolder\http-server.py
Start-Process -FilePath "$env:ProgramFiles\Python311\python.exe" -NoNewWindow -ArgumentList "$workingFolder\http-server.py"
