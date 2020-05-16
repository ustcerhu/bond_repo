import pandas as pd
import numpy as np
import os,re,datetime,sys
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
#写个系统函数，输入质押券代码，返回质押券的交易历史信息
def Repo_history(code,data):
    '''
    统计券质押历史信息
    :param code: 质押券代码
    :param data: 历史数据库
    :return: 返回质押券回购历史交易及对手方信息
    '''
    history=data[data['质押券代码']==code][['质押券简称','折算率(%)','成交金额','回购天数','回购利率','对手方交易商','联系人']]
    #质押过的机构
    trader =data['质押券代码'].drop_duplicates()
    if code in trader.values:
        print('***************该券质押交易记录如下***************\n', history)
        trades=history[['对手方交易商','折算率(%)']].drop_duplicates()
        print('\n***************历史质押机构及折扣率如下***************\n',trades)
    else:
        print('Warning:该质押券代码无质押历史信息')
    return 0

if __name__ == '__main__':
    cwd = os.getcwd()
    os.chdir(cwd)
    df=pd.read_excel('协回交易记录20200511.xls',index_col=None)  #step1:读取表格文件
    vol = df['成交金额'].groupby(df['对手方交易商']).mean()
    print('\n***************交易对手平均出资金体量情况如下***************\n', vol)
    period = df['回购天数'].groupby(df['对手方交易商']).mean()
    print('\n***************交易对手出资金平均期限如下***************\n', period)
    rate = df['回购利率'].groupby(df['对手方交易商']).mean()
    print('\n***************交易对手出资金平均期限如下***************\n', rate)
    while True:
        try:
            code=np.int64(input('\n请输入质押券代码,参考如下格式：162202\n代码：'))  #格式才能和pandas数据格式匹配上
            Repo_history(code,df)
        except:
            print('输入有误，请重新输入')

