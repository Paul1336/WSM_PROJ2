import pandas as pd

input_file = './predictions_full_weighted.xlsx'
output_file = '../result/logistic_regression_full_weight_10.run'

predictions_df = pd.read_excel(input_file)

predictions_df['Q0'] = 'Q0'
predictions_df['Rank'] = 10
predictions_df['Method'] = 'ml'

formatted_df = predictions_df[['Query ID', 'Q0', 'Doc ID', 'Rank', 'Predictions', 'Method']]
formatted_df.rename(columns={'Predictions': 'Score'}, inplace=True)
formatted_df_sorted = formatted_df.sort_values(by=['Query ID', 'Score'], ascending=[True, False])
formatted_df_sorted.to_csv(output_file, sep=' ', index=False, header=False)

print(f"save to: {output_file}")

input_file = './predictions_full.xlsx'
output_file = '../result/logistic_regression_full_10.run'

predictions_df = pd.read_excel(input_file)

predictions_df['Q0'] = 'Q0'
predictions_df['Rank'] = 10
predictions_df['Method'] = 'ml'

formatted_df = predictions_df[['Query ID', 'Q0', 'Doc ID', 'Rank', 'Predictions', 'Method']]
formatted_df.rename(columns={'Predictions': 'Score'}, inplace=True)
formatted_df_sorted = formatted_df.sort_values(by=['Query ID', 'Score'], ascending=[True, False])
formatted_df_sorted.to_csv(output_file, sep=' ', index=False, header=False)

print(f"save to: {output_file}")

input_file = './predictions_partial_weighted.xlsx'
output_file = '../result/logistic_regression_partial_weight_10.run'

predictions_df = pd.read_excel(input_file)

predictions_df['Q0'] = 'Q0'
predictions_df['Rank'] = 10
predictions_df['Method'] = 'ml'

formatted_df = predictions_df[['Query ID', 'Q0', 'Doc ID', 'Rank', 'Predictions', 'Method']]
formatted_df.rename(columns={'Predictions': 'Score'}, inplace=True)
formatted_df_sorted = formatted_df.sort_values(by=['Query ID', 'Score'], ascending=[True, False])
formatted_df_sorted.to_csv(output_file, sep=' ', index=False, header=False)

print(f"save to: {output_file}")

input_file = './predictions_partial.xlsx'
output_file = '../result/logistic_regression_partial_10.run'

predictions_df = pd.read_excel(input_file)

predictions_df['Q0'] = 'Q0'
predictions_df['Rank'] = 10
predictions_df['Method'] = 'ml'

formatted_df = predictions_df[['Query ID', 'Q0', 'Doc ID', 'Rank', 'Predictions', 'Method']]
formatted_df.rename(columns={'Predictions': 'Score'}, inplace=True)
formatted_df_sorted = formatted_df.sort_values(by=['Query ID', 'Score'], ascending=[True, False])
formatted_df_sorted.to_csv(output_file, sep=' ', index=False, header=False)

print(f"save to: {output_file}")