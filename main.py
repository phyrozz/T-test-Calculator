import statistics
import math


def enter_mode():
    mode = input("Enter test type: \n"
                 "\"t\" for t test (two-tailed with unequal variances)\n"
                 "\"r\" for pearson-r test (two-tailed with unequal variances): ")
    if mode == "t":
        input_t_test()
    elif mode == "r":
        input_pearson_r()
    else:
        print("Invalid input. Please try again.")
        enter_mode()


def input_t_test():
    first_set = input("Enter the first set of data\n(Must be separated by comma \",\" and there must be no spaces): ")
    first_set_list = first_set.split(",")
    first_set_list = [float(x) for x in first_set_list]
    second_set = input("Enter the second set of data\n(Must be separated by comma \",\" and there must be no spaces): ")
    second_set_list = second_set.split(",")
    second_set_list = [float(x) for x in second_set_list]
    print(first_set_list)
    print(second_set_list)
    confirm = input("Review your data shown above. Are you sure you want to continue?\n\"y\" for yes\n\"n\" for no: ")
    if confirm == "y" or confirm == "Y":
        calc_t_test(first_set_list, second_set_list)
    else:
        input_t_test()


def input_pearson_r():
    first_set = input("Enter the first set of data\n(Must be separated by comma \",\" and there must be no spaces): ")
    first_set_list = first_set.split(",")
    first_set_list = [float(x) for x in first_set_list]
    second_set = input("Enter the second set of data\n(Must be separated by comma \",\" and there must be no spaces): ")
    second_set_list = second_set.split(",")
    second_set_list = [float(x) for x in second_set_list]
    print(first_set_list)
    print(second_set_list)
    confirm = input("Review your data shown above. Are you sure you want to continue?\n\"y\" for yes\n\"n\" for no: ")
    if confirm == "y" or confirm == "Y":
        calc_pearson_r(first_set_list, second_set_list)
    else:
        input_pearson_r()


def calc_t_test(x, y):
    print("\nFirst set of data: ")
    print("Mean = " + str(statistics.mean(x)))
    print("Variance = " + str(statistics.variance(x)))
    print("StDev = " + str(statistics.stdev(x)))

    print("\nSecond set of data: ")
    print("Mean = " + str(statistics.mean(y)))
    print("Variance = " + str(statistics.variance(y)))
    print("StDev = " + str(statistics.stdev(y)))

    num = statistics.mean(x) - statistics.mean(y)
    denum = math.sqrt((statistics.stdev(x)**2 / len(x)) + (statistics.stdev(y)**2 / len(y)))
    t_calc = num / denum
    df = len(x) + len(y) - 2
    t_tabular_column = [12.71, 4.303, 3.182, 2.776, 2.571, 2.447, 2.365, 2.306, 2.262, 2.228, 2.201, 2.179, 2.160,
                        2.145, 2.131, 2.120, 2.110, 2.101, 2.093, 2.086, 2.080, 2.074, 2.069, 2.064, 2.060, 2.056,
                        2.052, 2.048, 2.045, 2.042]

    print("\ndf = " + str(df))
    print("t-tabular = " + str(t_tabular_column[df - 1]))
    print("t-calculated = " + str(abs(t_calc)))
    if abs(t_calc) > t_tabular_column[df - 1]:
        print("\nThere is a significant difference between the two sets of data.")

    elif abs(t_calc) <= t_tabular_column[df - 1]:
        print("\nThere is no significant difference between the two sets of data.")

    confirm = input("\nDo you want to continue? \n\"y\" for yes\n\"n\" for no: ")
    if confirm == "y" or confirm == "Y":
        enter_mode()
    else:
        return 0


def calc_pearson_r(x, y):
    sum_x = 0
    sum_y = 0
    xy = 0
    x_squared = 0
    y_squared = 0

    for i in range(len(x)):
        sum_x += x[i]
        sum_y += y[i]
        xy += x[i] * y[i]
        x_squared += x[i]**2
        y_squared += y[i]**2

    print("\nFirst set of data: ")
    print("Sum of x = " + str(sum_x))
    print("Sum of x^2 = " + str(x_squared))
    print("Mean = " + str(statistics.mean(x)))
    print("Variance = " + str(statistics.variance(x)))
    print("StDev = " + str(statistics.stdev(x)))

    print("\nSecond set of data: ")
    print("Sum of y = " + str(sum_y))
    print("Sum of y^2 = " + str(y_squared))
    print("Mean = " + str(statistics.mean(y)))
    print("Variance = " + str(statistics.variance(y)))
    print("StDev = " + str(statistics.stdev(y)))

    num = len(x) * xy - (sum_x * sum_y)
    denum = math.sqrt(((len(x) * x_squared) - sum_x ** 2) * ((len(x) * y_squared) - sum_y ** 2))
    r = num / denum

    t_calc = (r * math.sqrt(len(x) - 2)) / math.sqrt(1 - r**2)
    df = len(x) + len(y) - 2
    t_tabular_column = [12.71, 4.303, 3.182, 2.776, 2.571, 2.447, 2.365, 2.306, 2.262, 2.228, 2.201, 2.179, 2.160,
                        2.145, 2.131, 2.120, 2.110, 2.101, 2.093, 2.086, 2.080, 2.074, 2.069, 2.064, 2.060, 2.056,
                        2.052, 2.048, 2.045, 2.042]

    print("\nr = " + str(r))
    print("Sum of xy = " + str(xy))
    print("df = " + str(df))
    print("t-tabular = " + str(t_tabular_column[df - 1]))
    print("t-calculated = " + str(abs(t_calc)))
    if abs(t_calc) > t_tabular_column[df - 1]:
        print("\nThere is a significant relationship between the two sets of data.")

    elif abs(t_calc) <= t_tabular_column[df - 1]:
        print("\nThere is no significant relationship between the two sets of data.")

    confirm = input("\nDo you want to continue? \n\"y\" for yes\n\"n\" for no: ")
    if confirm == "y" or confirm == "Y":
        enter_mode()
    else:
        return 0


if __name__ == "__main__":
    print("This calculator currently supports two-tailed data with unequal variances only."
          "\nThe program is still work in progress. More features will be added in the near-future.\n"
          "Thank you.\n")
    enter_mode()
