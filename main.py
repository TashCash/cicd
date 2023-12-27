# main.py
import sys

def merge_arrays(arr1, arr2):
    result_array = [x for x in arr1 if x in arr2]
    return result_array

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python main.py <arr1> <arr2>")
        sys.exit(1)

    arr1 = list(map(int, sys.argv[1].split(',')))
    arr2 = list(map(int, sys.argv[2].split(',')))

    result = merge_arrays(arr1, arr2)

    print("Результат объединения массивов:", result)
