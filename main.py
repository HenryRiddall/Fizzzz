import sys


class Rule_Type():
    def __init__(self, description, function_builder):
        self.description = description
        self.function_builder = function_builder


class Rule():
    def __init__(self, triggers, priority, update_function):
        self.triggers = triggers
        self.priority = priority
        self.update_function = update_function


def input_integer(question, valid_nums=[]):
    num = None

    while num == None:
        try:
            num = int(input(question))
            if valid_nums:
                if not num in valid_nums:
                    print("That isnt a valid option please enter a number from the list")
                    num = None
        except ValueError:
            print("Invalid input, please enter a single integer value")

    return num

def input_bool(prompt):
    current_input = ""

    while current_input == "":
        current_input = input('{0} (y/n)\n'.format(prompt))
        if current_input == "y":
            return True
        elif current_input == "n":
            return False
        else:
            print("Invalid input please enter y or n")
            current_input = ""

def define_rule_types():
    rule_types = []

    def word_rule_function_builder():
        word_to_add = input("What word should be added? \n")
        return lambda current_output: current_output.append(word_to_add)
    rule_types.append(Rule_Type("Add a word to the end of the output string", word_rule_function_builder))

    def flip_rule_function_builder():
        return lambda current_output: current_output.reverse()
    rule_types.append(Rule_Type("Flip the output string", flip_rule_function_builder))

    def clear_rule_function_builder():
        return lambda current_output: current_output.clear()
    rule_types.append(Rule_Type("Clear the current string", clear_rule_function_builder))

    return rule_types

def create_rule_prompt(rule_types):
    rule_prompt = "When this rule is triggered what should it do?\n"

    for i, rule_type in enumerate(rule_types):
        rule_prompt = rule_prompt + '    {0}: {1}\n'.format(str(i), rule_type.description)

    return rule_prompt

def input_rule(rule_types, rule_prompt):
        print("")
        rule_triggers = []
        
        more_triggers = True
        while more_triggers:
            rule_triggers.append(input_integer("Please enter a number, multiples of this number will trigger the current rule:\n"))

            more_triggers = input_bool("Would you like to add another number to trigger this rule?")

        rule_priority = input_integer("What is the priority of this rule (0 is applied first then 1 etc)?\n")

        rule_action_type = input_integer(rule_prompt, range(len(rule_types)))

        return Rule(rule_triggers, rule_priority, rule_types[rule_action_type].function_builder())

def input_rules():
    rules = []
    more_rules = True
    rule_types = define_rule_types()
    rule_prompt = create_rule_prompt(rule_types)

    print("\nPlease create your first rule!")
    while more_rules:

        rules.append(input_rule(rule_types, rule_prompt))
        
        more_rules = input_bool("Would you like to add more rules?")
    print("")

    return rules

def fizzbuzz(num, rules):
    rules.sort(key=lambda x: x.priority)

    for i in range(1, num):

        output = []

        for rule in rules:
            apply_rule = True

            for trigger in rule.triggers:
                if i % trigger != 0:
                    apply_rule = False
            
            if apply_rule:
                rule.update_function(output)
        
        if not output:
            output.append(str(i))

        output_string = ''.join(output)
        
        print(output_string)

if __name__ == '__main__':
    fizzbuzz(input_integer("Welcome to FizzBuzzer!\nWhat is the max number you would like FizzBuzzer to calculate?\n"), input_rules())