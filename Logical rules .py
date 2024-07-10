global facts
global is_changed
is_changed = True
facts = [["breathe","dog"],
         ["eat","cow"],
         ["2 legs","John"],
         ["move","goat"],
         ["skin","cat"],
         ["skin","giraffe"],
         ["fly","parrot"],
         ["2 legs","kangaroo"],
         ["intelligence","John"],
         ["egg","hen"]]

def assert_fact(fact):
    global facts
    global is_changed
    if not fact in facts:
        facts += [fact]
        is_changed = True

while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "breathe":
            assert_fact(["Living_thing",A1[1]])
        if A1[0] == "eat":
            assert_fact(["Living_thing",A1[1]])
        if A1[0] == "Animal":
            assert_fact(["Living_thing",A1[1]])
        if A1[0] == "Bird":
            assert_fact(["Living_thing",A1[1]])
        if A1[0] == "Human":
            assert_fact(["Living_thing",A1[1]])
        if A1[0] == "move":
            assert_fact(["Animal",A1[1]])
        if A1[0] == "fly" or A1[0] == "egg":
            assert_fact(["Bird",A1[1]])
        if A1[0] == "skin" or A1[0] == "2 legs":
            assert_fact(["Animal",A1[1]])
        if A1[0] == "2 legs" and ["intelligence",A1[1]] in facts:
            assert_fact(["Human",A1[1]])

for A1 in facts:
    if A1[0] == "Living_thing":
        print(A1)
