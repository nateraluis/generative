import vpype_cli

filepath = '20230802_tangents/tangents.svg'
vpype_cli.execute(f'read {filepath} write --pen-up penup.svg')
vpype_cli.execute(f'read {filepath} linesort write --pen-up penup_linesort.svg')
