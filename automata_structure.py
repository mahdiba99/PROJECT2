from toCFG import *
import copy


class NPDA:
    """A nondeterministic pushdown automaton."""

    def __init__(self, states, input_symbols, stack_symbols,
                 transitions, initial_state,
                 initial_stack_symbol, final_states):
        """Initialize a complete NPDA."""
        self.states = states.copy()
        self.input_symbols = input_symbols.copy()
        self.stack_symbols = stack_symbols.copy()
        self.transitions = copy.deepcopy(transitions)
        self.initial_state = initial_state
        self.initial_stack_symbol = initial_stack_symbol
        self.final_states = final_states.copy()


input_file = open("input.txt", "r")
states = set()
input_symbols = set()
stack_symbols = set()
stack_initial_symbols = set()
transitions = {}
initial_states = set()
num_of_states = int(input_file.readline())
final_states = set()
for i in range(num_of_states):
    states.update(["q" + str(i)])

input_symbols.update(input_file.readline().rstrip('\n').split(','))
stack_symbols.update(input_file.readline().rstrip('\n').split(','))
stack_initial_symbols = input_file.readline()

lines = input_file.readlines()

for line in lines:
    if line[:1] == "->":
        for letter in line:
            if letter == "q":
                initial_states.update([line[line.find(letter)] + line[line.find(letter) + 1]])
    if "*" in line:
        final_states.update([line[line.find("*") + 1:line.find("*") + 2]])
    line = line.replace("->", "").replace("*", "").replace("\n", "")
    line = line.split(',')

    new_trans = [line[1], line[2], line[3], line[4]]
    if line[0] in transitions:
        transitions[line[0]].append(new_trans)
    else:
        transitions[line[0]] = [new_trans]

npda = NPDA(states, input_symbols, stack_symbols,
            transitions, initial_states,
            stack_initial_symbols, final_states)

def main():
    print('convert to CFG')
    print(printGrammar(npda))
    print("for cyk")
    print(normalizeGrammar(toCFG(npda)))
    # TODO:run and get input from user & print cyk 
if __name__=='__main__':
    main()
