if __name__ == '__main__':
    change = RMB()
    while 1:
        s = input('请输入金额：')
        try:
            if s.isdigit():
                if len(s)<13:
                    print(f'大写金额为：{change.small_to_big(s)}')
                else:
                    print("输入错误")
            else:
                print(f'小写金额为：{change.big_to_small(s)}')
        except Exception:
            print("输入错误")

 if __name__ == '__main__':
    change = RMB()
    while 1:
        s = input('请输入金额：')
        try:
            if s.isdigit():
                if len(s)<13:
                    print(f'大写金额为：{change.small_to_big(s)}')
                else:
                    print("输入错误")
            else:
                print(f'小写金额为：{change.big_to_small(s)}')
        except Exception:
            print("输入错误")
