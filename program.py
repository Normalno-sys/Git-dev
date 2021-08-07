def copying_the_file(output,input):
	with open(output) as f:
		text=f.read()

	with open(input, "w",newline='') as f:
		print(text,file=f)


output_file=input()
input_file=input()
copying_the_file(output_file, input_file)
