Project: Machine Learning with dataset    
ID a dataset: https://www.kaggle.com/uciml/student-alcohol-consumption#student-por.csv  
ID a machine learning algorithm: Linear Regression


First:  
 run make docker-all 
  
Second:  
 Go to http://localhost:8080/ to verify it is running
 Once you get the 'it's working' message, adjust the endpoints to be:
 http://localhost:8080/data/output/test  
 This will download the data
  
Third:  
 go to http://localhost:8080/experiment/regression  
 this should run the experiment with a test size of 20% and return a table of true vs predicted values  
  
Fourth:  
 go to http://localhost:8080/experiment/regression/barplot  
 this should return a png of a bar plot of the true vs predicted values  
  
Fifth:  
 go to http://localhost:8080/experiment/regression  
 now enter your own float value between 0.1 and 0.9 on the end  
 ex: http://localhost:8080/experiment/regression/0.5  
 this should give you another true vs predicted value table, but with a test size of 50%. The default value is 0.2 or 20%        
