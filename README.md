# StocksPredictor

## Description
In this project, I analyzed the stock of Apple Inc. (AAPL), and tried to predict the closing stock price of the next day. These weere the steps I took to complete this project. 

### Processing the Data
The file, csv_get.py in the folder StockCSV allows you to download the historical data if any specified stock. After downloading Apple's stock information, I processed the csv file into my notebook (main.ipynb) through Pandas. I then split my data up into two sets: Training Data and Testing Data. The Training Data will be used to train my model and the Testing Data to test the accuracy of my model's predictions. 

### Building the Model
I constructed Keras' Sequential Model using Long Short-Term Memory (LSTM) layers, and Dense layers. For the loss function, I chose to use Mean Square Error (MSE)  to calculate the average squared difference between the predicted and actual values, providing a measure of how accurate the model is.

### Training Process
During the training process, I used trial and error to fine-tune the hyperparameters such as the batch size, and number of epochs to improve the model's accuracy. At the end, I found that a batch size of 1, and 10 number of epochs gave me the most accurate results.

### Results
After training and testing my model with the Apple stock data from 2019-05-07 to 2024-05-07, it predicted that the closing price for Apple Stock on 2024-05-08 will be $182.09. As of today (2024-05-09), I can conclude that I have succesfully trained my model to predict the Apple's future stock price as the actual closing price was $182.74, $0.65 away from my predicted price. Additionally, the model's predictions also follow the overall trends of the prices if you take a close look at the graphs.

## References
1. https://ca.finance.yahoo.com/
2. https://www.youtube.com/watch?v=QIUxPv5PJOY
3. https://keras.io/guides/sequential_model/ 
