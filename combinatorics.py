def get_perms(string):
    perms = set()

    def permute(letters, cur=''):
        if len(letters) == 0:
            return perms.add(cur)
        for i in range(len(letters)):
            permute(letters[:i] + letters[i + 1:], cur + letters[i])

    permute(string)
    return list(perms)


print(get_perms('abc'))


def get_combs(string, choose=0):
    if choose == 0:
        choose = len(string) - 1
    combs = []

    def comb(letters, cur=''):
        if len(cur) == choose:
            return combs.append(cur)
        for i in range(len(letters)):
            comb(letters[i + 1:], cur + letters[i])

    comb(string)
    return combs


print(get_combs('abcdef', 2))


def get_cart(l1, l2):
    return [(x, y) for x in l1 for y in l2]


print(get_cart([1, 2, 3], [10, 20, 30]))