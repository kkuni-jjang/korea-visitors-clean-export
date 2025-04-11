# 국적별 관광데이터를 개별 엑셀 파일로 저장하기
# [국적별 관광객 데이터] 스위스.xlsx

# total.xlsx 파일 읽어내기
cn = pd.read_excel('./files/kto_total.xlsx')

# 국가 리스트 : cntry_list
cntry_list = list(cn['국적'].unique())

# 개별 파일로 저장
df = pd.DataFrame()

for cntry in cntry_list:
   
    # 국적으로 필터링
    df = cn[cn['국적'] == cntry]
       
    # 정해 놓은 파일명으로 저장
    df.to_excel('./homework/[국적별 관광객 데이터]{}.xlsx'.format(cntry), index=False)