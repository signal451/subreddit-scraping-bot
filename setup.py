
def __init__():
    with open('terminal.txt', 'r') as txt:
        while True:
            asci = txt.read()
            if not asci:
                break
            print(asci)


    