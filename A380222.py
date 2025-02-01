import incomplete_knapsack as ik
import math


def item_input(file_name):
    with open(file_name, encoding="utf-8", mode="r") as f:
        lines = f.readlines()

    data = []
    for x in lines:
        line = x.split(",")
        data.append(
            ik.Item(
                line[0],
                int(line[1].replace("\n", "")),
                math.log(float(line[0])),
                len(data),
            )
        )

    return data


# A380222
item_list = item_input("A380222_factors.csv")

# these settings are speficially for the 14th primorial check. Adjust based on the values printed by the rust script.
sequence, item_list = ik.incomplete_knapsack(item_list, 0.187141861, 198, -1, 200, True)
# ik.sequence_output(sequence, "A380222_shorthand.csv", -1)
ik.sequence_to_explicit(sequence, item_list, "A380222.csv", 1000, 2)
# ik.sequence_to_explicit(sequence, item_list, "b380222.txt", 5000, 1, " ")  # create b file for OEIS
