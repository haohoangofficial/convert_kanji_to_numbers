import pandas as pd
def convert_kanji_to_numbers(kanji='1,155,993,391円'):

    if pd.isna(kanji):
        return None
    kanji = kanji.strip(',').strip()
    UNITS = {
        '円': 1,
        '十': 10,
        '百': 100,
        '千': 1000
    }

    MULTIPLES = {
        '万': 10000,
        '億': 100000000,
        '兆': 1000000000000
    }

    digit = ''
    total = []
    unit = 1
    multiple = 1
    # unimul = 0
    for kan in kanji:
        if kan.isdigit() or kan == '.':
            digit += str(kan)
        elif kan == '円':
            if digit != "":
                total.append(float(digit))
            break
        else:
            if kan in UNITS.keys() or kan in MULTIPLES.keys():
                if kan in UNITS.keys():
                    unit *= UNITS[kan]
                elif kan in MULTIPLES.keys():
                    multiple *= MULTIPLES[kan]
                    total.append(float(digit or 1) * unit * multiple)
                    multiple = 1
                    digit = ''
    if total is not None:
        return float(sum(total))
if __name__ =='__main__':

    df = pd.read_csv('200urls.csv')
    
    capital = df['資本金 (Capital)']
    df['資本金 (Capital) Check'] = (df['資本金 (Capital)']).apply(convert_kanji_to_numbers)
    df['売上高 (Sales) Check'] = (df['売上高 (Sales)']).apply(convert_kanji_to_numbers)
    print(df['資本金 (Capital) Check'])
    df.to_csv('200urls.csv')
    # print(convert_kanji_to_numbers('売上高 (Sales)'))