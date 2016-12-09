# Ansible module for manipulating fish shell abbreviations

Work in progress

## Usage
In the command line:
```bash
ansible -m fish-abbr -a 'name="gs" value="git status" state=present'
```

In a playbook:
```yml
---
- hosts: all
  tasks:
  - name: abbreviation for git status
  	fish-abbr:
  	  name: gs
  	  value: git status 
```
