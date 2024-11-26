import pandas as pd

def load_file(file_path, has_last_value=False):
    data = {}
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) < (4 if has_last_value else 6):
                continue
            query_id = parts[0]
            doc_id = parts[2]
            score = float(parts[4]) if not has_last_value else int(parts[3])
            key = (query_id, doc_id)
            data[key] = score
    return data   

def merge_with_fourth_to_excel(file_paths, fourth_file, output_excel, is_train):

    datasets = [load_file(file_path) for file_path in file_paths]

    common_keys = set(datasets[0].keys())
    for data in datasets[1:]:
        common_keys.intersection_update(data.keys())
    
    if is_train:
        fourth_data = load_file(fourth_file, has_last_value=True)
        #print(fourth_data)
        common_keys.intersection_update(fourth_data.keys())

    #print(common_keys)
    rows = []
    
    if is_train:
        for key in common_keys:
            query_id, doc_id = key
            scores = [data[key] for data in datasets]
            last_value = fourth_data[key]
            rows.append([query_id, doc_id, *scores, last_value])
        df = pd.DataFrame(rows, columns=['Query ID', 'Doc ID', 'Score 1', 'Score 2', 'Score 3', 'Last Value'])
        df.to_excel(output_excel, index=False)

    else:
        for key in common_keys:
            query_id, doc_id = key
            scores = [data[key] for data in datasets]
            rows.append([query_id, doc_id, *scores])
        df = pd.DataFrame(rows, columns=['Query ID', 'Doc ID', 'Score 1', 'Score 2', 'Score 3'])
        df.to_excel(output_excel, index=False)

    print(f"Final merged data saved to {output_excel}")


fourth_file = '../../data/qrels.401_440.txt'
file_paths = ['../result/bm25_stemming_40.run', '../result/lmLaplace_stemming_40.run', '../result/lmJelinekMercer_stemming_40.run']
output_excel = 'new_train_partial.xlsx'
merge_with_fourth_to_excel(file_paths, fourth_file, output_excel, True)


fourth_file = '../../data/qrels.401_440.txt'
file_paths = ['../result/bm25_stemming_40_full.run', '../result/lmLaplace_stemming_40_full.run', '../result/lmJelinekMercer_stemming_40_full.run']
output_excel = 'new_train_full.xlsx'
merge_with_fourth_to_excel(file_paths, fourth_file, output_excel, True)

file_paths = ['../result/bm25_stemming_10.run', '../result/lmLaplace_stemming_10.run', '../result/lmJelinekMercer_stemming_10.run']
output_excel = 'new_test.xlsx'
merge_with_fourth_to_excel(file_paths, fourth_file, output_excel, False)