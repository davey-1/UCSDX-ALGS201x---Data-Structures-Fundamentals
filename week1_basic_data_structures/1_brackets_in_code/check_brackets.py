# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["position", "char"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    brackets = []

    for i,next in enumerate(text):
        if next in "({[":
            brackets.append((i,next))
        if next in ")]}":
            if len(brackets)>0:
                if are_matching(brackets[-1][1], next):
                    brackets.pop()
                else:
                    #return unmatched first closing backet, if no match
                    return i+1
                     #return the most recent bracket
            else:
                return i+1
            
    if len(brackets)==0:
        return "Success"
    else:
        return(brackets[0][0]+1)
    
""" 
#intended function is to read the test cases in the 'test' folder      
def test_function():
    path = 'Your path to the test cases folder '
    for filename in os.listdir(path): # enumerate all the document names in the test file
        f = open(path+'/' + filename, 'r') # open the file
        content = f.read() # read the file
        if filename.endswith('.a'): # standard results
            print('stardard_result: ', content)
        else:# test result
            text = content
            print('Our_algorithm_result: ', check_brackets_in_code(text))            
"""

def main():
    text = input()
    print(find_mismatch(text))

if __name__ == "__main__":
    main()

