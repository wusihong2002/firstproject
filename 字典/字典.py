#aline_0 = {'color':'green','points':'5'}
#print(aline_0['color'])
#print(aline_0['points'])
#new_points = aline_0['points']
#print(f"you just earned {new_points} points!")
#print(aline_0)
#aline_0['x_position'] = 0
#aline_0['y_position'] = 25
#print(aline_0)

#aline_0 = {}
#aline_0['color'] = 'green'
#aline_0['points'] = 5
#print(aline_0)

#aline_0 = {'color':'green'}
#print(f"the aline is {aline_0['color']}.")
#aline_0['color'] = 'yellow'
#print(f"the aline is {aline_0['color']}.")


#���ݵ�ǰ�ٶ�ȷ���������������ƶ���Զ
#aline_0 = {'x_position':0,'y_position':25,'speed':'medium'}
#print(f"Original x_position:{aline_0['x_position']}")
#aline_0['speed'] = 's'
#if aline_0['speed'] == 'slow':
#    x_increment = 1
#elif aline_0['speed'] == 'medium':
#    x_increment = 2
#else:
#    x_increment = 3
#aline_0['x_position'] = aline_0['x_position'] + x_increment
#print(f"new x_position:{aline_0['x_position']}")

#aline_0 = {'color':'green','points':'5'}
#del aline_0['points']
#print(aline_0)

#favorite_languages = {
#    'jen':'python',
#    'tom':'c',
#    'sarah':'ruby',
#    'phil':'python',
#    }
#languages = favorite_languages['sarah'].title()
#print(f"Sarah favorite languages is {languages}")

#aline_0 = {'color':'green','speed':'slow'}
#point_value = aline_0.get('points','no point value assigned.')
#print(point_value)

#person = {'first_name':'zhang','last_name':'san','age':18,'city':'beijin'}
#print(person)

#num = {'tom':12,'zhang':23,'li':4,'wang':5,'zhao':6}
#print(f"{num['li']}  {num['tom']}")

#uses_0 = {
#    'username':'efermi',
#    'first':'enrico',
#    'last':'fermi',
#    }
#for key,value in uses_0.items():
#    print(f"\nkey: {key}")
#    print(f"value: {value}")

#favorite_languages = {
#    'jen':'python',
#    'tom':'c',
#    'sarah':'ruby',
#    'phil':'python',
#    }
#friends = ['jen','tom']
#for name in favorite_languages.keys():
#    print(f"hi {name.title()}")
#    if name in friends:
#        languages = favorite_languages[name].title()
#        print(f"\t{name.title()}, i see you love {languages.title()}")

#������ͨ��key()ȷ��ĳ���Ƿ�����˵���
#favorite_languages = {
#    'jen':'python',
#    'tom':'c',
#    'sarah':'ruby',
#    'phil':'python',
#    }
#if 'erin' not in favorite_languages.keys():
#    print("Erin please take our poll")

#���ض�˳������ֵ��е����м�
#favorite_languages = {
#    'jen':'python',
#    'tom':'c',
#    'sarah':'ruby',
#    'phil':'python',
#    }
#for name in sorted(favorite_languages.keys()):
#    print(f"{name.title()},think you for taking the poll")
#�����ֵ�������ֵ
#favorite_languages = {
#    'jen':'python',
#    'tom':'c',
#    'sarah':'ruby',
#    'phil':'python',
#    }
#print("the following languages have been mentioned")
#for languages in favorite_languages.values():
#    print(languages.title())
#��������û�п����Ƿ��ظ���Ϊ�޳��ظ����ʹ�ü���(set),������ÿ��Ԫ�ض������Ƕ�һ�޶���
#favorite_languages = {
#    'jen':'python',
#    'tom':'c',
#    'sarah':'ruby',
#    'phil':'python',
#    }
#print("the following languages have been mentioned")
#for languages in set(favorite_languages.values()):
#    print(languages.title())
##����һ�Ի�����ֱ�Ӵ������ϣ����������ö��ŷָ�Ԫ��
#languages = {'python','c','ruby','python'}
##{'python','c','ruby''}
##���Ϻ��ֵ�����׻���������������û�м�ֵ��ʱ����Ŀ����Ǽ��ϡ���ͬ���б���ֵ䣬���ϲ������ض���˳��洢Ԫ��

#hes = {'nile':'egypt','wenlan':'lingao','wangquan':'haikou'}
#for key,value in hes.items():
#    print(f"the {key.title()} run through {value.title()}")


#favorite_languages = {
#    'jen':'python',
#    'tom':'c',
#    'sarah':'ruby',
#    'phil':'python',
#    }
#person = {'jen','tom','jei','sd'}
#for fa in person:
#    if fa in favorite_languages:
#        print(f"think {fa.title()}")
#    else:
#        print(f"poll {fa.title()}")