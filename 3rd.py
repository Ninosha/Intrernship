# მოცემულია string-ი რომელიც შედგება “(“ და “)“ ელემენტებისგან. დაწერეთ ფუნქცია რომელიც
# აბრუნებს ფრჩხილები არის თუ არა მათემატიკურად სწორად დასმული.
# მაგ: “(()())” სწორი მიმდევრობაა,  “())()” არასწორია

#3
def parentheses(string):
    result = False
    if string[0] != ")":
        if string[-1] != "(":
            if string.count("(") == string.count(")"):
                result = True

    return result
