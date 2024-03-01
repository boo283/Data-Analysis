import pandas as pd

def split_engine_to_new_df(engine):
    """
    Hàm nhận đầu vào là một kiểu series

    Tham số:
    Cột enginetype

    Trả về:
    một dataframe chứa 2 (Cylinder_type, Engine_type) cột được phân tách từ cột enginetype ban đầu
    """
    engine = engine.str.replace('4 stroke', '').str.replace('4-Takt', '').str.replace('4-stroke', '').str.replace('2-stroke', '').str.replace('2 stroke', '')
    engine = engine.str.replace('lengthways','')
    engine = engine.str.replace('4 stroke', '').str.replace('4-Takt', '').str.replace('4-stroke', '')
    engine = engine.str.replace('|','')
    s = (engine.str.split())

    for index, value in enumerate(s):
        if len(value) == 2:
            continue
        else:
            if len(value) == 1:
                if value in [['Twin'],['V'],['Straight'],['Boxer']]:
                    value.append('Not provided')
                else:
                    value.insert(0,'Not provided')
            else:
                value.append('Not provided')
                value.append('Not provided')

    for value in s:
        if value[0] == 'V':
            value[0] = 'Straight'
    
    dfs = pd.DataFrame(s.tolist(),columns=['Cylinder-type','Engine-type'])
    return dfs


def extract_Power(pw):
    """
    Hàm trích xuất giá trị đầu tiên (đơn vị: hp) trong cột power
    Input: Series
    Return: List
    """
    pw = pw.str.split()
    new_pw = []
    for value in pw:
        if value == ['Not', 'provided']:
            value = "Not provided"
        else:
            new_value = value[0].split('/')
            value = new_value[1]
        new_pw.append(value)
    return new_pw

def convert_mls_to_km(value):
    """
    Hàm chuyển đổi đơn vị của biến Mileage về cùng đơn vị là km
    Not provided => None
    Cách dùng: dùng df['col_name'].apply(conver_mls_to_km)
    """
    value = value.replace(',','')
    if 'km' in value:
        value = value.replace('km','')
        return int(value)
    elif 'mls' in value:
        value = value.replace('mls','')
        value = int(value)
        value = float(value)
        return value * 1.60934
    else: return None

def is_numeric(value):
    """
    Hàm kiểm tra cột ( biến ) có thể đưa về dạng float hay không
    Input: Series
    Output: True nếu có thể chuyển về Float / ngược lại trả về False
    """
    try:
        float(value)
        return True
    except ValueError:
        return False