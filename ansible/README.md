```bash
ansible webclient -s -m shell -a 'yum list installed | grep python'
ansible all -s -m shell -a 'yum install telnet -y'
```