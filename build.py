import shutil
from datetime import datetime

print('Clearing previous build...')
shutil.rmtree('output', ignore_errors=True)

print('Copying static file(s)...')
shutil.copytree('src', 'output')

print('Building dynamic file...')
now = datetime.now()
with open(f'output/{ now:%Y%m%d%H%M%S }.txt', 'w') as fd:
	fd.write(f'Build time: { now.isoformat() }\n')

print('Finished!')
