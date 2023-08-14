# josh

Josh is the crypto-trading robot 🤖 I created thanks to #Freqtrade (https://www.freqtrade.io/en/stable/) open source framework. 

By deploying Josh to a cloud service (AWS, Digital Ocean), he can work for me 24/7 and trade according to market signal (he is so hardworking!). 

How to wake Josh up?

1. Start off 

   To start off docker image 
```
cd /Users/~/freqtrade/

docker-compose up -d
```

2. Download data

   I personally use Binance US data.
```
docker-compose run freqtrade download-data --exchange binanceus -t 15m
```
3. Backtesting

   Back test if all the hyperparameters are working well to serve the puspose of maximizing profit.

   **change to static pair list "method": "StaticPairList" in config.json file
```
docker-compose run freqtrade backtesting -s ADXMomentum
```

4. Hyperparameter Tuning

   **change to static pair list "method": "StaticPairList"
   
   **can later move back to VolumePairList
   
```
docker-compose run freqtrade hyperopt --hyperopt-loss SharpeHyperOptLossDaily --strategy ADXMomentumHopt -e 1500
```


5. Data Analysis

   Stop the container first, docker compose down.
   
   Open Jupiter notebook in browser using popped up url.
   
   Upload config.json and strategy file to the same directory as popped up Jupiter notebook.
   
```
cd /Users/~/freqtrade

docker-compose -f docker/docker-compose-jupyter.yml up
```

6. File transfer

   Use FileZilla to transfer configuration file to virtual machine or cloud.


7. Analyze trading results

   From time to time, use the strategy_analysis_AL.ipynb file to analyze and visualize trading results. Strategy needs constant update and analysis based on market    conditions.
