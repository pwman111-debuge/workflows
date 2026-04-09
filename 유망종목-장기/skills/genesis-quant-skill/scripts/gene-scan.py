import pandas as pd
import sys

def filter_genesis_stocks(csv_path):
    """
    Genesis Quant Filter Script
    - ROE > 15
    - Operating Profit Growth > 10%
    - PBR < 3 (Flexible)
    """
    try:
        df = pd.read_csv(csv_path)
        # 필수 컬럼 존재 여부 확인
        required_cols = ['Ticker', 'Name', 'ROE', 'OpProfitGrowth', 'PBR']
        if not all(col in df.columns for col in required_cols):
             print(f"Error: CSV file must contain columns: {required_cols}")
             return

        # 필터링 조건 적용
        df_filtered = df[
            (df['ROE'] >= 15) & 
            (df['OpProfitGrowth'] > 0.1) & 
            (df['PBR'] < 5)
        ]
        
        # 정렬: ROE 상위 순
        df_sorted = df_filtered.sort_values(by='ROE', ascending=False)
        
        print(f"--- Genesis Quant Screening Result (Total: {len(df_sorted)}) ---")
        print(df_sorted[['Name', 'ROE', 'OpProfitGrowth', 'PBR']].to_string(index=False))
        
    except FileNotFoundError:
        print(f"Error: File '{csv_path}' not found.")
    except Exception as e:
        print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python gene-scan.py <path_to_stock_data.csv>")
    else:
        filter_genesis_stocks(sys.argv[1])
