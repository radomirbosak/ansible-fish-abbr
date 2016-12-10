# Ansible module for manipulating fish shell abbreviations

Work in progress

## Usage
In the command line:
```bash
ansible -m fish_abbr -a 'name="gs" value="git status" state=present' all
```

In a playbook:
```yml
---
- hosts: all
  tasks:
  - name: create abbreviation for git status
    fish_abbr: name=gs value="git status"

  - name: make sure the gs abbreviation is not present
    fish_abbr: name=gs state=absent
```

You can:

* [x] add abbreviation
* [x] remove abbreviation