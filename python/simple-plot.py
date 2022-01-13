import matplotlib.pyplot as plt

class SimplePlot:

    @staticmethod
    def plot(self, out_path, title, x, y, xlabel, ylabel):
        plt.style.use('ggplot')
        plt.style.use('seaborn-whitegrid')
        plt.figure(figsize=(10,10))

        # Plotting...
        sctr = plt.scatter(x, y, marker='o', color="tab:blue", alpha=0.9);  
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.xticks(rotation=90)
        plt.legend(handles=[sctr], loc='upper right', fontsize='xx-small', frameon=True)
        plt.savefig(out_path)
