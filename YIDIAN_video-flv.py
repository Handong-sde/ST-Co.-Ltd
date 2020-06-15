from selenium import webdriver
import pyperclip
import time,os
import random
import pyautogui
# 导入selenium中的actionchains的方法
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
#打开txt文件夹
def dirfiles(file_dir):
        for root, dirs, files in os.walk(file_dir, 1):
            return files

def list_dir(file_dir):
    for root, dirs, files in os.walk(file_dir, 1):
        return dirs
#人工输入每次几个图片
pyautogui.FAILSAFE = False#autogui 不能fail safety
num_of_video = input("how many video a time:")
num_of_title = input("num of titles:")

num_of_title = int(num_of_title)
num_of_video = int(num_of_video) 
print('starting')
#图片循环数，每次以3或4递增
turn = 0
#title循环数，总循环数
title_num = 0
quit = False
quit_error = False
fo3 = open("./title.txt", "r", encoding='utf-8-sig')
fo2 = open("./video/video.txt", "r", encoding='utf-8-sig')
fo = open("./nameandpassword.txt", "r", encoding='utf-8-sig')

title_line = fo3.readlines()

video_line = fo2.readlines()



for line in fo.readlines():
	line = line.strip()
	arr = line.split('#')
	username = arr[0]
	password = arr[1]

#定义一个随机的等待时间
	range1 = random.randint(1,2)
	range2 = random.randint(2,4)
	#open website
	driver = webdriver.Firefox()
	driver.get("https://mp.yidianzixun.com/")#打开网页
	# driver.set_window_size(1920,1080)
	driver.maximize_window()
	time.sleep(range1)

#总循环，根据title在一个号里面的数量
	for i in range(0,20):
			if i<19:
				try:
					#click login
					driver.find_element_by_xpath("//*[@id='app']/div[3]/div[1]/div[3]/div/form/a[1]").click()
					time.sleep(range1)
					#driver.find_element_by_name('query').send_keys('python')
					#enter username and password
					driver.find_element_by_xpath("//input[@name='username']").send_keys(username)#插入用户名密码
					print("success username")
					driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
					print("success password")
					time.sleep(range1)


					#click login
					driver.find_element_by_xpath("//*[@id='app']/div[3]/div[1]/div[3]/div/form/div[3]/button").click()#点击login
					print("success login")
					time.sleep(range2)
					break
				except Exception as e:
					time.sleep(range2)
					i+=1
			else:
				print("*******用户名密码出现问题，请手动操作")
				os.system("pause")#s

		#-------------------------------------------------------------------------------------------------------
		#悬停在发布键上，然后点击视频，次循环，完成一个图集的循环
	for single_turn in range(num_of_title):
		quit_error == False
		print("在此账号中目前处于第： "+ str(single_turn+1)+"图集")
		for i in range(0,20):
			if i<19:
				try:
					ActionChains(driver).reset_actions()
					ele= driver.find_element_by_xpath("//*[@id='managePage']/div[2]/div/div/div[1]")
						# 鼠标移到悬停元素上
					ActionChains(driver).move_to_element(ele).perform()
					ActionChains(driver).reset_actions()
					#dian ji list
					driver.find_element_by_xpath("//*[@id='managePage']/div[2]/div/div/div[1]/div/ul/li[1]/a").click()#点击发视频
					print("success hover")
					time.sleep(range2)
					break
				except Exception as e:
					driver.refresh()
					ele= driver.find_element_by_xpath("//*[@id='managePage']/div[2]/div/div/div[1]")
						# 鼠标移到悬停元素上
					ActionChains(driver).move_to_element(ele).perform()
					ActionChains(driver).reset_actions()
					time.sleep(range2)
					i+=1
			else:
				print("进入发布视频页面出现问题，请手动操作")
				os.system("pause")#scan unicode

