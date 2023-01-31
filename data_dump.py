#pip install pymongo
import pymongo
import pandas as pd
import json



client = pymongo.MongoClient("mongodb+srv://sup:Sup2023@cluster0.klxaggu.mongodb.net/?retryWrites=true&w=majority")
db = client.test
data_file_path = (r"C:\Users\supraja.yarramsetti\Desktop\medexp\Predicting-MedExp-using-ml\insurance.csv")
database_name = "insurence"
collection_name = 'insurence_project'

if __name__=='__main__':
    df = pd.read_csv(data_file_path)
    #print(f"Rows and Columns:{df.shape}")

    df.reset_index(drop = True,inplace = True)

    # to make the data as key value pair as mongo db works as key_value pair
    #T --> transpose 

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    client[database_name][collection_name].insert_many(json_record)
