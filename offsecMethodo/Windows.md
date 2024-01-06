
# SMB
```
nxc smb <IP>
```

## liste les shares
```
nxc smb <IP> --shares
```

## liste users
```
nxc smb <IP> -u 'guest' -p '' --rid-brute 10000
````

## download files
```
nxc smb <IP> -u 'guest' -p '' -M spider_plus -o DOWNLOAD_Flag=True
```

