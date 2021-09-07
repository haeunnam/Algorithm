def solution(n, arr1, arr2):
    def binary_change(num, binary):
        while num >= 2:
            binary =  str(num % 2) + binary
            num = num//2
        binary =  str(num) +binary
        return binary

    # arr 1이랑 arr2 이진수로 바꾸기
    arr1_map = []
    arr2_map = []
    total_map = []
    for num in range(n):
        map_str = binary_change(arr1[num], "")
        while len(map_str) < n:
            map_str = '0' + map_str
        arr1_map.append(map_str)
    for num in range(n):
        map_str = binary_change(arr2[num], "")
        while len(map_str) < n:
            map_str = '0' + map_str
        arr2_map.append(map_str)


    for row in range(n):
        tmp = ''
        for col in range(n):
            if arr1_map[row][col] == '1' or arr2_map[row][col] == '1':
                tmp += '#'
            else:
                tmp += " "
        total_map.append(tmp)
    print(total_map)

    return total_map

