from pathlib import Path


def checkFile(user_input) -> bool:
    path_to_file = user_input + ".csv"
    path = Path(path_to_file)

    if path.is_file():
        return True

    return False


def printResult(stat) -> None:
    print("\n========== RESULT ==========")
    
    for key, value in stat.items():
        print("{}: ${}".format(key, value[0]))
        
    print()
    
