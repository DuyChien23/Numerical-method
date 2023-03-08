def ShowOption():
    print('1.Sai số tuyệt đối')
    print('2.Sai số tương đối')
    print('3.Sai số tích lũy')
    print('4.Kết thúc chương trình')

while True:
    ShowOption()
    opt = int(input('Hãy đưa ra lựa chọn: '))

    if opt == 1:
        x = float(input('Nhập x: '))
        dx = float(input('Nhập sai số tuyệt đối của x: '))
        print(f'Sai số tương đối của x {dx/x*100}%')

    if opt == 2:
        x = float(input('Nhập x: '))
        sx = input('Nhập sai số tương đối của x: ')
        sx = sx.rstrip('%')
        sx = float(sx)
        print(f'Sai số tuyệt đối của x {x * sx / 100}')



    if opt == 4:
        print('==========END==========')
        break

    if opt not in [1, 2, 3, 4]:
        print('Lựa chọn không phù hợp!')

    print("=======================")