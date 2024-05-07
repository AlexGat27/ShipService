from tabulate import tabulate

def tabulating_result(result):
    columns = ("ID", "Indicator")
    if len(result) > 1:
        return tabulate(result, headers=columns, tablefmt="grid",maxcolwidths=50)
    else: return tabulate([result], headers=columns, tablefmt="grid",maxcolwidths=50)