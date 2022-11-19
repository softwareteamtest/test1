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
