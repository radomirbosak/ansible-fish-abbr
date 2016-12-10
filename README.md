# Ansible module for manipulating fish shell abbreviations

**fish_abbr** is an ansible module which adds and removes fish abbreviations. It does this by calling `fish -c 'abbr -a ...'` and `fish -c 'abbr -e ...'` on target host.

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
