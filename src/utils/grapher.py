import matplotlib.pyplot as plt


def continuous_plot(
        ind_var, dep_var,
        title: str = "", graph_label: str = "",
        x_label: str = "", y_label: str = ""):
    plt.plot(ind_var, dep_var, label=graph_label)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()


def discrete_plot(
        ind_var, dep_var,
        title: str = "", graph_label: str = "",
        x_label: str = "", y_label: str = ""):
    plt.stem(ind_var, dep_var, label=graph_label)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()
    
def combined_plot(
        cont_ind_var, cont_dep_var,
        disc_ind_var, disc_dep_var,
        title: str = "", cont_label: str = "",
        disc_label: str = "", x_label: str = "", y_label: str = ""):
    plt.plot(cont_ind_var, cont_dep_var, label=cont_label)
    plt.stem(disc_ind_var, disc_dep_var, linefmt='r-', markerfmt='ro', basefmt='k-', label=disc_label)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()
