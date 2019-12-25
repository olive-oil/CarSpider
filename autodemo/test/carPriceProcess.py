import pandas as pd
#车牌-价格csv处理
if __name__=="__main__":
    data = pd.read_csv('../../data/CarPrice.csv')
    df = data.dropna()
    price = df['price'].str.extract(r'.*-(?P<price>.*)万')
    df2 = pd.concat([df['car'],price], axis=1)
    df3 = df2.assign(price = pd.to_numeric(df2['price'],errors='coerce'))
    price_agg = {'price': ['max','min','mean']}
    df4 = df3.groupby('car').agg(price_agg)
    df5 = df4['price']['mean']
    df6 = df4.loc[df5>=20]
    df6.columns = df6.columns.droplevel(0)
    df6.index = [index+'牌' for index in list(df6.index)]
    df6.index.names = ['car']
    df6.round(2).to_csv('../../data/CarPriceAgg.csvs', sep=';')