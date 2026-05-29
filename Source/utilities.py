def validate_input(options, chosen):
    return chosen in options

def pick_menu(options):

    for i, element  in enumerate(options):
        print(f"({i}) {element}")
    picked_option = input("Pick option: ")
    while not picked_option.isdigit() and picked_option < 0 or int(picked_option) > len(options):
        picked_option = input("Pick option: ")
    return options[picked_option]