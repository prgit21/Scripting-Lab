from collections import Counter
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

print("Number of words in the file :",word_count("test.txt"))


##S = [x**2 for x in range(10)] # read elements  to list
#M = [x for x in S if x % 2 == 0]
#M.reverse()



def Max(list):
    if len(list) == 1:
        return list[0]
    else:
        m = Max(list[1:])
        return m if m > list[0] else list[0]

def main():
	try:
		list = eval(input("Enter a list of numbers: "))
		print ("The largest number is: ", Max(list))
	except SyntaxError:
		print ("Please enter comma separated numbers")
	except:
		print ("Enter only numbers")

main()
