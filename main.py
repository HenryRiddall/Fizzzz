
def get_input():
    num = None

    while num == None:
        try:
            num = int(input("How many numbers would you like to fizzbuzz: "))
        except ValueError:
            print("Enter a NUMBER")
    
    return num


def fizzbuzz(num):
    for i in range(1, num):

        output = ""

        if i % 3 == 0:
            output = output + "fizz"
        
        if i % 5 == 0:
            output = output + "buzz"

        if output == "":
            output = i
        
        print(output)

if __name__ == '__main__':
    fizzbuzz(get_input())