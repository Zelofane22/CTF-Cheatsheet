https://github.com/security-cheatsheet/cmd-command-cheat-sheet/blob/master/README.md

# user and group cmd
| **Commande** | **description** |
|--------------|-----------------|
| `new-localuser -name "username" -fullname "fullusername" -password (converto-securestring "passe" -asplainttext -force) -description "user description" -passwordneverexpires` | create new user |
| `new-localgroup -name "gruopName"` | create new group |
| `add-localgroupmember -group "groupName" -member "memberName"` | add member in a group |
| `rename-localuser "userName" "newName"` | rename an username|
| `rename-localgroup "groupName" "newName"` | rename a grouName |
| `` ||
| `` ||
| `` ||

# access controle
| **Commande** | **description** |
|--------------|-----------------|
| `get-acl fileOrPathName | format-list` | get fileOrPath info |
| `icacls.exe filename /<grant>or<diny> username:F` | allow or diny fullControl on a file |
| `` ||

# search and sort
| **Commande** | **description** |
|--------------|-----------------|
| `get-childitem -recurse -filter "fileName"` | search file in directory and subDirectory |
| `` ||
| `` ||
| `` ||