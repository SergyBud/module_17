def main():
    global some_list
    try:
        def binary_search(array, value, left, right):
            if left > right:
                return str("Введенное число не может быть добавлено в список")
            middle = (right + left) // 2
            if value > array[middle]:
                if value <= array[middle + 1]:
                    array.insert(middle + 1, value)
                    return middle, middle + 1
                elif value < array[middle]:
                    return binary_search(array, value, left, middle - 1)
                else:
                    return binary_search(array, value, middle + 1, right)
            elif value < array[middle]:
                return binary_search(array, value, left, middle - 1)
            else:
                return binary_search(array, value, middle + 1, right)

        def insertion_sort(value):
            for i in range(1, len(value)):
                x = value[i]
                idx = i
                while idx > 0 and value[idx - 1] > x:
                    value[idx] = value[idx - 1]
                    idx -= 1
                value[idx] = x
            return value

        some_list = input("Введите список чисел через пробел: ").split()
        some_value = int(input("Введите число для вставки: "))
        some_list = [int(i) for i in some_list]
        insertion_sort(some_list)
        print(binary_search(some_list, some_value, 0, len(some_list)))
        print(some_list)
    except IndexError:
        print("Введенное число не может быть добавлено в список")
        print(some_list)
    except ValueError:
        print("Введено невалидное значение, попробуйте еще раз!")
        print("--------------------------------------------------")
        main()


main()
