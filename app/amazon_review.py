import urllib.request
from bs4 import BeautifulSoup

base_url = 'https://www.amazon.co.jp/product-reviews/4478025819/ref=cm_cr_dp_d_show_all_top?ie=UTF8&reviewerType=all_reviews'
page_num = 0
f = open('amazon.csv', 'w')

while True:
	page_num += 1
	print(page_num)
	url = base_url + "&pageNumber=" + str(page_num)
	req = urllib.request.Request(url,None,{"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'})
	response = urllib.request.urlopen(req)
	soup = BeautifulSoup(response, "html.parser")
	review_list = soup.find_all("div", class_='a-section review')

	if len(review_list) != 0:
		for review in review_list:
			rate = review.find("i", attrs={'data-hook': 'review-star-rating'}).find("span").string
			body = review.find("span", attrs={'data-hook': 'review-body'}).get_text()
			body_str = body.encode('cp932', "ignore").decode('cp932')
			f.write(rate + "," + body_str[:1000] + "\n")
	else:
		break

f.close()