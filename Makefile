run-example-command:
	python3 main.py examples/help_example.json command

run-example-list:
	python3 main.py examples/help_example.json list

run-example-file:
	python3 main.py examples/help_example.json file examples/example.txt

run-example-multiple-commands:
	python3 main.py examples/help_example.json multiple_commands