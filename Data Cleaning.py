import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')

#Salary parsing
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['Employer_Provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary' in x.lower() else 0)
df = df[df['Salary Estimate'] != '-1']
salary  = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
mins_kd = salary.apply(lambda x: x.replace('K' , '').replace('$' , ''))
min_hr  = mins_kd.apply(lambda x: x.lower().replace('per hour' , '').replace('employer provided salary' , ''))
df['min_salary'] = min_hr.apply(lambda x: x.split('-')[0])
df['min_salary'] = df['min_salary'].apply(lambda x : int(x.replace(':' , '')))
df['max_salary'] = min_hr.apply(lambda  x: x.split('-')[-1])
df['max_salary'] = df['max_salary'].apply(lambda x : int(x.replace(':' , '')))
df['avg_salary'] = (df.min_salary + df.max_salary)/2

#company name text only
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3] , axis=1 )

# State field
df['job_state']  = df['Location'].apply(lambda x: x.split(',')[1])
df['same state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0 ,axis=1)
# print(df.job_state.value_counts())
# print(df['job_state'])
# print(df['same state'])

#age of company
df['age'] = df.Founded.apply(lambda x: x if x<1 else 2023 - x)

#parsing job description (pthon , etc.)
print(df['Job Description'][22])

#python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
print(df.python_yn.value_counts())
# #excel
df['excel_yn'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
print(df['excel_yn'].value_counts())
# #r studio
df['r_studio_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studion' in x.lower() else 0)
print(df['r_studio_yn'].value_counts())
# #power bi
df['power_bi_yn'] = df['Job Description'].apply(lambda x: 1 if 'power bi' in x.lower() else 0)
print(df['power_bi_yn'].value_counts())
# #tabula
df['tabula_yn']  = df['Job Description'].apply(lambda x: 1 if 'tabula' in  x.lower() else 0)
print(df['tabula_yn'].value_counts())
# #matplotlib
df['matplotlib_yn'] = df['Job Description'].apply(lambda x: 1 if 'matplotlib' in x.lower() else 0)
print(df['matplotlib_yn'].value_counts())
# #math
df['math'] = df['Job Description'].apply(lambda  x: 1 if 'math' or 'mathematics' in x.lower() else 0)
print(df['math'].value_counts())
#machine learning
df['machine learning'] = df['Job Description'].apply(lambda x: 1 if 'machine learning' in x.lower() else 0 )
print(df['machine learning'].value_counts())
#communication skills
df['communication skills'] = df['Job Description'].apply(lambda x: 1 if 'communication skills' in x.lower() else 0 )
print(df['communication skills'].value_counts())


print(df.columns)
df_final = df.drop('Unnamed: 0', axis= 1)
print(df_final)
df_final.to_csv('salary_data_cleaned.csv' , index=False)