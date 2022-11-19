def small_to_big(self, small):  ##小写转大写
    max, min = self.validate(val=small)
    big_str = '整'
    change_swap = ['', '拾', '佰', '仟']
    unit_swap = ['元', '万', '亿', '兆']
    for index, num in enumerate(max[::-1]):
        if index % 4 == 0:
            change_swap[0] = unit_swap[index // 4]
            if num == '0':  ##4的整数倍位零不加
                big_str += change_swap[index % 4]
                continue
            big_str += '%s%s' % (change_swap[index % 4], self.NUM_DICT[num])
        else:
            if num == '0':
                big_str += self.NUM_DICT[num]
                continue
            big_str += '%s%s' % (change_swap[index % 4], self.NUM_DICT[num])
    # 去掉多于的零
    big_str = big_str[::-1]
    tmp_str = ''
    for i in range(len(big_str)):
        if i == len(big_str):
            continue
        if big_str[i] == '零' and big_str[i + 1] == '零':
            continue
        if big_str[i] == '零' and big_str[i + 1] in unit_swap:
            continue
        tmp_str += big_str[i]
    return tmp_str