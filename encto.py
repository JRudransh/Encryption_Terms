""" Encryption Terms One The Encryption of numbers"""


class NEncryptTSK:
    """The Encryption of number with two single keys"""
    def __init__(self, first_key=2, second_key=5):
        self.done = False
        self.values = []
        self.o = 0
        self.multiplier = 1
        self.rm = 0
        self.dd = 0
        self.tn = 0
        self.tv = 0
        if first_key > second_key:
            mn = second_key
            mx = first_key
        elif first_key < second_key:
            mn = first_key
            mx = second_key
        elif first_key == second_key:
            mn = first_key
            mx = first_key + 4
        else:
            mn = 2
            mx = 5
        self.mn_value = mn
        self.mx_value = mx
        self.mx_range = self.mx_value + 1
        self.mid_value = self.mx_range - self.mn_value

    def calc(self, n):
        self.tn = n
        while not self.done:
            self.rm = self.tn % self.mid_value
            self.values.append(self.rm)
            self.dd = self.tn // self.mid_value
            if self.dd > self.mid_value:
                self.tn = self.dd
            else:
                self.values.append(self.dd)
                break

        for i in self.values:
            self.tv = self.multiplier * (i + self.mn_value)
            self.o += self.tv
            self.multiplier *= 10

        return self.o


class NDecryptTSK:
    """The Decryption of number with two single keys"""
    def __init__(self, first_key=2, second_key=5):
        if first_key > second_key:
            mn = second_key
            mx = first_key
        elif first_key < second_key:
            mn = first_key
            mx = second_key
        elif first_key == second_key:
            mn = first_key
            mx = first_key + 4
        else:
            mn = 2
            mx = 5
        self.mn_value = mn
        self.mx_value = mx
        self.mx_range = self.mx_value + 1
        self.mid_value = self.mx_range - self.mn_value
        self.first = True
        self.rev = 0

    def calc(self, n):
        for i in str(n):
            i = int(i) - self.mn_value
            if self.first:
                self.rev = i * self.mid_value
                self.first = False
            else:
                self.rev = (self.rev + i) * self.mid_value
        self.rev /= self.mid_value
        self.rev = int(self.rev)
        return self.rev
