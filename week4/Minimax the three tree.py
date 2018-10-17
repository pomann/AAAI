###########################################################
#														  #
#    REPLACE THE LIST IN enumerate() BY YOUR OWN LIST	  #
#														  #
###########################################################


def sol():
    return max(min(s) for s in [[x[1] for x in enumerate([36, 22, 9, 22, 10, 19, 28, 17, 37]) if x[0] < i*3 and x[0] >= (3 * (i - 1))] for i in range(1,4)])
