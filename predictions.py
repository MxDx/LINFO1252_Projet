import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import scipy.stats as sp
import statsmodels.api as sm
import time


def prediction_linear(data: pd.core.frame.DataFrame, nb_thread: int, start: int):
    Xm = sm.add_constant(data['nb_thread'])

    model = sm.OLS(data['mean'], Xm)
    results = model.fit()

    print(results.summary())

    prediction = range(start,nb_thread)
    estimated_val = results.predict(sm.add_constant(prediction))

    plt.figure()
    plt.plot(data['nb_thread'], data['mean'])

    plt.plot(prediction, estimated_val)

    plt.grid()
    plt.show()

    estimated_time_sec = 5 * estimated_val.sum()
    estimated_time = time.strftime('%M:%S', time.gmtime(estimated_time_sec))    
    print("======================================================")
    print(f'With {nb_thread} threads:' + '\t' + estimated_time)
    print("======================================================")
    
    return estimated_time_sec, estimated_time

def prediction_log(data: pd.core.frame.DataFrame, nb_thread: int, start: int):
    Xm = sm.add_constant(data['nb_thread'])
    Xm['nb_thread'] = np.log(Xm['nb_thread'])

    model = sm.OLS(data['mean'], Xm)
    results = model.fit()

    print(results.summary())

    prediction = range(start,nb_thread)
    estimated_val = results.predict(sm.add_constant(np.log(prediction)))

    plt.figure()
    plt.plot(data['nb_thread'], data['mean'])

    plt.plot(prediction, estimated_val)

    x_ticks = [0,2]+[2**i for i in range(2,7)]
    plt.xticks(x_ticks)
    plt.grid()
    plt.show()

    estimated_time_sec = 5 * estimated_val.sum()
    estimated_time = time.strftime('%M:%S', time.gmtime(estimated_time_sec))
    print("======================================================")
    print(f'With {nb_thread} threads:' + '\t' + estimated_time)
    print("======================================================")
    
    return estimated_time_sec, estimated_time

if __name__ == '__main__':
    NBTHREAD = 64

    philosophe_raw = pd.read_csv("result_ingi/test_philosophe.csv", sep=';')

    philosophe_raw = philosophe_raw.iloc[:,:-1]
    philosophe = philosophe_raw.mean().to_frame(name="mean")
    philosophe['nb_thread'] = range(1,65)
    
    time_phil = prediction_log(philosophe, NBTHREAD, 1)
    
    producteurs_consomateurs_raw = pd.read_csv("result_ingi/Better_prodcons.txt", sep=';')
    producteurs_consomateurs_raw = producteurs_consomateurs_raw.iloc[:,:-1]
    producteurs_consomateurs = producteurs_consomateurs_raw.mean().to_frame(name="mean")
    producteurs_consomateurs['nb_thread'] = range(2,65)
    
    time_prod_cons = prediction_log(producteurs_consomateurs, NBTHREAD, 2)
    
    lecteurs_ecrivains_raw = pd.read_csv("result_ingi/Better_lecteur_écrivains.txt", sep=';')
    lecteurs_ecrivains_raw = lecteurs_ecrivains_raw.iloc[:,:-1]
    lecteurs_ecrivains = lecteurs_ecrivains_raw.mean().to_frame(name="mean")
    lecteurs_ecrivains['nb_thread'] = range(2,65)
    
    time_lect_ecriv = prediction_log(lecteurs_ecrivains, NBTHREAD, 2)
    
    total_time = time.strftime('%M:%S', time.gmtime(time_phil[0]+time_prod_cons[0]+time_lect_ecriv[0]))
    
    print("\n")
    print("="*80)
    print(f'Results ({NBTHREAD} threads):')
    print(f'Estimated time for philosophe:\t \t \t{time_phil[1]}')
    print(f'Estimated time for producteurs-consomateurs:\t{time_prod_cons[1]}')
    print(f'Estimated time for lecteurs-ecrivains:\t \t{time_lect_ecriv[1]}')
    print("="*80)
    print(f'Total time:\t{total_time}')
    print("="*80)    
