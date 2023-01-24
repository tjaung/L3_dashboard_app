import boto3
import s3fs
import fastparquet as fp
import os
import pickle as pkl
import pandas as pd
import numpy as np
from pprint import pprint


def list_s3_subdirectories(prefix):
    s3client = boto3.client("s3")
    bucket='emr-cohere-data-management'

    result = s3client.list_objects(Bucket=bucket, Prefix=prefix, Delimiter='/')
    
    if result.get("CommonPrefixes") == None:
        return None
    
    dirs = []
    for o in result.get('CommonPrefixes'):
        # print('sub folder : ', o.get('Prefix'))
        dirs.append(o.get("Prefix"))
    return(dirs)

def list_s3_files_in_folder_using_client(path):
    """
    This function will list down all files in a folder from S3 bucket
    :return: None
    """
    s3client = boto3.client("s3")
    bucket='emr-cohere-data-management'
    response = s3client.list_objects(Bucket=bucket, Prefix=path)
    files = response.get("Contents")
    if len(files) > 1:
        print("Multiple Files Found: \n")
        for i, file in enumerate(files):
            print(f"[{i}] file_name: {file}, size: {file['Size']}")
            
        print("\nPlease Select Desired File Index: ")
        # model = int(input())
        # print(model)
        # return files[model]['Key']
    else:
       # print(files[0]['Key'])
        return files[0]['Key']

def get_model_name(params):
    if params['modality'] != None:
        mpath = f"signal_based_models/{params['service']}/by_PAL/{params['pal']}/{params['modality']}/{params['version']}/model/"
    else:
        mpath = f"signal_based_models/{params['service']}/by_PAL/{params['pal']}/{params['version']}/model/"
        
    path_model = list_s3_files_in_folder_using_client(mpath)
    model_name = path_model.replace(mpath, '')
    
    return {"s3_path": path_model,
            "name": model_name,
           "mpath": mpath}

def get_model(params):
    # get model info
    path_model = get_model_name(params)["s3_path"]
    mpath = get_model_name(params)["mpath"]
    
    s3client = boto3.client("s3")
    bucket='emr-cohere-data-management'
    response = s3client.get_object(Bucket=bucket, 
                               Key=path_model)

    body = response['Body'].read()
    model = pkl.loads(body)
    model.classes_ = np.array([0,1])
    
    return model

def get_model_params_from_s3_buckets(service, pal):
    # get modality if applicable
    modality = os.path.basename(os.path.normpath(list_s3_subdirectories(f'signal_based_models/{service}/by_PAL/{pal}/')[0])) if service=='cardio' else None
    # modality check
    if modality not in ["CTA", "PET", "DME", "MRI", "ABLATION", "EPS", "CCTA", "INTERVENTIONS", "ECHO", "MRA", "CT", "CATH", "PCI", "MPI-SPECT"]:
        modality = None

    # pull latest version
    v_path = list_s3_subdirectories(f'signal_based_models/{service}/by_PAL/{pal}/{modality}/') if modality != None else list_s3_subdirectories(f'signal_based_models/{service}/by_PAL/{pal}/')

    # check if version folder is empty
    v = None
    if len(v_path) > 1 and v_path != None:
        for i in reversed(range(0, len(v_path))):
            if list_s3_subdirectories(v_path[i]) != None:
                v = os.path.basename(os.path.normpath(v_path[i]))
                break
    else:
        v = os.path.basename(os.path.normpath(v_path[0]))
    
    # build base path
    path = f'signal_based_models/{service}/by_PAL/{pal}/{v}/' if modality == None else f'signal_based_models/{service}/by_PAL/{pal}/{modality}/{v}/'
    
    return {'service': service,
            'pal': pal,
            'modality': modality,
            'version': v,
            'path': path}

def load_data(params):
  
    s3 = s3fs.S3FileSystem()
    fs = s3fs.core.S3FileSystem()

    #mybucket/data_folder/serial_number=1/cur_date=20-12-2012/abcdsd0324324.snappy.parquet 
    if params['modality'] == None:
        test_X_path = f"s3://emr-cohere-data-management/signal_based_models/{params['service']}/by_PAL/{params['pal']}/{params['version']}/test_data/X/*.parquet"
        test_y_path = f"s3://emr-cohere-data-management/signal_based_models/{params['service']}/by_PAL/{params['pal']}/{params['version']}/test_data/identifiers_and_y/*.parquet"
    else:
        test_X_path = f"s3://emr-cohere-data-management/signal_based_models/{params['service']}/by_PAL/{params['pal']}/{params['modality']}/{params['version']}/test_data/X/*.parquet"
        test_y_path = f"s3://emr-cohere-data-management/signal_based_models/{params['service']}/by_PAL/{params['pal']}/{params['modality']}/{params['version']}/test_data/identifiers_and_y/*.parquet"
    
    d_paths = [test_X_path, test_y_path]

    test_X = pd.DataFrame()
    test_y = pd.DataFrame()

    for path in d_paths:
        all_paths_from_s3 = fs.glob(path=path)
        myopen = s3.open
        fp_obj = fp.ParquetFile(all_paths_from_s3, open_with=myopen)

        #convert to pandas dataframe
        if test_X.empty and test_y.empty:
            test_X = fp_obj.to_pandas()
        elif not test_X.empty and test_y.empty:
            test_y = fp_obj.to_pandas()

    return {'X': test_X,
            'y': test_y}

def recode_binary(col, first_class = 'Pend'):
        if col == first_class:
            return 1
        else:
            return 0

def load_cleaned_train_test(params, model):
    d = load_data(params)
    #print('X length: ', len(d['X']), '\ny Length: ', len(d['y']))
    # get col names
    identifier_cols = ["auth_id", 
            "patient_id",
            "provider_npi",
            "auth_betos",
            "auth_pal",
            "auth_date",
            "auth_status",
            "auth_service_type",
            'auth_primaryprocedurecode_code']
    index_col = "auth_id"
    y_cols=['auth_status']
    X_cols= list(model.feature_names_in_)
    
    # split data and recode
    #X_train = train.loc[:, train.columns.isin(X_cols)]
    X_test = d['X'][X_cols]
    y_test = d['y'][y_cols]
    
    # df len test
    if len(X_test) == len(y_test):
        # add auth id as index col
        for df in [X_test, y_test]:
            df['auth_id'] = d['y'][index_col]
            df.set_index(['auth_id'], inplace=True)
    else:
        print('Length Mismatch: ')
        print('X length: ', len(X_test), '\ny Length: ', len(y_test))

    # features to binary
    bool_cols = list(X_test.select_dtypes(include='bool')) + list(X_test.select_dtypes(include='object'))
    X_test[bool_cols] = X_test[bool_cols].astype('int')
            
    y_test['auth_status'] = y_test['auth_status'].apply(recode_binary)

    return {'X_test': X_test,  
            'y_test': y_test
    }

        



