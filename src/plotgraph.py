import matplotlib.pyplot as plt


class PlotGraph:
    def_style = ["-", "--", "-.", ":"]
    def_num = 0

    def __init__(self):
        pass

    def plot(self, p_path, g_path, st, gr, x, df):
        plt.figure(figsize=(st["graph_size"][0]*0.01, st["graph_size"][1]*0.01))
        plt.xlabel(gr["xlabel"])
        plt.ylabel(gr["ylabel"])
        for grp in gr["plot"]:
            if grp["style"] == "order":
                grp["style"] = self.def_style[self.def_num]
                self.def_num = self.def_num + 1 if self.def_num < 3 else 0

            if not grp["col"] in df.columns:
                print("error: column '"+grp["col"]+"' is not exist in", p_path)
                continue

            plt.plot(
                x, df[grp["col"]],
                label=grp["label"], color=grp["color"],
                linestyle=grp["style"], linewidth=grp["width"]
            )
        plt.xlim(st["xlim"])
        plt.ylim(gr["ylim"])

        plt.legend(loc=gr["legend"]["loc"],
                   bbox_to_anchor=gr["legend"]["bbox_to_anchor"],
                   ncol=gr["legend"]["ncol"])
        plt.savefig(g_path)
        plt.close()
