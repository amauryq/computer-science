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
ansible-playbook -s Playbooks/appclient.yml
```

## Working with files for store passwords in a secure way

```bash
# Create vault
ansible-vault create accounts.yml

# Edit vault
ansible-vault edit accounts.yml

# Change vault password
ansible-vault rekey accounts.yml

# Decrypt the vault
ansible-vault decrypt accounts.yml

# Encrypt the vault
ansible-vault encrypt accounts.yml

# Run Playbook with vault asking for password
ansible-playbook first-playbook.yml --ask-vault-pass

# Run Playbook with vault asking for password
ansible-playbook first-playbook.yml --vault-password-file ./vault_pass.txt
```