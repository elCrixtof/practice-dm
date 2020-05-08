import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

def start():

    df = read_csv()
    op = '0'
    print('> Selecciona una opción:', end=' ')
    op = input()
        
    if op == '1':
        funcion_1(df)
    elif op == '2':
        funcion_2(df)
    elif op == '3':
        funcion_3(df)
    elif op == '4':
        funcion_4(df)
    elif op == '5':
        funcion_5(df)
    elif op == '6':
        funcion_6(df)
    elif op == '7':
        funcion_7(df)
    elif op == '8':
        funcion_8(df)
    elif op == '9':
        funcion_9(df)
    elif op == '10':
        funcion_10(df)
    elif op == '11':
        funcion_11(df)
    elif op == '12':
        funcion_12(df)
    elif op == '13':
        funcion_13(df)
    elif op == '14':
        pass
    else:
        print('\n * Opción Inválida * \n')

def read_csv():
    w_d = '/Users/Crist/Documents/'
    i_f = 'survey_results_public.csv'
    df = pd.read_csv(w_d + i_f)
    return df

def remove_nan(df, column):
    df_filter = (df[column].notnull()) & (df[column] != '')
    return df_filter

def find_vals(df, column):
    filter_nan = remove_nan(df, column)
    data = df[filter_nan][column].str.split(';')
    aux = []
    for element in data:
        for e in element:
            if e not in aux:
                aux.append(e)
    return aux

def correlation(lista1, lista2):
    x = sum(lista1)/len(lista1)
    y = sum(lista2)/len(lista2)
    
    suma1 = 0
    suma2 = 0
    suma3 = 0
    
    for i in range(0, len(lista1)):
        suma1 += (lista1[i]-x)*(lista2[i]-y)
        suma2 += (lista1[i]-x)**2
        suma3 += (lista2[i]-y)**2
        
    #raiz = (suma2*suma3)**(1/2)
    suma2 = math.sqrt(suma2)
    suma3 = math.sqrt(suma3)
    raiz = suma2 * suma3
    correlacion = suma1/raiz
    
    return correlacion

def funcion_1(df):
    genders = find_vals(df, 'Gender')
    filter_nan = remove_nan(df, 'ConvertedComp')

    for gen in genders:
        filter = (filter_nan) & (df['Gender'].str.contains(gen))
        print('\n\nResumen para '+gen+': ')
        print(df[filter]['ConvertedComp'].describe()[['mean','std','min','25%','50%','75%','max']])
        df[filter].boxplot(column = 'ConvertedComp', sym='')
        plt.show()

def funcion_2(df):
    ethnicities = find_vals(df, 'Ethnicity')
    filter_nan = remove_nan(df, 'ConvertedComp')

    for ethnicity in ethnicities:
        filter = (filter_nan) & (df['Ethnicity'].str.contains(ethnicity))
        print('\n\nResumen para '+ethnicity+': ')
        print(df[filter]['ConvertedComp'].describe()[['mean','std','min','25%','50%','75%','max']])
        df[filter].boxplot(column = 'ConvertedComp')
        plt.show()
        
def funcion_3(df):
    devtypes = find_vals(df, 'DevType')
    filter_nan = remove_nan(df, 'ConvertedComp')

    for devtype in devtypes:
        filter = (filter_nan) & (df['DevType'].str.contains(devtype))
        print('\n\nResumen para '+devtype+': ')
        print(df[filter]['ConvertedComp'].describe()[['mean','std','min','25%','50%','75%','max']])
        df[filter].boxplot(column = 'ConvertedComp')
        plt.show()
        
def funcion_4(df):
    Countries = find_vals(df, 'Country')
    filter_nan = remove_nan(df, 'ConvertedComp')

    for country in Countries:
        filter = (filter_nan) & (df['Country'].str.contains(country))
        print('\nResumen para '+country+': ')
        print(df[filter]['ConvertedComp'].describe()[['50%','mean','std']])
        

def funcion_5(df):
    devtypes = find_vals(df, 'DevType')
    filter_nan = remove_nan(df, 'DevType')
    frec = []
    for devtype in devtypes:
        filter = filter_nan & df['DevType'].str.contains(devtype)
        count = 0
        for i in filter:
            if i == True:
                count += 1
        frec.append(count)
     
    print('Grafica de barras')
    plt.barh(devtypes, frec)
    plt.show()

# def funcion_6(df):
#     filter_nan = remove_nan(df, 'YearsCode')
#     genders = find_vals(df, 'Gender')
#     for gen in genders:
#         print('Género: ' +  gen)
#         filter = (filter_nan) & (df['Gender'].str.contains(gen))
#         data = df[filter]['YearsCode'].tolist()
#         data2 = []
#         for l in range(len(data)):
#             if not (data[l] == 'Less than 1 year' or data[l] == 'More than 50 years'):
#                 data2.append(int(data[l]))
#         data2.sort()
#         plt.hist(data2, bins=10)
#         plt.show()

def funcion_6(df):
    print('Plot histograms with 10 bins for the years of experience with coding per gender')
    filter_nan = remove_nan(df, 'YearsCode')
    genders = find_vals(df, 'Gender')
    filter_2 = (filter_nan) & ( df['YearsCode'] != 'Less than 1 year' ) & ( df['YearsCode'] != 'More than 50 years' )
    for gen in genders:
        print('Género: ' +  gen)
        filter = (filter_2) & (df['Gender'].str.contains(gen))
        df[filter]['YearsCode'].apply(pd.to_numeric).sort_values().hist(bins=10, xrot=90)
        plt.show()

