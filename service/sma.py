from pandas import DataFrame


class SMA:
    def __init__(self, sma=21, sma1=105):
        self.sma = sma
        self.sma1 = sma1

    def get_crossed(self, df: DataFrame) -> list:
        self.sma_df = df.rolling(window=self.sma).mean()
        sma_pers_df = df.div(self.sma_df).mul(100).sub(100)

        self.sma_week_df = df.rolling(window=self.sma1).mean()
        sma_week_pers_df = df.div(self.sma_week_df).mul(100).sub(100)

        df_prep = []
        tickers = sma_pers_df.columns.values.tolist()
        for ticker in tickers:
            sma_last = None
            counter = 0
            sma_d = 0
            sma_w = 0
            sma_last = 0
            date = None
            for index, _ in sma_pers_df.iterrows():
                sma_d = sma_pers_df[ticker][index]
                sma_w = sma_week_pers_df[ticker][index]
                if sma_d < sma_w:
                    date = index
                    counter += 1
                    sma_last = sma_d - sma_w
                else:
                    sma_last = 0
                    counter = 0
            df_prep.append([ticker, counter, sma_last, self.sma,
                           self.sma1, sma_d, sma_w, date, "cross"])
        df = DataFrame(df_prep, columns=['name', 'count', 'sma_diff', 'sma_size', 'sma_size1', 'sma_daily', 'sma_weekly', 'last_date', 'sma_type'])\
            .sort_values(by=['count', 'sma_diff'], ascending=False)

        self.lead_comps_df = df[df['count'] >= 2].drop_duplicates(subset=['name'])
        lead_comps = self.lead_comps_df['name'].values.tolist()
        return lead_comps