#check whether 5 tabs and enter invoke the windows window
		for l in range(5):
			if l<4:
				#click uplaod video
				for i in range(0,20):
					if i<19:
						try:
							driver.find_element_by_xpath("//*[@id='managePage']/div[3]/div[2]/div/div/div/div[1]/div[2]/a[1]").click()
							print("success click upload video")
							break
						except Exception as e:
							time.sleep(range2)
							i+=1

				time.sleep(range2)
				pyautogui.press(['tab', 'tab', 'tab'])
				time.sleep(range1)
				print("press tab five times")

				pyautogui.press('enter')
				time.sleep(range1)

				for i in range(0,20):
					if i<19:
						try:
							# num = str(len(3))
							pyautogui.typewrite('C:\\Users\\Administrator\\Desktop\\YIDIAN_shipin\\video')
							time.sleep(range1)
							pyautogui.press('enter')
							time.sleep(range2)
							break
						except Exception as e:
							time.sleep(range2+2)
							#scan unicode
							i = int(i)
							i+=1
					else:
						# os.system("pause")
						print("视频路径输入出现问题，请手动操作")

				#打开pic文件， 获取pic文件数量
				n=0
				# pic_num = random.randint(len(pic_line))
				#上传图片,向窗口中写文件名
				for j in range(10):
					if j<9:
						for line in video_line[turn:]:
							line = line.strip()
							line_arr = line.split(".")
							video_arr = line_arr[0]
							if n<num_of_video:
								try:
									print("now it is: " + line + " video")
									pyautogui.typewrite('"' + video_arr + '.flv"' + " ")
									time.sleep(1)
									print("success enter video files")
								except Exception as e:
									time.sleep(range1)
									j+=1
								n+=1
							else:
								break
						break
					else:
						print("视频名称输入出现问题，程序已暂停")
						# os.system("pause")#scan unicode



				for i in range(0,20):
					if i<19:
						try:
							# num = str(len(3))
							time.sleep(range2)
							pyautogui.press('enter')
							print("success uploaded")
							time.sleep(range2)

							break
						except Exception as e:
							time.sleep(range2+2)
							#scan unicode
							i = int(i)
							i+=1

				try:
					print("check click upload again")
					driver.find_element_by_xpath("//*[@id='managePage']/div[3]/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div[1]/a/div").click()
					break
				except Exception as e:
					driver.refresh()
					l+=1
			else:
				os.system("pause")
				print("视频上传出现问题，请手动操作，系统下一步为：检查视频上传")



		for i in range(0,20):
			if i<19:
				try:
					ele= driver.find_element_by_xpath("//*[@id='anchor-1']/div[1]/div[4]/button[1]")
						# 鼠标移到悬停元素上
					ActionChains(driver).move_to_element(ele).perform()
					ActionChains(driver).reset_actions()
					print("success check")
					time.sleep(range1)
					break
				except Exception as e:
					time.sleep(range2)
					i+=1
			else:
				print("悬停到删除键出现问题，请手动操作")
				os.system("pause")#s


		#some tips on the page
		for i in range(0,20):
			if i<19:
				try:
					driver.find_element_by_xpath("//*[@id='anchor-1']/div[2]/div[2]/div[1]/span/span/span[1]").click()
					time.sleep(range1)
					print("click tips")
					break
				except Exception as e:
					break
			else:
				print("点击tips出现问题，请手动操作")
				os.system("pause")#s


		#输入title
		for i in range(0,20):
			if i<19:
				try:
					print(title_num)
					title = title_line[title_num]
					element=driver.find_element_by_xpath("//*[@id='anchor-1']/div[2]/div[1]/div[2]/input")
					element.send_keys(Keys.CONTROL + 'a')
					driver.find_element_by_xpath("//*[@id='anchor-1']/div[2]/div[1]/div[2]/input").send_keys(title)#输入title
					print("success title")
					time.sleep(range1)
					break
				except Exception as e:
					time.sleep(range2)
					i+=1
			else:
				print("输入title出现问题，请手动操作")
				os.system("pause")#s


						#scroll down
		time.sleep(range1)
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight)"); 
		time.sleep(range1)


		single_turn+=1#for the biggest turn
		#第一个循环title输入结束，为第二循环准备
		title_num = title_num + 1
		
		for i in range(0,20):
			if i<19:
				try:
					#分类
					driver.find_element_by_xpath("//*[@id='anchor-1']/div[2]/div[3]/div[2]/div[1]/div/div[1]/input").click()
					print("success type1")
					time.sleep(range1)

					pyautogui.hotkey('ctrl', 'f')
					print("c+f")
					string_1 = "时尚"
					pyperclip.copy(string_1)
					pyautogui.hotkey('ctrl', 'v')
					print("c+v")
					time.sleep(range1)

					pyautogui.press('esc')
					print("press esc")

					#选择
					ele2 = driver.find_element_by_xpath("//*[@id='anchor-1']/div[2]/div[3]/div[2]/div[1]/div/div[2]/div/ul/li[35]")
					print("success shi shang ")
					time.sleep(range1)
					ActionChains(driver).move_to_element(ele2).perform()
					# "//li[contains(@title,'秀场街拍')]"

					#zi分类
					ele3 = driver.find_element_by_xpath("//*[@id='anchor-1']/div[2]/div[3]/div[2]/div[1]/div/div[2]/div/div/ul/li[3]")
					print("success hover and click jie pai ")
					ActionChains(driver).move_to_element(ele3).click().perform()
					ActionChains(driver).reset_actions()
					print("success choose type1")
					# # #zi选择
					# driver.find_element_by_xpath("//*[@id='managePage']/div[3]/div[2]/div/div/div/div[2]/div/div[1]/div[3]/div[2]/div[2]/div/div[1]").click()
					# print("success click type2")
					# time.sleep(range2)
					break
				except Exception as e:
					time.sleep(range2)
					i+=1
			else:
				print("选择分类出现问题，请手动操作")
				os.system("pause")#s

