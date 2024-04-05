## Basic Tools

| **Command**   | **Description**   |

| **Vim** |
	| `vim file` | vim: open file with vim |
	| `esc+i` | vim: enter `insert` mode |
	| `esc` | vim: back to `normal` mode |
	| `x` | vim: Cut character |
	| `dw` | vim: Cut word |
	| `dd` | vim: Cut full line |
	| `yw` | vim: Copy word |
	| `yy` | vim: Copy full line |
	| `p` | vim: Paste |
	| `:1` | vim: Go to line number 1. |
	| `:w` | vim: Write the file 'i.e. save' |
	| `:q` | vim: Quit |
	| `:q!` | vim: Quit without saving |
	| `:wq` | vim: Write and quit |

# Active Reconnaissance Service Scanning
```
nmap -Pn -A -sC -p- 10.129.42.253
```
## _display ssl ports only_
```
nmap -p 31000-32000 -sV --open -v localhost | grep -E '^[0-9]+/tcp.*ssl/.*$'
```
	| `locate scripts/citrix` | List various available nmap scripts |
	| `nmap --script smb-os-discovery.nse -p445 10.10.10.40` | Run an nmap smb script on an IP |
	| `nmap -sV --script=http-enum -oA name_file 10.129.42.190` | enumerate common web application directories |
	| `nc -nv 10.129.42.190 22` | Get the banner |
	| `netcat 10.10.10.10 22` | Grab banner of an open port |
	| `openssl s_client -connect localhost:30001` | Connect to remote host by ssl protocole

# Passive Reconnaissance 
	| `whois <address>` | général info |
	
	

# Web Enumeration
```
gobuster dir  -w /usr/share/seclists/Discovery/Web-Content/big.txt -u http://$ip/
```
```
ffuf -w /usr/share/wordlists/dirb/big.txt -u http://$ip/FUZZ
```
## par rapport au cms
```
$ find /usr/share/seclists/Discovery/Web-Content/ -type f -name *<cms_name>* 2>/dev/null
```
## php web server
```
gobuster dir -w /usr/share/seclists/Discovery/Web-Content/Common-PHP-Filenames.txt -u http://challenge01.root-me.org/web-serveur/ch11/
```
## scan website
	| `enum4linux @IP` | scan website |
## Grab website banner
```
curl -IL https://www.inlanefreight.com
```

	| `` | same thing |
	| `dirsearch -u @HOST` | directory scan |
	| `` | Grab website banner |
	| `whatweb 10.10.10.121` | List details about the webserver/certificates |
## backup files #backupFiles
### metasploit
`msf6 > use auxiliary/scanner/http/backup_file`
On définit le host à scanner :
`msf6 auxiliary(scanner/http/backup_file) > set rhosts challenge01.root-me.org`
Ainsi que le path :
`msf6 auxiliary(scanner/http/backup_file) > set path web-serveur/ch11/index.php`
Enfin on lance le scan :
`msf6 auxiliary(scanner/http/backup_file) > run`
# DNS Enumeration
```
gobuster dns -w /usr/share/seclists/Discovery/DNS/namelist.txt -d domain.com
```
	| `host -t ns -p54011 adresse` | Display domain master and subdns |
	| `dig -t ns @<address>` | same thing |
	| `dig @1.1.1.1 tryhackme.com MX` |  |
	| `nslookup -type=A adresse 1.1.1.1` | |
	| `dnsenum axfr <subdomain> @<domain>` | zone transfer |
	| `use DNSDumpster.com or shodan.io`

# Subdomaine enumeration 
```
gobuster vhost -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt -t 50 --append-domain -u http://$ip/
```
```
ffuf -w /usr/share/wordlists/seclists/Discovery/DNS/namelist.txt -H "Host: FUZZ.acmeitsupport.thm" -u http://10.10.244.139 -fs 2395
```
## _online enumeration_
```
sublist3r -d domaine_name -b /usr/lib/python3/dist-packages/subbrute/names.txt
```
# Amazone s3 buckets interact with awscli
	| `aws configure` | |
	| `aws --endpoint=http://s3.domaine_name s3 ls s3://domaine_name` | list s3 bucket container |

# foothold exploit

## Partage des ports de la cible sur ma machine
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
