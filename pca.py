from sklearn.decomposition import PCA
import  matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#Global variables declaration
import globals
from PyQt5.QtWidgets import *
n_samples = 0
n_features = 0
eig_val = []
load_matrix = []
col_mean = []
col_var = []
score_matrix = []
runtime = []
wavelength = []
wavelength_contrib = []
X = []
score = []
load = []
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号 #有中文出现的情况，需要u'内容'
#%%

def get_data(train_data_path):
    global n_samples,n_features,runtime,wavelength,X
    #get source data
    X=np.array(pd.read_excel(train_data_path))
    X=np.delete(X,0,1)
    runtime=(np.delete(X[:,0],0,0))[:211]
    X=np.delete(X,0,1)
    wavelength=(X[0,:])
    #get X except runtime and wavelength
    X=np.array(np.delete(X,0,0),dtype=np.float64)[:211,]
    #size
    n_samples, n_features = X.shape
    print('norm_X.shape',X.shape)

def pca():
    global load_matrix, score_matrix
    pca = PCA(n_components = 0.98)
    pca_obj = np.array(pca.fit_transform(X))
    score_matrix = pca_obj
    print('pca_obj.shape',pca_obj.shape)
    print(pca_obj.shape)
    # Principal Components Weights (Eigenvectors)
    load_matrix = np.array(pca.components_)
    print('load_matrix.shape:',load_matrix.shape)
    return score_matrix,load_matrix

def write_load_score(file_name):
    #写入excel
    data_score = pd.DataFrame(score_matrix)
    writer_score = pd.ExcelWriter('D:\File\data_oes\score_file\score_%s.xlsx'%file_name)		# 写入Excel文件
    data_score.to_excel(writer_score, 'Sheet1')		# ‘page_1’是写入excel的sheet名
    writer_score.save()
    writer_score.close()

    data_load = pd.DataFrame(load_matrix)
    writer_load = pd.ExcelWriter('D:\File\data_oes\load_file\load_%s.xlsx'%file_name)		# 写入Excel文件
    data_load.to_excel(writer_load, 'Sheet1')		# ‘page_1’是写入excel的sheet名
    writer_load.save()
    writer_load.close()

def write_data(file_name,data):
    data_prim = pd.DataFrame(data)
    writer_data = pd.ExcelWriter(globals.file_dir+'\%s.xlsx'%file_name)		# 写入Excel文件
    data_prim.to_excel(writer_data, 'Sheet1')		# ‘page_1’是写入excel的sheet名
    writer_data.save()
    writer_data.close()
def read_score_load(score_data_path):
    return np.array(pd.read_excel(score_data_path,sheet_name='Sheet1'))[:,1:]

def get_score_load(file_name):
    global score
    score = []
    s_t = []
    for i in range(len(file_name)):
        s_t.append(read_score_load('D:\File\data_oes\score_file\score_%s.xlsx'%file_name[i]))
    score = np.array(s_t)
    print('score.shape:',score.shape)




def get_mean_score():
    sc_mean = []
    for i in range(score.shape[2]):
        sc_mean.clear()
        sc=score[:,:,i]
        for j in range(sc.shape[0]):
            sc_mean.append(np.mean(sc[j,]))
        break
    print(sc_mean)
    return sc_mean

def process_control(file_name,path_list):
    for j in range(len(path_list)):
        temp_path = path_list.__getitem__(j)
        #get data
        get_data(temp_path)
        #PCA
        pca()
        #write_load_score
        write_load_score(file_name[j])
    get_score_load(file_name)
    return get_mean_score()