# Ansible module for manipulating fish shell abbreviations

Work in progress

## Usage
In the command line:
```bash
ansible -m fish_abbr -a 'name="gs" value="git status" state=present'
```

In a playbook:
```yml
---
- hosts: all
  tasks:
  - name: abbreviation for git status
    fish_abbr:
      name: gs
      value: git status 
```

You can:

* [ ] add abbreviation
* [ ] remove abbreviation