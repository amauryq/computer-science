# Ansible

## Ansible Commands Examples

```bash
ansible webclient -s -m shell -a 'yum list installed | grep python'
ansible all -s -m shell -a 'yum install telnet -y'
ansible local -m setup --tree ./facts
ansible webclient -m setup -a 'filter=*ipv4*'
ansible webclient -m setup -a 'filter=ansible_*'
```

## Ansible Command using modules

```bash
ansible appclient -s -m yum -a 'pkg=telnet state=installed update_cache=true'
```
