import requests

# response = requests.get('http://www.jiuzhang.com')
# print(type(response))
# print(response.status_code)
# print(response.encoding)
# print(response.text)

#no space for = in the function!!!! code style!!!!!

response1 = requests.get('http://www.jiuzhang.com/article/?tag=guidance')
print(type(response1))
print(response1.status_code)

paras = {'tag':'guidance'}
response2 = requests.get('http://www.jiuzhang.com/article/',params=paras)
print(type(response2))

print(response1.text==response2.text)
