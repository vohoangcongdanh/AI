# nhập thư viện
import speech_recognition
import pyttsx3
from datetime import date 
from datetime import datetime
# khởi tạo
robot_ear=speech_recognition.Recognizer()
robot_brain=""
robot_mouth=pyttsx3.init()
while True: 
# nghe
	with speech_recognition.Microphone() as mic:
		print("Robot: Tôi đang nghe")
		audio=robot_ear.listen(mic)

	try:
		you=robot_ear.recognize_google(audio)
	except:
		you=""
	print("You: "+you)
	print('...')
# hiểu
	if "hello" in you or "hi" in you:
		robot_brain= "Hello Mr Danh"
	elif "name" in you:
		robot_brain="My name is J.A.R.V.I.S"
	elif you=="":
		robot_brain="Sorry i don't understand what you're saying, please say again, thanks"
	elif "today" in you:
		today=date.today()
		robot_brain=today.strftime("%B %d,%Y")
	elif "time" in you:
		now=datetime.now()
		current_time=now.strftime("%H hours %M minutes %S seconds")
	elif "do" in you:
		robot_brain="Yeah, she is a chicken"
	elif "bye" in you:
		robot_brain="Bye Mr Danh"
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
		print("Robot: "+robot_brain)
		break
	print("Robot: "+robot_brain)
# nói
	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()
	print("----------------------------------------------")