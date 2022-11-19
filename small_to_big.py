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
