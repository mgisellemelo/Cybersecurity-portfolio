#
🖥️ 1️⃣ WINDOWS SECURITY CONFIGURATION

#

✅  1: Update Windows and drivers
Configuration > Updates and security > Windows Update

- Search for updates.
- Install optional updates (drivers, firmware).
- Configure automatic updates.

##
✅ 2: Windows Defender Configuration
If you have another antivurus, Windows Defender doesn't make an active analysis but you can configure this. You can also allow and recurring analysis.

- Enable realtime protection
- Enable the cloud protection.
- Enable automatic updates of its database as frquently as possible.


##
✅ 3: Firewall Configuration

Firewall > net protection
. Enable it for private and public networks.
. Allow app thorugh the firewall.
. Check which apps have permissions and delete the ones that you not longer use.
. Block inbound traffic in the firewall configuration.


##
✅ P4: Activate BitLocker ( Windows Pro)
 Configuration > Windows Privacy & Security > BitLocker encryption > activate

. Save your recovery password ( USB o account Microsoft)
. Choose to encrypt all the hard disk and compatible mode.

##
✅ 5: Configuration UAC to maximun

.Saearch for: uac

. Choose "change configuration of user account control"

. Choose the highest level (always notify)

##
✅ 6: Check all unnecessary services

.Search: services.msc 

: Check services like:

-Remote Desktop Services → desable if you don't use RDP

-Server → desable if you don't share folders

-SSDP Discovery, UPnP Device Host → desable if you don't need a devicede UPnP
- For example: SSH is a critical vulnerability veary easy to configure. You can install a secure SSHServer and use a key-based authentication. Also limit the acces to specific users.

##
✅ 7: Backup
- Be sure that your backup is routinely backing up and encrypted.




