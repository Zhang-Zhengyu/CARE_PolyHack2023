from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.37",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
]

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.baidu.com")


options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={random.choice(user_agents)}")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=options)

# # 创建Chrome浏览器对象
# driver = webdriver.Chrome()

# 打开知乎问题页面
# driver.get("https://www.zhihu.com/question/32313367/answers/updated")
driver.get("https://www.zhihu.com/question/32313367")

# 等待页面加载
time.sleep(1)
print('已等待1秒')

# 关闭登录弹窗
close_login = driver.find_element(By.XPATH,'//button[@class="Button Modal-closeButton Button--plain"]')
close_login.click()
print('已关闭弹窗')

# 模拟向下滚动
body = driver.find_element(by=By.TAG_NAME, value="body")
times = 6
print(f'本次运行将下滑[{times}]次')
for i in range(times):
    body.send_keys(Keys.PAGE_DOWN)
    body.send_keys(Keys.PAGE_DOWN)
    print(f'\r已下划[{str(i)}]次', end='', flush=True)
    time.sleep(1)
print()

# 找到问题标题元素
ans_element = driver.find_elements(by=By.XPATH, value='//div[@role="list"] //div[@class="List-item"]')
order=0

print('order,user_name,date_time,count_comments,count_likes,url,post_content,comments')
for title in ans_element:
    # the order of post
    order += 1
    print(order, end=',')

    # the nickname of user
    print(title.find_element(by=By.XPATH, value='.//meta[@itemprop="name"]').get_attribute('content'), end=',')

    # the date-time created
    print(title.find_element(by=By.XPATH, value='.//meta[@itemprop="dateCreated"]').get_attribute('content'), end=',')

    # number of comments
    commentCount = title.find_element(by=By.XPATH, value='.//meta[@itemprop="commentCount"]').get_attribute('content')
    print(commentCount,end=',')

    # number of likes(upvote count)
    print(title.find_element(by=By.XPATH, value='.//meta[@itemprop="upvoteCount"]').get_attribute('content'), end=',')

    # url
    print(title.find_element(by=By.XPATH, value='.//div[@class="ContentItem-time"] //a[@target="_blank"]').get_attribute('href'), end=',')

    # post content
    print(title.find_element(by=By.XPATH, value='.//div[@class="RichContent-inner"]').get_attribute('innerHTML'), end='\n')
    # print(title.find_element(by=By.XPATH, value='.//div[@class="RichContent-inner"]')., end='\n')

    if int(commentCount) > 0:
        # 找到展开评论
        # open_comment = title.find_elements(by=By.XPATH, value='.//button[contains(text(), "评论")]')
        # print(open_comment)
        # # open_comment.click()
        # print('展开评论')
        try:
            element = title.find_element(by=By.XPATH, value='.//button[contains(text(), "评论")]')
            driver.execute_script("arguments[0].scrollIntoView();", element)
            element.click()
            time.sleep(5)
        except:
            print(f'找不到元素')
    while True:
        pass
time.sleep(30)
# 关闭浏览器
driver.quit()
print('已关闭浏览器')
