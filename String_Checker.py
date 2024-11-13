# DFA String Checker

# Function to verify if the current state is a final state
def checkfinal_state(current_state):
    match n:
        case 1:
            # Check if the string starts and ends with specified characters
            if current_state in final_states:
                print("\nYes!...The string is Valid.")
                return
            print("\nNo!...The string is Invalid.")
        case 2:
            # Check occurrence count of a specific character
            if current_state in final_states:
                print("\nYes!...The string has", occ, "occurrences of '", ch, "'.")
                return
            print("\nNo!...The string does not have", occ, "occurrences of '", ch, "'.")
        case 3:
            # Check for the presence of a substring
            if current_state in final_states:
                print("\nYes!...The string has the sub-string '", ch, "'.")
                return
            print("\nNo!...The string does not have the sub-string '", ch, "'.")
        # Additional cases for various conditions
        case 4:
            if current_state in final_states:
                print("\nYes!...The string has even occurrences of '", ch, "' and odd occurrences of '", ch_2, "'.")
                return
            print("\nNo!...The string does not have even occurrences of '", ch, "' and odd occurrences of '", ch_2, "'.")
        case 5:
            if current_state in final_states:
                print("\nYes!...The string has at-least", occ, "'", ch, "' and at-most", occ_2, "'", ch_2, "'.")
                return
            print("\nNo!...The string does not have at-least", occ, "'", ch, "' or/and at-most", occ_2, "'", ch_2, "'.")
        case 6:
            if current_state in final_states:
                print("\nNo!...The string has the sub-string '", ch, "'.")
                return
            print("\nYes!...The string does not have the sub-string '", ch, "'.")
        case 7:
            if current_state in final_states:
                print("\nYes!...The string has the sub-string '", ch, "'. And it starts with '", start, "' and ends with '", end, "'.")
                return
            print("\nNo!...The string does not have the sub-string '", ch, "' Or it does not start with '", start, "' and end with '", end, "'.")

# Function to check if all characters in the string are in the input alphabet
def check(s, input_alpha):
    for i in s:
        if i not in input_alpha:
            return 1
    return 0

# Recursive function for traversing DFA states based on input string
def q(current_state, s, i, arr_2D):
    row_iteration, c0 = int(current_state[1])+1, 0
    print("->", current_state, end=' ')

    # Check for final state at the end of the string
    if i == len(s):
        checkfinal_state(current_state)
        return

    # Find the column number in the transition table (2D array) for current character
    for ele in arr_2D[0]:
        if ele == s[i]:
            break
        c0 = c0 + 1

    # Recursive call to transition to the next state
    q(arr_2D[row_iteration][c0], s, i+1, arr_2D)


# Main program loop
arr_2D_2 = []
n = 0
print("\n*********************************************  STRING  CHECKER  *********************************************")

while n != 8:
    counter, c, ch, ch_2, occ, occ_2, DFA = 0, 1, '', '', 0, 0, 0
    print("\n=============================================================================================================")
    print("Choose your problem type:\n")
    print("1. Starts with a string & Ends with an alphabet.\t2. Occurrence of alphabet in a string.")
    print("3. Must include a sub-string.\t4. Even & Odd Occurrence of a string.")
    print("5. Based on In-equalities of a string.\t6. Does NOT contain a string.")
    print("7. Occurrence of sub-string & start/end of the string.\t8. Exit\n")
    n = int(input("Enter your choice: "))

    # Exit option
    if n == 8:
        print("\n================================================= CODE ENDS =================================================")
        break
    elif n > 8:
        print("\nEnter valid input!")
        continue

    input_alpha = input("Enter input alphabets: ").split()
    for i in input_alpha:
        c = c + 1

    # Define parameters for each condition type
    match n:
        case 1: pass
        case 2:
            ch = input("Enter the alphabet to be checked: ")
            occ = int(input(f"Enter the number of occurrences of '{ch}': "))
        case 3:
            ch = input("Enter the sub-string: ")
        case 4:
            ch = input("Enter the alphabet which occurs even times: ")
            ch_2 = input("Enter the alphabet which occurs odd times: ")
        case 5:
            ch = input("Enter the alphabet with 'at-least': ")
            occ = int(input(f"'{ch}' must occur at-least how many times: "))
            ch_2 = input("Enter the alphabet with 'at-most': ")
            occ_2 = int(input(f"'{ch_2}' must occur at-most how many times: "))
        case 6:
            ch = input("Enter the sub-string which should not be included: ")
        case 7:
            ch = input("Enter the sub-string to include: ")
            start = input("String starts with: ")
            end = input("String ends with: ")

    r = int(input("Enter the number of states: ")) + 1
    arr_2D = [['__'], ]

    # Set up transition table (2D array)
    states = [f'q{app}' for app in range(r-1)]
    for i in input_alpha:
        counter += 1
        arr_2D[0].insert(counter, i)
    for i in range(r - 1):
        arr_2D.append([states[i]])

    # Loop for DFA input
    while DFA != 2:
        print("\n1. Use Previous DFA\n2. New DFA")
        DFA = int(input("Enter your choice: "))
        if DFA == 1:
            if not arr_2D_2:
                print("Enter a DFA first!")
            else:
                for row in arr_2D_2:
                    print(" ".join(row))
                arr_2D = arr_2D_2
                break
        elif DFA == 2:
            print("Enter the DFA transitions:")
            for i in range(r):
                for j in range(c):
                    if i == 0 or j == 0:
                        print(arr_2D[i][j], end="  ")
                    else:
                        a = input().split()
                        arr_2D[i].extend(a[:1])
                        break
                print()
        else:
            print("\nEnter valid choice!")

    arr_2D_2 = arr_2D
    final_states = input("Enter the final states: ").split()
    s = input("Enter String: ")
    print("State Traversal: ")

    # Check if the string contains valid characters
    if check(s, input_alpha) == 1:
        print("INVALID\n-> Entered string can't be recognized.\n")
        continue

    # Begin state traversal
    current_state = 'q0'
    q(current_state, s, 0, arr_2D)

# End of code!___by Aditya Matale
