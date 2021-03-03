text = input()

special_chars = '!@#$%^&*()-+'


def score(text):
    score_set = set()

    if len(text) >= 6:
        score_set.add(1)

    for i in text:

        if i.isupper():
            score_set.add(2)
        if i.islower():
            score_set.add(3)
        if i in special_chars:
            score_set.add(4)

        try:
            temp = int(i)
            score_set.add(5)
        except ValueError:
            pass

    return score_set


if len(score(text)) == 5:
    print("the given password is strong.")
else:
    print("the given password is not strong.")