def funcion_7(df):
    filter_nan = remove_nan(df, 'WorkWeekHrs')
    devtypes = find_vals(df, 'DevType')
    # wwh = find_vals(df, 'WorkWeekHrs')
    # print(wwh)
    # count = 0
    for devtype in devtypes:
        print('Tipo de programador: ' +  devtype)
        filter = (filter_nan) & (df['DevType'].str.contains(devtype))
        data = df[filter]['WorkWeekHrs'].tolist()
        aux = []
        for d in data:
            if d <= 98:
                aux.append(d)
        aux.sort()
        plt.hist(aux, bins=10)
        plt.show()
        # plt.clf()
        # plt.savefig('7_'+str(count))
        # count = count + 1

def funcion_8(df):
    filter_nan = remove_nan(df, 'Age')
    genders = find_vals(df, 'Gender')
    # wwh = find_vals(df, 'Age')
    # print(wwh)
    # count = 0
    for gender in genders:
        print('Edad por genero: ' +  gender)
        filter = (filter_nan) & (df['Gender'].str.contains(gender))
        data = df[filter]['Age'].tolist()
        data.sort()
        plt.hist(data, bins=10)
        plt.show()
        # plt.savefig(str(count))
        # plt.clf()
        # count = count + 1

def funcion_9(df):
    languages = find_vals(df, 'LanguageWorkedWith')
    filter_nan = remove_nan(df, 'Age')

    languages[languages.index('C++')] = 'C\+\+'
    languages[languages.index('Other(s):')] = 'Other'

    for language in languages:
        filter = (filter_nan) & (df['LanguageWorkedWith'].str.contains(language))
        print('\n\nResumen para '+language+': ')
        print(df[filter]['Age'].describe()[['50%','mean','std']])

    
def funcion_10(df):
    print('Correlacion entre años de experiencia y salario anual')
    filter_nan = remove_nan(df, 'ConvertedComp')
    filter_nan2 = remove_nan(df, 'YearsCode')
    filter = (filter_nan) & (filter_nan2)
    filter_3 = (filter) & ( df['YearsCode'] != 'Less than 1 year' ) & ( df['YearsCode'] != 'More than 50 years' )
    data1 = df[filter_3]['YearsCode'].tolist()
    data2 = df[filter_3]['ConvertedComp'].tolist()
    x = []
    y = []
    for d1 in range(len(data1)):
        x.append(int(data1[d1]))
    for d2 in range(len(data2)):
        y.append(int(data2[d2]))
    print('La correlacion', correlation(x,y))
    

def funcion_11(df):
    print('Correlacion entre la edad y salario anual')
    filter_nan = remove_nan(df, 'ConvertedComp')
    filter_nan2 = remove_nan(df, 'Age')
    filter = (filter_nan) & (filter_nan2)
    data1 = df[filter]['Age'].tolist()
    data2 = df[filter]['ConvertedComp'].tolist()
    x = []
    y = []
    for d1 in range(len(data1)):
        x.append(int(data1[d1]))
    for d2 in range(len(data2)):
        y.append(int(data2[d2]))
    print('La correlacion', correlation(x,y))

def funcion_12(df):
    d = {'I never completed any formal education': 0, 'Primary/elementary school': 1, 'Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)': 2,  'Some college/university study without earning a degree': 3, 'Bachelor’s degree (BA, BS, B.Eng., etc.)': 4, 'Professional degree (JD, MD, etc.)': 5, 'Master’s degree (MA, MS, M.Eng., MBA, etc.)': 6, 'Other doctoral degree (Ph.D, Ed.D., etc.)': 7, 'Associate degree':8}
    filter_nan = remove_nan(df, 'EdLevel')
    filter_nan2 = remove_nan(df, 'ConvertedComp')
    filter = (filter_nan) & (filter_nan2)
    ed_level =  df[filter]['EdLevel'].tolist()
    salary = df[filter]['ConvertedComp'].tolist()

    for l in range(len(ed_level)):
        ed_level[l] = d[ed_level[l]]
    
    print(correlation(ed_level, salary))

def funcion_13(df):
    languages = find_vals(df, 'LanguageWorkedWith')
    languages[languages.index('C++')] = 'C\+\+'
    languages[languages.index('Other(s):')] = 'Other'
    print(languages)
    # languages = ['HTML/CSS', 'Java', 'JavaScript', 'Python', 'C++', 'C', 'C#', 'SQL', 'VBA', 'R', 'Bash/Shell/PowerShell', 'Ruby', 'Rust', 'TypeScript', 'WebAssembly', 'Other(s):', 'Go', 'PHP', 'Assembly', 'Kotlin', 'Swift', 'Objective-C', 'Elixir', 'Erlang', 'Clojure', 'F#', 'Scala', 'Dart']

    filter_nan = remove_nan(df, 'LanguageWorkedWith')
    frec = []
    for language in languages:
        if languages == 'C\+\+':
            filter = filter_nan & df['LanguageWorkedWith'].str.contains('C++')
        if language == 'Other':
            filter = filter_nan & df['LanguageWorkedWith'].str.contains('Other(s):')

        filter = filter_nan & df['LanguageWorkedWith'].str.contains(language)
        count = 0
        for i in filter:
            if i == True:
                count += 1
        frec.append(count)
     
    print('Grafica de barras')
    plt.barh(languages, frec)
    plt.show()

start()