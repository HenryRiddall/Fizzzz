import sys

class Rule():
    __description__ = "Undescribed rule"

    def __init__(self, triggers, priority):
        self.triggers = triggers
        self.priority = priority
    
    def update_output(self, output):
        pass

class Word_Rule(Rule):
    __description__ = "Add a word to the end of the output string"

    def __init__(self, triggers, priority):
        super().__init__(triggers, priority)
        self.word = input("What word shoud be added? ")

    def update_output(self, output):
        output.append(self.word)

class Flip_Rule(Rule):
    __description__ = "Flip the output string"

    def __init__(self, triggers, priority):
        super().__init__(triggers, priority)
    
    def update_output(self, output):
        output.reverse()

class Clear_Rule(Rule):
    __description__ = "Clear the current string"

    def __init__(self, triggers, priority):
        super().__init__(triggers, priority)
    
    def update_output(self, output):
        output.clear()

def get_num(question, valid_nums=[]):
    num = None

    while num == None:
        try:
            num = int(input(question))
            if valid_nums:
                if not num in valid_nums:
                    print("That isnt a valid option")
                    num = None
        except ValueError:
            print("Enter a NUMBER")

    
    return num

def get_rules():
    rules = []
    more_rules = True

    rule_types = Rule.__subclasses__()
    rule_prompt = "When this rule is triggered it should "

    for i, subclass in enumerate(rule_types):
        rule_prompt = rule_prompt + '{0}: {1} '.format(str(i), subclass.__description__)

    while more_rules:
        print("")
        rule_triggers = []
        
        more_triggers = True
        while more_triggers:
            rule_triggers.append(get_num("For this rule multiples of which number should trigger it? "))

            more_triggers_input = ""

            while more_triggers_input == "":
                more_triggers_input = input("Would you like to add another trigger? (y/n) ")
                if more_triggers_input == "y":
                    break
                elif more_triggers_input == "n":
                    more_triggers = False
                else:
                    more_triggers_input = ""

        rule_priority = get_num("What is the priority of this rule in the rule queue? ")


        rule_action_type = get_num(rule_prompt, range(len(rule_types)))

        rules.append(rule_types[rule_action_type](rule_triggers, rule_priority))

        
        more_rules_input = ""
        
        while more_rules_input == "":
            more_rules_input = input("Would you like to add a rule? (y/n) ")
            if more_rules_input == "y":
                break
            elif more_rules_input == "n":
                more_rules = False
            else:
                more_rules_input = ""
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
                rule.update_output(output)
        
        if not output:
            output.append(str(i))

        output_string = ''.join(output)
        
        print(output_string)

if __name__ == '__main__':
    fizzbuzz(get_num("How many numbers would you like to fizzbuzz? "), get_rules())