#-----------------------------------------------------------------------------------------------------------------
		#insert cover
		for i in range(0,20):
			if i<19:
				try:
		#插入正文
					driver.find_element_by_xpath("//*[@id='anchor-1']/div[2]/div[4]/div[2]/div[1]/div/div").click()
					print("success posted")
					time.sleep(range2)
					break
				except Exception as e:
					time.sleep(range2+2)
					#scan unicode
					i+=1
			else:
				print("封面上传出现问题")

#-----------------------------------------------------------------------------------------------------------------

					#click local upload
		for i in range(0,20):
			if i<9:
				try:
					driver.find_element_by_xpath("//*[@id='anchor-1']/div[2]/div[4]/div[3]/div[2]/div[2]/div[2]").click()
					print("success click local upload")
					time.sleep(range1)

					pyautogui.press('tab')
					print("press tab")

					pyautogui.press('enter')
					print("press enter")
					time.sleep(range1)
					break
				except Exception as e:
					i+=1
			else:
				print("封面上传tab/enter出现问题")


#enter name of the cover
		for j in range(10):
			if j<9:
				for line in video_line[turn:]:
					line = line.strip()
					line_arr = line.split(".")
					video_arr = line_arr[0]
					try:
						print("now it is: " + line + " video cover")
						pyautogui.typewrite('"' + video_arr + '.png"' + " ")
						time.sleep(range1)
						print("success enter video cover")
						break
					except Exception as e:
						time.sleep(range1)
						j+=1
				break
			else:
				print("上传图片出现问题")
		


