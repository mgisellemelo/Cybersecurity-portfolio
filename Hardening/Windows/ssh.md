Replace your existing sshd_config file at:


C:\ProgramData\ssh\sshd_config
With this:

ssh:

# Basic settings
Port 2222                   # Use a non-standard port
AddressFamily any
ListenAddress 0.0.0.0
ListenAddress ::

# Authentication
PermitRootLogin no
PasswordAuthentication no   # Only allow key-based login
PubkeyAuthentication yes
AuthorizedKeysFile .ssh/authorized_keys

# Access control
AllowUsers YourUser         # Replace with your real username

# Session settings
AllowTcpForwarding no
X11Forwarding no
PermitTunnel no
AllowAgentForwarding no
ClientAliveInterval 300
ClientAliveCountMax 2
LoginGraceTime 30
MaxAuthTries 3
MaxSessions 2
 ##

 PowerShell Script – SSH Hardening & Firewall Rules
##
 Here’s a PowerShell script to:

- Change SSH to port 2222

- Disable password login

- Allow only a specific user

- Configure firewall rules

⚠️ Before running the script, make sure you’ve:

Replaced YourUser with your actual username

Uploaded your public key to:
C:\Users\YourUser\.ssh\authorized_keys

Restart SSH service
# Logging
LogLevel VERBOSE
After editing, restart the SSH service:
# Variables
$sshConfig = "C:\ProgramData\ssh\sshd_config"
$allowedUser = "YourUser"  # Replace with your username
$sshPort = 2222

# Backup existing sshd_config
Copy-Item $sshConfig "$sshConfig.bak"

# Secure config update
$content = @"  
Port $sshPort  
PermitRootLogin no  
PasswordAuthentication no  
PubkeyAuthentication yes  
AuthorizedKeysFile .ssh/authorized_keys  
AllowUsers $allowedUser  
AllowTcpForwarding no  
X11Forwarding no  
PermitTunnel no  
AllowAgentForwarding no  
ClientAliveInterval 300  
ClientAliveCountMax 2  
LoginGraceTime 30  
MaxAuthTries 3  
MaxSessions 2  
LogLevel VERBOSE  
"@  

Set-Content $sshConfig $content

# Set firewall rule for new SSH port
New-NetFirewallRule -DisplayName "SSH Port $sshPort" -Direction Inbound -Protocol TCP -LocalPort $sshPort -Action Allow

# Remove default port 22 rule (optional)
Remove-NetFirewallRule -DisplayName "OpenSSH-Server-In-TCP"

# Restart SSH service
Restart-Service sshd

Write-Host "✅ SSH hardened and restarted on port $sshPort"


powershell:

Restart-Service sshd
