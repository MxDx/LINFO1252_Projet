import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

if __name__ == '__main__':
    NBTHREAD = 64
    
    print("="*90)
    print("Graph for philosophe implementation")
    print("="*90)

    philosophe = pd.read_csv("test_philosophe.csv", sep=';')

    philosophe = philosophe.iloc[:,:-1]
    dic = {'1 threads': 1,'2 threads': 2,'4 threads': 4,'8 threads': 8,'16 threads': 16,'32 threads': 32,'64 threads': 64}
    philosophe = philosophe.rename(columns=dic)

    philosophe_new = philosophe.mean().to_frame(name="mean")
    philosophe_new["std"] = philosophe.std().to_list()
    # philosophe_new["nb_thread"] = [1,2,4,8,16,32,64]
    
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 8))
    philosophe_new.plot(y='mean', ax=axes[0], kind='bar', title='Mean')
    philosophe_new.plot(y='std', ax=axes[1],kind='bar', title="Standard deviation", color='orange')
    
    print(philosophe_new.head())
    plt.show()
    
    """time_phil = prediction_log(philosophe, NBTHREAD, 1)"""
    
    print("="*90)
    print("Graph for producteurs-consomateurs implementation")
    print("="*90)
    
    producteurs_consomateurs = pd.read_csv("test_producteurs_consommateur.csv", sep=';')
    producteurs_consomateurs = producteurs_consomateurs.iloc[:,:-1]
    producteurs_consomateurs_new = producteurs_consomateurs.mean().to_frame(name="mean")
    producteurs_consomateurs_new['std'] = producteurs_consomateurs.std().to_list()

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 8))
    producteurs_consomateurs_new.plot(y='mean', ax=axes[0], kind='bar', title='Mean')
    producteurs_consomateurs_new.plot(y='std', ax=axes[1],kind='bar', title="Standard deviation", color='orange')
    
    print(producteurs_consomateurs_new.head())
    plt.show()
    
    
    """time_prod_cons = prediction_log(producteurs_consomateurs, NBTHREAD, 2)"""
    
    print("="*90)
    print("Graph for lecteurs-ecrivains implementation")
    print("="*90)
    
    lecteurs_ecrivains = pd.read_csv("test_lecteurs-Ecrivains.csv", sep=';')
    lecteurs_ecrivains = lecteurs_ecrivains.iloc[:,:-1]
    lecteurs_ecrivains_new = lecteurs_ecrivains.mean().to_frame(name="mean")
    lecteurs_ecrivains_new['std'] = lecteurs_ecrivains.std().to_list()

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 8))
    lecteurs_ecrivains_new.plot(y='mean', ax=axes[0], kind='bar', title='Mean')
    lecteurs_ecrivains_new.plot(y='std', ax=axes[1],kind='bar', title="Standard deviation", color='orange')

    print(lecteurs_ecrivains_new.head())
    plt.show()

    
    
    """"time_lect_ecriv = prediction_log(lecteurs_ecrivains, NBTHREAD, 2)"""
    
    #TAS
    
    print("="*90)
    print("Graph for tas implementation")
    print("="*90)
    
    tas = pd.read_csv("test_tas.csv", sep=';')
    tas = tas.iloc[:,:-1]
    tas_new = tas.mean().to_frame(name="mean")
    tas_new['std'] = tas.std().to_list()


    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 8))
    tas_new.plot(y='mean', ax=axes[0], kind='bar', title='Mean')
    tas_new.plot(y='std', ax=axes[1],kind='bar', title="Standard deviation", color='orange')

    print(tas_new.head())
    plt.show()
    
    #TATAS
    
    print("="*90)
    print("Graph for tatas implementation")
    print("="*90)
    
    tatas = pd.read_csv("test_tatas.csv", sep=';')
    tatas = tatas.iloc[:,:-1]
    tatas_new = tatas.mean().to_frame(name="mean")
    tatas_new['std'] = tatas.std().to_list()


    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 8))
    tatas_new.plot(y='mean', ax=axes[0], kind='bar', title='Mean')
    tatas_new.plot(y='std', ax=axes[1],kind='bar', title="Standard deviation", color='orange')

    print(tatas_new.head())
    plt.show()
    
    
    #Comparaison
    
    comp_tastatas = tas_new.rename(columns={'mean':'mean_tas', 'std': 'std_tas'})
    comp_tastatas['mean_tatas'] = tatas_new['mean']
    comp_tastatas['std_tatas'] = tatas_new['std']
    
    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(15,8))
    comp_tastatas.plot(y=['mean_tas', 'mean_tatas'], ax=axes, kind='bar', title='Mean', grid=True)
    