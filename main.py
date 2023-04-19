class Word_Rule():
    def __init__(self, trigger, word, priority):
        self.trigger = trigger
        self.word = word
        self.priority = priority



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
    word_rules = []
    flip_rules = []
    more_rules = True

    while more_rules:
        rule_trigger = get_num("For this rule multiples of which number should trigger it? ")

        rule_action_type = get_num("When this rule is triggered should 1: a word be added    2: flip the order of words ", [1,2])

        if rule_action_type == 1:
            rule_word = input("What word shoud be added? ")
            rule_priority = get_num("What will this words priority be in the order? ")
            word_rules.append(Word_Rule(rule_trigger, rule_word, rule_priority))
        else:
            flip_rules.append(rule_trigger)

        
        more_rules_input = ""
        
        while more_rules_input == "":
            more_rules_input = input("Would you like to add a rule? (y/n) ")
            if more_rules_input == "y":
                break
            elif more_rules_input == "n":
                more_rules = False
            else:
                more_rules_input = ""

    return (word_rules, flip_rules)

def fizzbuzz(num, rules):
    word_rules = rules[0]
    flip_rules = rules[1]

    word_rules.sort(key=lambda x: x.priority)

    for i in range(1, num):

        output = []
        flip = False

        for word_rule in word_rules:
            if i % word_rule.trigger == 0:
                output.append(word_rule.word)
        
        for flip_rule in flip_rules:
            if i % flip_rule == 0:
                flip = not flip
        
        if flip:
            output.reverse()
        
        if not output:
            output.append(str(i))

        output_string = ''.join(output)
        
        print(output_string)

if __name__ == '__main__':
    fizzbuzz(get_num("How many numbers would you like to fizzbuzz? "), get_rules())