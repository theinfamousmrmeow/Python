### This is a sample Python script.

#
# GO AWAY

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#IMPORTS

from alg2.HashTable import HashTable

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
class TuringMachine(object):

    def __init__(self, alphabet, tape_string, blank_symbol, initial_state,
                 final_states, transition_function):
        self.alphabet = alphabet
        self.tape = list(tape_string)
        self.blank_symbol = blank_symbol
        self.current_state = initial_state
        self.final_states = final_states
        self.transition_function = transition_function

        self.head_position = 0
        self.tape.append(blank_symbol)

    def bark(self):
        print("WOOF")

    def step(self):
        current_char = self.tape[self.head_position]
        trans_key = (self.current_state, current_char)

        # Retrieve transition rule for current configuration
        if trans_key in self.transition_function:
            trans_rule = self.transition_function[trans_key]
            self.tape[self.head_position] = trans_rule[1]
            # Move head position right or left
            if trans_rule[2] == 'R':
                self.head_position += 1
            elif trans_rule[2] == 'L' and self.head_position != 0:
                self.head_position -= 1
            self.current_state = trans_rule[0]

    def final_state(self):
        if self.current_state in self.final_states:
            return True
        else:
            return False



###HEAP SORT ALGORITHM



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    tm = TuringMachine("asldkjfasd","a","","a","z","a-b")
    tm.bark()
    ht = HashTable()
    ht.bark()
    ht.print()
    ht.add2("meow","what a cat does")
    ht.print()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
