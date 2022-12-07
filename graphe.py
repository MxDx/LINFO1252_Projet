import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

if __name__ == '__main__':
    NBTHREAD = 64
    
    #Philosophes
    
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
    
    
    #Philosophes AA
    
    print("="*90)
    print("Graph for philosophe_AA implementation")
    print("="*90)

    philosophe_AA = pd.read_csv("test_philosophe_AA.csv", sep=';')

    philosophe_AA = philosophe_AA.iloc[:,:-1]
    dic = {'1 threads': 1,'2 threads': 2,'4 threads': 4,'8 threads': 8,'16 threads': 16,'32 threads': 32,'64 threads': 64}
    philosophe_AA = philosophe_AA.rename(columns=dic)

    philosophe_AA_new = philosophe_AA.mean().to_frame(name="mean")
    philosophe_AA_new["std"] = philosophe_AA.std().to_list()
    # philosophe_AA_new["nb_thread"] = [1,2,4,8,16,32,64]
    
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 8))
    philosophe_AA_new.plot(y='mean', ax=axes[0], kind='bar', title='Mean')
    philosophe_AA_new.plot(y='std', ax=axes[1],kind='bar', title="Standard deviation", color='orange')
    
    print(philosophe_AA_new.head())
    plt.show()
    
    
    # Comp
    comp_philosophe = philosophe_new.rename(columns={'mean':'mean_POSIX', 'std': 'std_POSIX'})
    comp_philosophe['mean_AA'] = philosophe_AA_new['mean']
    comp_philosophe['std_AA'] = philosophe_AA_new['std']
    
    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(15,8))
    comp_philosophe.plot(y=['mean_POSIX', 'mean_AA'], ax=axes, kind='bar', title='Mean', grid=True)
    plt.show()
    
    
    #Producteurs-Consomateurs =====================================================================================================================================
    
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
    
    
    #Producteurs-Consomateurs AA =====================================================================================================================================
    
    
    print("="*90)
    print("Graph for producteurs-consomateurs_AA implementation")
    print("="*90)
    
    producteurs_consomateurs_AA = pd.read_csv("test_producteurs_consommateur_AA.csv", sep=';')
    producteurs_consomateurs_AA = producteurs_consomateurs_AA.iloc[:,:-1]
    producteurs_consomateurs_AA_new = producteurs_consomateurs_AA.mean().to_frame(name="mean")
    producteurs_consomateurs_AA_new['std'] = producteurs_consomateurs_AA.std().to_list()

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 8))
    producteurs_consomateurs_AA_new.plot(y='mean', ax=axes[0], kind='bar', title='Mean')
    producteurs_consomateurs_AA_new.plot(y='std', ax=axes[1],kind='bar', title="Standard deviation", color='orange')
    
    print(producteurs_consomateurs_AA_new.head())
    plt.show()

    # Comp
    comp_producteurs_consomateurs = producteurs_consomateurs_new.rename(columns={'mean':'mean_POSIX', 'std': 'std_POSIX'})
    comp_producteurs_consomateurs['mean_AA'] = producteurs_consomateurs_AA_new['mean']
    comp_producteurs_consomateurs['std_AA'] = producteurs_consomateurs_AA_new['std']
    
    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(15,8))
    comp_producteurs_consomateurs.plot(y=['mean_POSIX', 'mean_AA'], ax=axes, kind='bar', title='Mean', grid=True)
    plt.show()
    
    
    #Lecteurs-écrivains ================================================================================================================================================
    
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

    
    
    #Lecteurs-écrivains AA ================================================================================================================================================
    
    print("="*90)
    print("Graph for lecteurs-ecrivains_AA implementation")
    print("="*90)
    
    lecteurs_ecrivains_AA = pd.read_csv("test_lecteurs-Ecrivains_AA.csv", sep=';')
    lecteurs_ecrivains_AA = lecteurs_ecrivains_AA.iloc[:,:-1]
    lecteurs_ecrivains_AA_new = lecteurs_ecrivains_AA.mean().to_frame(name="mean")
    lecteurs_ecrivains_AA_new['std'] = lecteurs_ecrivains_AA.std().to_list()

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 8))
    lecteurs_ecrivains_AA_new.plot(y='mean', ax=axes[0], kind='bar', title='Mean')
    lecteurs_ecrivains_AA_new.plot(y='std', ax=axes[1],kind='bar', title="Standard deviation", color='orange')

    print(lecteurs_ecrivains_AA_new.head())
    plt.show()
    
    # comp
    comp_lecteurs_ecrivains = lecteurs_ecrivains_new.rename(columns={'mean':'mean_POSIX', 'std': 'std_POSIX'})
    comp_lecteurs_ecrivains['mean_AA'] = lecteurs_ecrivains_AA_new['mean']
    comp_lecteurs_ecrivains['std_AA'] = lecteurs_ecrivains_AA_new['std']
    
    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(15,8))
    comp_lecteurs_ecrivains.plot(y=['mean_POSIX', 'mean_AA'], ax=axes, kind='bar', title='Mean', grid=True)
    plt.show()
    
    
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
    
    
    
    