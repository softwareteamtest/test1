class RMB(object):
    number_change = {
        '0': '零','1': '壹','2': '贰','3': '叁','4': '肆',
        '5': '伍','6': '陆','7': '柒','8': '捌','9': '玖',
        '10': '拾','100': '佰','1000': '仟'
    }

    def small_to_big(self, small):  ##小写转大写
        res = '整'
        unit_middle = ['', '拾', '佰', '仟']
        unit_money = ['元', '万', '亿']
        for i, n in enumerate(small[::-1]):
            if i % 4 == 0:
                unit_middle[0] = unit_money[i // 4]
                if n == '0':  ##4的整数倍位零不加
                    res += unit_middle[i % 4]
                    continue
                res += '%s%s' % (unit_middle[i% 4], self.number_change[n])
            else:
                if n == '0':
                    res += self.number_change[n]
                    continue
                res += '%s%s' % (unit_middle[i% 4], self.number_change[n])
        res = res[::-1]
        for i in range(len(res)):
            if i == len(res):
                continue
            if res[i] == '零' and res[i + 1] == '零':
                continue
            if res[i] == '零' and res[i + 1] in unit_money:
                continue
        return res

    def big_to_small(self, big):
        change_int = ''
        change_int = self.change_big(big[:-1])
        remove = 0
        dec = ''
        for s in change_int:
            if s != '0':
                break
            remove += 1
        res_small = change_int[remove:] + dec
        return res_small

    def change_big(self, res):
        #利用递归函数实现处理输入的大写金额
        less = []
        max_money = ''
        unit_money = {'元': 1, '万': 5, '亿': 9}
        for s in unit_money:
            if s in res: #接收一个输入的大写金额并判断
                if len(less) < unit_money[s]:
                    less = ['' for _ in range(unit_money[s])]
                    max_money = s
        if len(res.split(max_money)) > 1:
            first = res.split(max_money)[0]
            second = res.split(max_money)[1]
        else:
            first = res.split(max_money)[0]
            second = []
        tmp = []
        inner = []
        for cn in first:
            if cn != '零':
                inner.append(self.money_number[cn])
            else:
                tmp.append(inner)
                inner = []
        tmp.append(inner)
        all = 0
        for need_calc in tmp:
            tp = 0
            for i in range(len(need_calc)):
                # 是最后一个数据，并且是奇数的时候
                if i + 1 == len(need_calc) and (i + 1) % 2 != 0:
                    tp += int(need_calc[i])
                if (i + 1) % 2 == 0:
                    tp += int(need_calc[i]) * int(need_calc[i - 1])
            all += tp
        all = str(all)
        if len(all) != 4:
            all = ('0' * (4 - len(all))) + all
        if not second:
            return all
        else:
            return all + self.change_big(second)

    money_number = {item[1]: item[0] for item in number_change.items()}
    money_cn = [item[1] for item in number_change.items()] + ['元', '拾', '佰', '仟', '万', '亿', '整']

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