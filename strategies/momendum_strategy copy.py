# --- Do not remove these libs ---
from freqtrade.strategy import IStrategy
from pandas import DataFrame
import talib.abstract as ta


# --------------------------------


class ADXMomentum(IStrategy):
    """

    author@: Gert Wohlgemuth

    converted from:

        https://github.com/sthewissen/Mynt/blob/master/src/Mynt.Core/Strategies/AdxMomentum.cs

    """


    # Minimal ROI designed for the strategy.
    # adjust based on market conditions. We would recommend to keep it low for quick turn arounds
    # This attribute will be overridden if the config file contains "minimal_roi"
    
    minimal_roi = {
        "0": 0.375,
        "106": 0.084,
        "282": 0.059,
        "518": 0
    }
#
#    minimal_roi = {
#        "0": 100
#    }
    
    # Optimal stoploss designed for the strategy
    stoploss = -0.173

    # Optimal timeframe for the strategy
    timeframe = '1h'
    #was 1h

    # Number of candles the strategy requires before producing valid signals
    startup_candle_count: int = 20

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe['adx'] = ta.ADX(dataframe, timeperiod=21)
        dataframe['plus_di'] = ta.PLUS_DI(dataframe, timeperiod=21)
        dataframe['minus_di'] = ta.MINUS_DI(dataframe, timeperiod=23)
        dataframe['sar'] = ta.SAR(dataframe)
        dataframe['mom'] = ta.MOM(dataframe, timeperiod=12)

        return dataframe

    def populate_buy_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (
                    (dataframe['adx'] > 30) &
                    (dataframe['mom'] > 0) &
                    (dataframe['plus_di'] > 30) &
                    (dataframe['plus_di'] > dataframe['minus_di'])

            ),
            'buy'] = 1
        return dataframe

    def populate_sell_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (
                    (dataframe['adx'] > 35) &
                    (dataframe['mom'] < 0) &
                    (dataframe['minus_di'] > 35) &
                    (dataframe['plus_di'] < dataframe['minus_di'])

            ),
            'sell'] = 1
        return dataframe
