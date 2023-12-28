# main.py

def merge_arrays(arr1, arr2):
    result_array = [x for x in arr1 if x in arr2]
    return result_array

if name == "__main__":
    arr1 = list(map(int, input("Введите элементы первого массива через пробел: ").split()))
    arr2 = list(map(int, input("Введите элементы второго массива через пробел: ").split()))

    result = merge_arrays(arr1, arr2)

    print("Результат объединения массивов:", result)
