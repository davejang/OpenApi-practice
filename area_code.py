def define_area_city(area):
  code = 0
  if(area == '서울특별시' or area == '서울'):
    code = 11000
    return code
  elif(area == '부산광역시' or area == '부산'):
    code = 26000
    return code
  elif(area == '대구광역시' or area == '대구'):
    code = 27000
    return code 
  elif(area == '인천광역시' or are a == '인천'):
    code = 28000
    return code   
  elif(area == '광주광역시' or area == '광주'):
    code = 29000
    return code
  elif(area == '대전광역시' or area == '대전'):
    code = 30000
    return code
  elif(area == '울산광역시' or area == '울산'):
    code = 31000
    return code
  elif(area == '세종세종특별자치시' or area == '세종'):
    code = 36110
    return code

def define_area_province(area):
  code = 0
  if(area == '경기도' or area == '경기'):
    code = 41000
    return code
  elif(area == '강원도' or area == '강원'):
    code = 42000
    return code
  elif(area == '충청북도' or area == '충북'):
    code = 43000
    return code
  elif(area == '충청남도' or area == '충남'):
    code = 44000
    return code
  elif(area == '전라북도' or area == '전북'):
    code = 45000
    return code
  elif(area == '전라남도' or area == '전남'):
    code = 46000
    return code
  elif(area == '경상북도' or area == '경북'):
    code = 47000
    return code
  elif(area == '경상남도' or area == '경남'):
    code = 48000
    return code
  elif(area == '제주도' or area == '제주'):
    code = 50000
    return code