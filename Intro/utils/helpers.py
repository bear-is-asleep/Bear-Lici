import matplotlib.pyplot as plt
import os
from datetime import date
import matplotlib.pylab as pylab
params = {'legend.fontsize': 'large',
          'figure.figsize': (7, 5),
         'axes.labelsize': 'large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'large',
         'ytick.labelsize':'large'}
pylab.rcParams.update(params)

#Plot organization
def format_plots():
  if 'science' in plt.style.available:
    plt.style.use('science')
  else:
    os.system('pip install SciencePlots -q')
    plt.style.reload_library()
    plt.style.use('science')



def make_plot_dir():
    day = date.today().strftime("%d_%m_%Y")
    isDir = os.path.isdir("Plots/Plots_"+day)
    if isDir == False:
        os.system("mkdir -p Plots_" +day)
        os.system("mv -n Plots_" +day+"/ Plots/")

def save_plot(fname):
    day = date.today().strftime("%d_%m_%Y")
    plt.savefig(fname,bbox_inches = "tight")
    os.system("mv " + fname + "* Plots/Plots_" +day+"/")

def plot_stuff():
  format_plots()
  make_plot_dir()

def plot_history(history,metric='loss',save=False,fname=''):
    loss = history.history[metric]
    val_loss = history.history[f'val_{metric}']
    
    plt.plot(loss,label='Training')
    plt.plot(val_loss,label='Validation')
    plt.xlabel('Epoch')
    plt.ylabel(metric.capitalize())
    plt.legend()
    if save:
        save_plot(fname)
        plt.close()
    else:
        plt.show()