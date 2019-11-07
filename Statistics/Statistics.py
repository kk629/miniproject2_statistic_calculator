from Calculator.Calculator import Calculator
import random


def sample_method(num):
    r = random.randint(30, 51)
    sample_list = random.sample(num, r)
    return sample_list


def population_Mean(num):
    n_sum = addition(num)
    return n_sum / len(num)


def Median(num):
    list_num = [num[i] for i in range(len(num))]
    list_num.sort()
    l_num = len(num)
    if l_num % 2 == 1:
        i = int((l_num + 1) / 2) - 1
        return list_num[i]
    else:
        i = int(l_num / 2) - 1
        return (list_num[i] + list_num[i + 1]) / 2


def mode(num):
    dict_num = {}
    for i in range(len(num)):
        if num[i] in dict_num.keys():
            dict_num[num[i]] += 1
        else:
            dict_num.setdefault(num[i], 1)
    max_key = []
    m = max(dict_num.values())
    for k, v in dict_num.items():
        if m == v:
            max_key.append(k)
    return max_key


def Population_Standard_Deviation(num):
    average = population_Mean(num)
    s = 0.0
    for i in num:
        s += (i - average) ** 2
    return square_root(float(s) / len(num))


def Population_Variance(num):
    deviation = Population_Standard_Deviation(num)
    return square(deviation)


def proportion(num):
    proportion_list = []
    for g in num:
        h = g / addition(num)
        proportion_list.append(h)
    return proportion_list


def Variance_of_population_proportion(num):
    variance_p = proportion(num)
    return Population_Variance(variance_p)


def Z_Score(num):
    average1 = population_Mean(num)
    deviation1 = Population_Standard_Deviation(num)
    score_list = []
    for x in num:
        f = (x - average1) / deviation1
        score_list.append(f)
    return score_list


def Population_Correlation_Coefficient(num, num1):
    z1 = Z_Score(num)
    z2 = Z_Score(num1)
    z1_z2 = list(map(lambda x, y: x * y, z1, z2))
    p = sum(z1_z2) / len(z1_z2)
    return p


def Confidence_Interval(num):
    x1 = population_Mean(num)
    c = 0.95
    z_value = (1-c) / 2
    d1 = Population_Standard_Deviation(num)
    l1 = square_root(len(num))
    return [x1 - z_value*d1 / l1, x1 + z_value*d1 / l1]


def sample_mean(num):
    sample_list1 = sample_method(num)
    print(sample_list1)
    return population_Mean(sample_list1)


def Sample_Standard_Deviation(num):
    sample_average = sample_mean(num)
    return Population_Standard_Deviation(sample_average)

class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def mean(self):
        self.result = mean(self.data)
        return self.result

    if __name__ == '__main__':
        num_list = [1, 2, 3, 50, 1, 1, 5, 6]
        num1_list = [2, 3, 4, 5, 1, 5, 8, 8]
        mean = population_Mean(num_list)
        print("mean is :")
        print(mean)
        median = Median(num_list)
        print(median)
        mode1 = mode(num_list)
        print(mode1)
        sd = Population_Standard_Deviation(num_list)
        print("this is dev")
        print(sd)
        va = Population_Variance(num_list)
        print("this is var")
        print(va)
        scoreT = Z_Score(num_list)
        print(scoreT)
        t_z1_z2 = Population_Correlation_Coefficient(num_list, num1_list)
        print(t_z1_z2)
        variance_prop0ration = Variance_of_population_proportion(num_list)
        print(variance_prop0ration)
        interval = Confidence_Interval(num_list)
        print("this interval")
        print(interval)
        pro = proportion(num_list)
        print("this is prop")
        print(pro)