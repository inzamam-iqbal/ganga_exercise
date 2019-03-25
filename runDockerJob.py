import sys

#check atleast 3 arguments are given
if len(args) < 3:
	print("Please provide docker image name and sudo password as argument")
	sys.exit(1)
	
args = sys.argv
j=Job(name='runDocker')
j.application.exe = File('runDockerCommand.sh')
j.application.args = [args[1], args[2]]
j.submit()
