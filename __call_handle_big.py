def __call_handle_big(self, big_str):
    # 利用递归函数实现处理输入的大写金额
    min_ls = []
    max_unit = ''
    unit_swap = {'元': 1, '万': 5, '亿': 9, '兆': 13}
    for s in unit_swap:
        if s in big_str:  # 接收一个输入的大写金额并判断
            if len(min_ls) < unit_swap[s]:
                min_ls = ['' for _ in range(unit_swap[s])]
                max_unit = s
    if len(big_str.split(max_unit)) > 1:
        front = big_str.split(max_unit)[0]
        back = big_str.split(max_unit)[1]
    else:
        front = big_str.split(max_unit)[0]
        back = []
    tmp_ls = []
    inner_ls = []
    for cn in front:
        if cn != '零':
            inner_ls.append(self.CN_TO_NUM[cn])
        else:
            tmp_ls.append(inner_ls)
            inner_ls = []
    tmp_ls.append(inner_ls)
    all_tp = 0
    for need_calc in tmp_ls:
        tp = 0
        for i in range(len(need_calc)):
            # 是最后一个数据，并且是奇数的时候
            if i + 1 == len(need_calc) and (i + 1) % 2 != 0:
                tp += int(need_calc[i])
            if (i + 1) % 2 == 0:
                tp += int(need_calc[i]) * int(need_calc[i - 1])
        all_tp += tp
    all_tp = str(all_tp)
    if len(all_tp) != 4:
        all_tp = ('0' * (4 - len(all_tp))) + all_tp
    if not back:
        return all_tp
    else:
        return all_tp + self.__call_handle_big(back)