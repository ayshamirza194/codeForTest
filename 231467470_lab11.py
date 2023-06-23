import pandas as pd

def NaiveBayesClassifier(conditionSet):
    datasetfile = pd.read_csv('dataset_sunny.csv.xls')
    true_value = datasetfile[(datasetfile['Play']=='yes')]
    negative_value = datasetfile[(datasetfile['Play']=='no')]

    true_cnt = {}
    negative_cnt = {}

    true_probability = 1
    negative_probability = 1


    #looping through the dataset to find true and negative values and their count
    for x in datasetfile:
        for y in conditionSet:
            if true_value[x].value_counts().get(y) != None:
                true_cnt[y] = true_value[x].value_counts().get(y)

                if negative_value[x].value_counts().get(y) == None:
                    negative_cnt[y]=0
                    break

            elif negative_value[x].value_counts().get(y) != None:
                negative_cnt[y] = negative_value[x].value_counts().get(y)
                if true_value[x].value_counts().get(y) == None:
                    true_cnt[y]=0 
                    break       

     #true and negative probability of each test 
    for z in conditionSet:
        true_probability =(true_cnt[z]/len(true_value)) * true_probability 
        negative_probability =  (negative_cnt[z]/len(negative_value)) * negative_probability


    #true and negative probability of each dataset
    true_probability  = (len(true_value)/len(datasetfile)) * true_probability
    negative_probability = (len(negative_value)/len(datasetfile)) * negative_probability 

    #calulate probability of yes and no
    yes =(true_probability /(true_probability + negative_probability))
    no =(negative_probability/(negative_probability + true_probability ))

    if yes>no:
        return ['Yes',yes]
    else:
        return ['No',no]


print(NaiveBayesClassifier(['sunny', 'hot', 'normal', False]))        

    
