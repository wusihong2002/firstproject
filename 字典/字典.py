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


#根据当前速度确定将外星人向右移动多远
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

#还可以通过key()确定某人是否接受了调查
#favorite_languages = {
#    'jen':'python',
#    'tom':'c',
#    'sarah':'ruby',
#    'phil':'python',
#    }
#if 'erin' not in favorite_languages.keys():
#    print("Erin please take our poll")

#按特定顺序遍历字典中的所有键
#favorite_languages = {
#    'jen':'python',
#    'tom':'c',
#    'sarah':'ruby',
#    'phil':'python',
#    }
#for name in sorted(favorite_languages.keys()):
#    print(f"{name.title()},think you for taking the poll")
#遍历字典中所有值
#favorite_languages = {
#    'jen':'python',
#    'tom':'c',
#    'sarah':'ruby',
#    'phil':'python',
#    }
#print("the following languages have been mentioned")
#for languages in favorite_languages.values():
#    print(languages.title())
#这种做法没有考虑是否重复，为剔除重复项，可使用集合(set),集合中每个元素都必须是独一无二的
#favorite_languages = {
#    'jen':'python',
#    'tom':'c',
#    'sarah':'ruby',
#    'phil':'python',
#    }
#print("the following languages have been mentioned")
#for languages in set(favorite_languages.values()):
#    print(languages.title())
##可用一对花括号直接创建集合，并在其中用逗号分隔元素
#languages = {'python','c','ruby','python'}
##{'python','c','ruby''}
##集合和字典很容易混淆，当花括号中没有键值对时定义的可能是集合。不同于列表和字典，集合不会以特定的顺序存储元素

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