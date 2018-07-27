import pandas as pd
import sys 
data = pd.read_csv("hn_stories.csv", names =["submission_time", "upvotes", "url", "headline"])

def load_data(csv_file):
        data_frame = pd.read_csv(csv_file, names =["submission_time", "upvotes", "url", "headline"])
        return data_frame
    
if __name__ == "__main__":
     df = load_data(sys.argv[1])
     print(df.dtypes)
    
    
    
    
        