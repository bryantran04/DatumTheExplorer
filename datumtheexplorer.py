# Import the modules needed to run the script.
import sys
import os
import numpy as np
import pandas as pd
import seaborn as sns
%matplotlib inline

menu_actions  = {}
data = None
 

def main_menu():
    os.system('clear')
    
    print ("Welcome,\n")
    print ("Please choose the menu you want to start:")
    print ("1. Load Data")
    print ("2. Null Values")
    print ("3. Joint Plot")
    print ("4. Correlation Plot")
    print ("5. Count Plot")
    print ("6. Simple Linear Regression Plot")
    print ("\n0. Quit\n")
    choice = input(" >>  ")
    exec_menu(choice)
 
    return
 
# Execute menu
def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print ("Invalid selection, please try again.\n")
            menu_actions['main_menu']()
    return

def inputDataHelper():
    print("Please enter Dataframe name: ")
    datainput = input(" >>  ")
    inputData(datainput)
    menu_actions['main_menu']()
def inputData(datainput):
    print(datainput)
    global data
    data = eval(datainput)
#Null Values
def nullValues():
    print(sns.heatmap(data.isnull(),yticklabels=False,cbar=False,cmap='viridis'))
    plt.show()
    print(data.isnull().sum())
    menu_actions['main_menu']()

def jointPlotHelper():
    print("Please enter xaxis name: ")
    x = input(" >>  ")
    print("Please enter yaxis name: ")
    y = input(" >>  ")
    jointPlot(x,y)
def jointPlot(xaxis,yaxis):
    print(sns.jointplot(data = data, x=xaxis, y=yaxis))
    plt.show()
    menu_actions['main_menu']()
    
def correlationPlot():
    global data
    corr = data.corr()
    corr = corr.style.background_gradient()
#     plt.show()
    print(corr)
#     sns.heatmap(data.corr(),cmap='coolwarm',annot=True)
#     plt.show()
    menu_actions['main_menu']()
    
def countPlotHelper():    
    print("Please enter xaxis name: ")
    x = input(" >>  ")
    countPlot(x)
def countPlot(xaxis):    
    sns.set_style('whitegrid')
    print(sns.countplot(x=xaxis,data=data,palette='RdBu_r'))
    plt.show()
    menu_actions['main_menu']()

    
def simpleRegressionHelper():
    print("Please enter xaxis name: ")
    x = input(" >>  ")
    print("Please enter yaxis name: ")
    y = input(" >>  ")
    simpleRegression(x,y)
def simpleRegression(xaxis,yaxis):
    print(sns.lmplot(data = data, x=xaxis, y=yaxis))
    plt.show()
    menu_actions['main_menu']()
    
    
# Menu 1
def menu1():
    print ("Hello Menu 1 !\n")
    print ("9. Back")
    print ("0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)
    return
 
 
# Back to main menu
def back():
    menu_actions['main_menu']()
 
# Exit program
def exit():
    sys.exit()

def hello():
    os.system('clear')
    menu_actions['main_menu']()
 
# =======================
#    MENUS DEFINITIONS
# =======================
 
# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': inputDataHelper,
    '2': nullValues,
    '3': jointPlotHelper,
    '4': correlationPlot,
    '5': countPlotHelper,
    '6': simpleRegressionHelper,
    '9': back,
    '0': exit,
}
 

#Run the Program
if __name__ == "__main__":

    main_menu()
