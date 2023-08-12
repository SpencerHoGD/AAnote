import requests
import json


def get_html_json_data(keyword, page):
    url = 'https://tuchong.com/rest/3/search/posts'
    params = {
                "query": keyword,
                "count": 20,
                "page": page
             }

    headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}
    response = requests.get(url, params=params, headers=headers)

    return response.content


print(get_html_json_data('猫', 1))
# json_data = get_html_json_data('猫', 1)
# with open('miao.txt', 'wb') as f:
#     f.write(json_data)
#     print('done')

# for each_images in json_data['data']['post_list']:
#     for each_image in each_images['title_image']:
#         url = each_image[:-1]
#         print(url)
#         # print(each_image)
#     # print('*' * 100)

