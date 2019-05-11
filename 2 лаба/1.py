words = "плов Плов пилот курорт курсов ботов".split(' ')
words = [x for x in words if x[-2:len(x):1] == 'ов']
print(words)