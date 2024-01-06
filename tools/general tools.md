
# convertir de hexa en binaire
```
xxd -p -r
``` 
# localisation
```
seeker
```
# deploiment d'app web local 
```
ngrok
```
# creer des script de fichiers pour le partages de files (window) et récuperer les hash
```
hashgrab
``` 
# impacket-smbserver
```
impacket-smbserver <sharename> $(pwd) -smb2support -user <username> -password <pass>
```
```
impacket-smbserver -ip @ip -port 445 shareName .
```
# Create custom wordlist
```
nameshuffler
```
# sudo
```
sudo ln -s "$(pwd)/<tool>" "/usr/local/bin/<tool>"
```

# curl
```
curl -H "Content-type: application/json" --Cookie "<name>=<value>" -d '{"data":"data"}' -X POST http://domaine
```

# firebox (dir brutforce)
```
firebox -w 'fzf-wordlist' -u http://adresse
```

# grep
## _find string in directory_
```
grep -r "strings" <path>
```