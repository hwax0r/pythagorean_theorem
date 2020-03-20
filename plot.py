from calcs import *
import csvOutput
import matplotlib.pyplot as plt

csvOutput.func(matrix_extra(1, 10000000000, 10000000))
#csvOutput.func(matrix_extra(1, 1000000, 10000))


# all_values = []
# all_percentage = []
# all_deltas = []

# start = 1
# stop = 10000000000000
# epsilon = 1000000
# all_acc = []
# all_notacc = []

# while start <= stop:
#     acc = count_length(start, True)
#     not_acc = count_length(start, False)
#     delta = acc - not_acc
#     percentage = delta/acc 
#     all_values.append([start, acc, not_acc, delta, percentage * 100])
#     all_percentage.append(percentage * 100)
#     all_deltas.append(delta)
#     all_acc.append(acc)
#     all_notacc.append(not_acc)
#     start += epsilon

# # plt.plot(all_deltas, all_percentage, all_acc, all_notacc)
# plt.hlines(all_notacc, 0, all_acc)
# plt.show()