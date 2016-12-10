#!/usr/bin/python3

import shlex
from subprocess import PIPE, check_output

from ansible.module_utils.basic import AnsibleModule


def cmd(args):
	return check_output(args, universal_newlines=True)

def cmd_fish(command):
	return cmd(['fish', '-c'] + [command])

def list_abbreviations():
	lines = cmd_fish('abbr -s').splitlines()
	name_value_tuples = [shlex.split(line)[1:] for line in lines]
	return dict(name_value_tuples)

def check_name(name):
	if name is None:
		raise Exception('Name cannot be None/null')
	if ' ' in name:
		raise Exception('Name cannot contain spaces')

def remove_abbreviation(name, value=None):
	# check if the name is valid
	check_name(name)

	# fetch abbreviation dictionary
	abbrs = list_abbreviations()

	# it the abbreviation doesn't exist don't delete anything
	if name not in abbrs:
		return False

	# if target value is specified, but it doesn't match the real value
	# don't do anything
	if value is not None and abbrs[name] != value:
		return False

	# delete the abbreviation with name 'name'
	cmd_fish('abbr -e {}'.format(name))
	return True


def add_abbreviation(name, value):
	# check if the name is valid
	check_name(name)

	# fetch abbreviation dictionary
	abbrs = list_abbreviations()

	# if the abbreviation exists and has the correct value, don't
	# do anything
	if name in abbrs and abbrs[name] == value:
		return False

	# add or replace the abbreviation
	cmd_fish('abbr -a {} {}'.format(name, value))
	return True

def main():
	module = AnsibleModule(
		argument_spec = dict(
			state=dict(default='present', choices=['present', 'absent']),
			name=dict(required=True),
			value=dict(),
		)
	)

	name, value, state = [module.params[prop]
		for prop in ['name', 'value', 'state']]

	abbrs = list_abbreviations()

	if state == 'absent':
		changed = remove_abbreviation(name, value)
	elif state == 'present':
		changed = add_abbreviation(name, value)

	module.exit_json(changed=changed)


if __name__ == '__main__':
	main()