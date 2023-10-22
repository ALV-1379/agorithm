
def binary_search(arr, low, high, x):

    if high >= low:

        mid = (high + low) // 2

        # اگه ایندکسی که دنبالشیم وسط باشه
        if arr[mid] == x:
            return mid

        # اگهه عنصر کوچک تر باشه در ارایه سمت چپ
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        # اگه بزرگ تر باشه ارایه سمت چپ
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # اگه وجود نداشته باشه
        return -1


test = [2, 3, 4, 10, 40]
x = 10


result = binary_search(test, 0, len(test)-1, x)

if result != -1:
    print('adad dar index ' + str(result) + " gharar darad")
else:
    print("adad dar araye nist")