#press enter for uploading cover

					# num = str(len(3))
		time.sleep(range2)
		pyautogui.press('enter')
		time.sleep(range1)
		print("success uploaded")
		time.sleep(range2)

		#click upload cover
		for i in range(0,20):
			if i<19:
				try:
		#插入正文
					driver.find_element_by_xpath("//*[@id='anchor-1']/div[2]/div[4]/div[3]/div[2]/div[3]/div/div[2]/div[2]/div[2]").click()
					time.sleep(range2)
					driver.find_element_by_xpath("//*[@id='anchor-1']/div[2]/div[5]/div[2]/div[1]/div[1]/input").click()
					print("success posted and checked")
					time.sleep(range1)
					break
				except Exception as e:
					time.sleep(range2)
					#scan unicode
					i+=1
					try:
						driver.find_element_by_xpath("//*[@id='anchor-1']/div[2]/div[5]/div[2]/div[1]/div[1]/input").click()
						time.sleep(range1)
						break
					except Exception as e:
						pass
			else:
				print("封面插入点击确定时出现问题，系统将自动进行下一组视频上传")
				with open('./not_uploaded.txt', 'a') as f_txt:
					f_txt.write('\n' + video_line[turn])
				quit_error = True
				break
		turn+=1
		#如果封面上传失败超过20次，系统跳过此次上传进行下一个视频
		if quit_error == False:
			#add tags
			for i in range(0,20):
				if i<20:
					try:
						driver.find_element_by_xpath("//*[@id='anchor-1']/div[2]/div[5]/div[2]/div[1]/div[1]/input").click()
						time.sleep(range1)
						print("success add cover")
						break
					except Exception as e:
						time.sleep(range2)
						#scan unicode
						i+=1
				else:
					os.system("pause")
					print("tag上传出现问题，请手动操作")


			#add tags
			for i in range(0,20):
				if i<20:
					try:
						driver.find_element_by_xpath("//*[@id='anchor-1']/div[2]/div[5]/div[2]/div[1]/div[1]/input").send_keys("美容")
						driver.find_element_by_xpath("//*[@id='anchor-1']/div[2]/div[5]/div[2]/div[1]/div[1]/input").send_keys(Keys.ENTER)
						driver.find_element_by_xpath("//*[@id='anchor-1']/div[2]/div[5]/div[2]/div[1]/div[1]/input").send_keys("化妆")
						driver.find_element_by_xpath("//*[@id='anchor-1']/div[2]/div[5]/div[2]/div[1]/div[1]/input").send_keys(Keys.ENTER)
						driver.find_element_by_xpath("//*[@id='anchor-1']/div[2]/div[5]/div[2]/div[1]/div[1]/input").send_keys("眼妆")
						driver.find_element_by_xpath("//*[@id='anchor-1']/div[2]/div[5]/div[2]/div[1]/div[1]/input").send_keys(Keys.ENTER)
						driver.find_element_by_xpath("//*[@id='anchor-1']/div[2]/div[5]/div[2]/div[1]/div[1]/input").send_keys("眼影")
						driver.find_element_by_xpath("//*[@id='anchor-1']/div[2]/div[5]/div[2]/div[1]/div[1]/input").send_keys(Keys.ENTER)
						driver.find_element_by_xpath("//*[@id='anchor-1']/div[2]/div[5]/div[2]/div[1]/div[1]/input").send_keys("美妆")
						driver.find_element_by_xpath("//*[@id='anchor-1']/div[2]/div[5]/div[2]/div[1]/div[1]/input").send_keys(Keys.ENTER)
						time.sleep(range1)
						print("add posted tags")
						break
					except Exception as e:	

						print(e)
						time.sleep(range2)
						#scan unicode
						i+=1
				else:
					os.system("pause")
					print("tag上传出现问题，请手动操作")


							#scroll down
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight)"); 
			time.sleep(range1)

			#原创
			try:
				driver.find_element_by_xpath("//*[@id='managePage']/div[3]/div[2]/div/div/div/div[2]/div/div[2]/div[3]/div/div[1]/div/div/div/div/div/span").click()
				print("success yuan chuang")
				time.sleep(range1)
				driver.find_element_by_xpath("//*[@id='dialog']/div/div[4]/div/button[2]").click()
				print("success click")
				time.sleep(range1)
			#发草稿
			#check draft
				for i in range(0,20):
					if i<20:
						try:
							driver.find_element_by_xpath("//*[@id='managePage']/div[3]/div[2]/div/div/div/div[2]/div/div[2]/div[4]/button[1]").click()
							print("CLICK draft")
							time.sleep(range1)
							driver.find_element_by_xpath("//*[@id='managePage']/div[3]/div[2]/div/div/div[2]/div[1]/div[4]/div").click()
							print("SUCCESS check draft")
							time.sleep(range1)
							break
						except Exception as e:
							try:
								ele2 = driver.find_element_by_xpath("//*[@id='managePage']/div[3]/div[2]/div/div/div/div[2]/div/div[2]/div[4]/button[1]")
								time.sleep(range1)
								ActionChains(driver).move_to_element(ele2).perform()
								i+=1
							except Exception as e:
								break
					else:
						os.system("pause")
						print("上传出现问题，请手动操作")
						
						
				print("finished all, system is closing")
				if single_turn == num_of_title:
					driver.quit()
					break

			except Exception as e:

			#如果没有原创直接发草稿+SECOND
				for i in range(0,20):
					if i<20:
						try:
							driver.find_element_by_xpath("//*[@id='managePage']/div[3]/div[2]/div/div/div/div[2]/div/div[2]/div[4]/button[1]").click()
							print("CLICK draft")
							time.sleep(range1)
							driver.find_element_by_xpath("//*[@id='managePage']/div[3]/div[2]/div/div/div[2]/div[1]/div[4]/div").click()
							print("SUCCESS check draft")
							time.sleep(range1)
							break
						except Exception as e:
							try:
								ele2 = driver.find_element_by_xpath("//*[@id='managePage']/div[3]/div[2]/div/div/div/div[2]/div/div[2]/div[4]/button[1]")
								time.sleep(range1)
								ActionChains(driver).move_to_element(ele2).perform()
								i+=1
							except Exception as e:
								break
					else:
						os.system("pause")			
						print("上传出现问题，请手动操作")
						
						
				print("finished all, system is closing")
				if single_turn == num_of_title:
					driver.quit()
					break
		else:
			if single_turn == num_of_title:
				driver.quit()
				break








