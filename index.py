from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = Edge()  # 使用Edge的WebDriver
driver.get("https://kktix.com/users/sign_in?back_to=https%3A%2F%2Fkktix.com%2F") # 網址導向KKTIX登入畫面(以KKTIX為例)

wait = WebDriverWait(driver, 5)  #設置等待時間為5秒

element = wait.until(EC.visibility_of_element_located((By.ID, "user_login")))
element.send_keys("輸入帳號")#輸入帳號
element = wait.until(EC.visibility_of_element_located((By.ID, "user_password")))
element.send_keys("輸入密碼")#輸入密碼

button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-login")))
button.click()#點擊登入

### Check Index(檢查哪一個是我要的)
buttons = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "type-view")))
for index, button in enumerate(buttons):
    print(f"Index: {index}, Button: {button.text}")
###
buttons = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "type-view")))
button = buttons[3]#使用索引值來選擇要點擊的元素
button.click()

### Check Index(檢查哪一個是我要的)
buttons = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "btn-point")))
for index, button in enumerate(buttons):
    print(f"Index: {index}, Button: {button.text}")
###
buttons = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "btn-point")))
button = buttons[0]#使用索引值來選擇要點擊的元素
button.click()

# 部分匹配的 CSS 類選擇器
class_selector = "[class*='ng-pristine']"

# 使用 CSS 選擇器定位元素
elements = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, class_selector)))

### Check Index(檢查哪一個是我要的)
for index, element in enumerate(elements):
    print(f"Index: {index}, Element: {element.text}")
###

# 選擇目標元素（假設要選擇第4個元素）
target_element = elements[4]

# 清除現有的值
target_element.clear()

# 輸入票券數
target_element.send_keys("1")

###打勾我同意
if 0 <= 5 < len(elements):
    target_element = elements[5]
    target_element.click()
else:
    print("Index is out of range.")
###

# 使用 CSS 選擇器定位按鈕元素
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary.btn-lg.ng-isolate-scope")))

# 點擊下一步
button.click()

###以此類推後續輸入其他隱私資料(信用卡資料...等)暫時不放上來###

while True:
    pass  # 添加無限循環，保持程序運行狀態