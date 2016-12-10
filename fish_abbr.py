#!/usr/bin/python3

from subprocess import run, PIPE

from ansible.module_utils.basic import AnsibleModule


def main():
	module = AnsibleModule(
		argument_spec = dict(
			state=dict(default='present', choices=['present', 'absent']),
			name=dict(required=True),
			value=dict(required=True),
		)
	)

	p = run(['fish', '-c', 'abbr -l'],
			stdout=PIPE,
			universal_newlines=True)
	abbrs = p.stdout.splitlines()

	changed = module.params['name'] in abbrs
	out = p.stdout

	module.exit_json(changed=changed, something_else=12345, fishout=out)


if __name__ == '__main__':
	main()