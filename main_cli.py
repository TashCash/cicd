# main_cli.py
import click
from main import merge_arrays

@click.command()
@click.argument('arr1')
@click.argument('arr2')
def main(arr1, arr2):
    arr1 = list(map(int, arr1.split(',')))
    arr2 = list(map(int, arr2.split(',')))

    result = merge_arrays(arr1, arr2)

    print("Результат объединения массивов:", result)

if __name__ == '__main__':
    main()
