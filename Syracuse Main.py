def main():                 #main for syracuse
    strSyr = []
    print("This program outputs a Syracuse sequence")
    userInput = int(input("Enter the initial value (an int >= 1) : ")) #take input from user.
    strSyr.append(userInput)
    syr(userInput, strSyr)

    print(strSyr)           #print the progress.
    
def syr(input,stra = []):
    if input == 1:          #base case for recursion.
        return
    
    if input%2 == 0:
        input = input/2
        stra.append(input)
    else:
        input = 3*input +1
        stra.append(input)
        
    syr(input,stra)         #recursive call untill it hits base case.

main()
    
    
