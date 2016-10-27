

def generate_session_id(i):
    digits = []
    id_parts = []
    while i:
        digits.append(i%10)
        i = i//10

    for i in digits:
        if i:
            id_parts.extend(['3', str(i)])
    return "".join(id_parts)+"2d78"


for i in range(100):
    print(generate_session_id(i))