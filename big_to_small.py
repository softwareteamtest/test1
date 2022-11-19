
    def big_to_small(self, big):
        change_int = ''
        change_int = self.change_big(big[:-1])
        remove = 0
        for s in change_int:
            if s != '0':
                break
            remove += 1
        res_small = change_int[remove:]
        return res_small
