a = '''keyword location ad_group campaign medium landing_page channel ad_content cost
None AT Discounts EasterSpecial referral Undefined Facebook None 4.96
None AT Discounts SignUpBonus referral Undefined Facebook None 0.14
None AT Group1 EasterSpecial organic Undefined Google None 3.56
None AT Group1 Launch cpc Undefined Instagram footer-ad 5.98'''



keys = a.split('\n')[0].split(' ')
print('keys: ', keys)

json_rec = []

for i in range( 1, len(a.split('\n')) ):
    values = a.split('\n')[i].split('	')
    r_dict = dict(zip(keys, values))
    json_rec.append(r_dict)

print(json_rec)