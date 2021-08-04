def copying_the_file(output,input):
	with open(output) as f:
		text=f.read()

	with open(input, "w") as f:
		print(text,file=f)


