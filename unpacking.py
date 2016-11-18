
x = (1, 2, 3)
a, b, c = x  # using unpacking on assignment


def f(i, j, k):
    print("Got three arguments, {}, {}, {}".format(i, j, k))


f(*x)  # unpack the list x into positional arguments of f

keyword_arguments = {"i": 10, "j": 20, "k":30}

f(**keyword_arguments)  # unpack the dict into the fuction arguments