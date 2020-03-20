from math import sqrt
def count_length(height, accuracy:bool):
    radius = 6000 #km

    if accuracy: length = sqrt( 2 * radius * height + height ** 2)
    else: length = sqrt( 2 * radius * height)

    return length

def matrix(start, stop, epsilon):
    while start <= stop:
        acc = count_length(start, True)
        not_acc = count_length(start, False)
        delta = str(acc - not_acc)
        print("accurate: " +  str(acc) + "   not accurate: " + str(not_acc) + "    delta: " + delta)
        start += epsilon

def matrix_extra(start, stop, epsilon):

    all_values = []

    while start <= stop:
        acc = count_length(start, True)
        not_acc = count_length(start, False)
        delta = acc - not_acc
        percentage = delta/acc 
        all_values.append([start, acc, not_acc, delta, percentage * 100])
        start += epsilon
    return all_values

