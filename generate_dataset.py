import fitz
import pandas as pd
import os

def get_path():
    final_path = []
    path1 = input('Enter the path for AI files: ')
    print('Path registered successfully')
    path2 = input('Enter the path for WEB files: ')
    print('Path registered sucessfully')
    final_path.append(path1)
    final_path.append(path2)
    return final_path

def get_content_of_pdfs(path_file):
    for path in path_file:
        if 'AI' in path:
            df_ai=get_final_dataframe(path,1)
            print(df_ai)
        elif 'WEB' in path:
            df_web=get_final_dataframe(path,0)
    df=pd.concat([df_ai,df_web])
    return df

def get_final_dataframe(path,flag):
    df=pd.DataFrame(columns=['Text','Label'])
    content=[]
    label=[]
    for file in os.listdir(path):
        if file.endswith('.pdf'):
            doc=fitz.open(path+'/'+file)
            content_temp=''
            for page in range(len(doc)):
                content_temp=content_temp+doc[page].get_text()
                print(content_temp)
            content.append(content_temp)

    df['Text']=content
    df['Label']=flag
    return df

def get_content(file_path):
    df = pd.DataFrame(columns = ['Text', 'Label'])
    df = get_content_of_pdfs(file_path)
    return df

def dataset_generate():
    file_path=get_path()
    dataset=get_content(file_path)
    dataset.to_csv('dataset.csv')

if __name__ == '__main__':
    dataset_generate()

