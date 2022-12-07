import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

if __name__ == '__main__':
    NBTHREAD = 64

    philosophe_raw = pd.read_csv("test_philosophe.csv", sep=';')

    philosophe_raw = philosophe_raw.iloc[:,:-1]
    philosophe = philosophe_raw.mean().to_frame(name="mean")
    philosophe['nb_thread'] = [1,2,4,8,16,32,64]
    philosophe.plot(x='nb_thread', kind='bar')
    
    """time_phil = prediction_log(philosophe, NBTHREAD, 1)"""
    
    producteurs_consomateurs_raw = pd.read_csv("test_producteurs_consommateur.csv", sep=';')
    producteurs_consomateurs_raw = producteurs_consomateurs_raw.iloc[:,:-1]
    producteurs_consomateurs = producteurs_consomateurs_raw.mean().to_frame(name="mean")
    producteurs_consomateurs['nb_thread'] = [2,4,8,16,32,64]
    producteurs_consomateurs.plot(x='nb_thread', kind='bar')
    
    """time_prod_cons = prediction_log(producteurs_consomateurs, NBTHREAD, 2)"""
    
    lecteurs_ecrivains_raw = pd.read_csv("test_lecteurs-Ecrivains.csv", sep=';')
    lecteurs_ecrivains_raw = lecteurs_ecrivains_raw.iloc[:,:-1]
    lecteurs_ecrivains = lecteurs_ecrivains_raw.mean().to_frame(name="mean")
    lecteurs_ecrivains['nb_thread'] = [2,4,8,16,32,64]
    lecteurs_ecrivains.plot(x='nb_thread', kind='bar')

    
    
    """"time_lect_ecriv = prediction_log(lecteurs_ecrivains, NBTHREAD, 2)"""
    
    # total_time = time.strftime('%M:%S', time.gmtime(time_phil[0]+time_prod_cons[0]+time_lect_ecriv[0]))
    
    # print("\n")
    # print("="*80)
    # print(f'Results ({NBTHREAD} threads):')
    # print(f'Estimated time for philosophe:\t \t \t{time_phil[1]}')
    # print(f'Estimated time for producteurs-consomateurs:\t{time_prod_cons[1]}')
    # print(f'Estimated time for lecteurs-ecrivains:\t \t{time_lect_ecriv[1]}')
    # print("="*80)
    # print(f'Total time:\t{total_time}')
    # print("="*80)  