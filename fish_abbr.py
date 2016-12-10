#!/usr/bin/python3

from subprocess import PIPE, check_output

from ansible.module_utils.basic import AnsibleModule


def cmd(args):
	return check_output(args, universal_newlines=True)

def cmd_fish(command):
	return cmd(['fish', '-c'] + [command])

def list_abbreviations():
	return cmd_fish('abbr -l').splitlines()

def main():
	module = AnsibleModule(
		argument_spec = dict(
			state=dict(default='present', choices=['present', 'absent']),
			name=dict(required=True),
			value=dict(required=True),
		)
	)

	abbrs = list_abbreviations()

	name, value, state = [module.params[prop]
		for prop in ['name', 'value', 'state']]

	changed = module.params['name'] in abbrs

	module.exit_json(changed=changed, something_else=12345)


if __name__ == '__main__':
	main()