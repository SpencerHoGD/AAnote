
https://serverfault.com/questions/1145358/how-can-i-configure-my-dns-settings-on-debian-12

1. You need to install resolvconf.
    
    ```
    sudo apt install resolvconf
    ```
    
2. Enable and Start the service resolvconf.
    
    ```
    systemctl start resolvconf
    systemctl enable resolvconf
    systemctl status resolvconf
    ```
    
3. Update the file /etc/resolvconf/resolv.conf.d/head to have lines like:
    
    ```
    nameserver 8.8.8.8
    nameserver 8.8.4.4
    ```
    
4. Run the command:
    
    ```
    resolvconf --enable-updates
    resolvconf -u
    ```
    

Ref: [https://www.ionos.com/digitalguide/server/configuration/how-to-set-dns-on-debian/#:~:text=the%20DNS%20field.-,How%20to%20set%20your%20DNS%20server%20using%20the%20configuration%20file,-You%20can%20also](https://www.ionos.com/digitalguide/server/configuration/how-to-set-dns-on-debian/#:%7E:text=the%20DNS%20field.-,How%20to%20set%20your%20DNS%20server%20using%20the%20configuration%20file,-You%20can%20also)