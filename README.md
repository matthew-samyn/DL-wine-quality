# Deep learning - Wine Quality challenge
## Description
  

## Installation
### Python version
* Python 3.9

### Packages used
* numpy==1.20.3
* pandas==1.3.2
* scikit-learn==0.24.2
* matplotlib==3.4.2
* tensorflow==2.6.0
* keras==2.6.0
* jupyter==1.0.0
* jupyterlab==3.1.10

## Usage
| File | Description |
|------|-------------|

## Step by step explanation of how I did it
#### 1. Categorised the quality, added this as an extra column: "target"  
+-------+-----------------------------+
| class | values                      |
+=======+=============================+
| 0     | Quality below or equal to 5 |
+-------+-----------------------------+
| 1     | Quality above or equal to 6 |
+-------+-----------------------------+

####  2. The search for a high score: categorical neural network



####  3. The search for a higher score: linear neural network
It did a pretty good job at predicting the quality just looking at it visually,  
but I was at a loss as to how I should give it a score.
I rounded the predictions of the model,   
and this is the confusion matrix I got out of it:
![](images/Regression_neural_network_2_categories_explanation_paint.png)
I noticed above that the model was actually doing a good job at what I did at my first step:  
Categorising by 0 and 1
![](images/Regression_neural_network_2_categories.png)
**Perfection!**   
But I wanted more.  
The linear model seemed to be good at predicting quality of 5, 6 and 7.  
Not coincidentally these were also the values of wich I had the most data on:
+---------------+-----------------------+
| quality value | number of data points |
+===============+=======================+
| 3             | 30                    |
+---------------+-----------------------+
| 4             | 206                   |
+---------------+-----------------------+
| 5             | 1751                  |
+---------------+-----------------------+
| 6             | 2323                  |
+---------------+-----------------------+
| 7             | 855                   |
+---------------+-----------------------+
| 8             | 148                   |
+---------------+-----------------------+
| 9             | 5                     |
+---------------+-----------------------+

#### 4. Upsampling my data










## Contributors
| Name          | Github                           |
|---------------|----------------------------------|
| Matthew Samyn | https://github.com/matthew-samyn |




## Timeline
07/09/2021 - 09/09/2021 