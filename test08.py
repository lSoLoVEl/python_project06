#เขียนโปรแกรม  รับชื่อ อายุ ทางแป้นพิมพ์ แล้วแสดงผลออกมาว่า ชื่อ อายุ เป้น เด็ก คนหนุ่ม หรือคนแก่
#อายุตั้งแต่ 18 คือ เด็ก /อายุ19-45 คุมหนุ่ม/46 ขึ้นคือคนแค่

#หาฟิเจอร์การทำงาน เพื่อจะเอาไปเขียนเป็นฟังก์ชั้น

#1.รับค่าข้อมูล  2.ตรวจสอบและแสดงผลว่าเป็น เด็ก คนหนุ่ม หรือคนแก่ 3.แสดงชท่อโปรแกรม

def showProgramName() :
    print('**--โปรแกรมตรวจสอบความเป็นเด็ก หนุ่ม หรือแก่--**')

def inputData( ) :
    name = input('โปรดป้อนชื่อ : ')
    age = int(input('โปรดป้อนอายุ : '))
    return name, age

def checkShowStatus(name,age) :
    if age <= 18 :
        print(f'คุณ{name} อายุ {age} ปี เป็นเด็ก')
    elif age >=19 and age <= 45 :
        print(f'คุณ{name} อายุ {age} ปี เป็นคนหนุ่ม')
    else :
        print(f'คุณ{name} อายุ {age} ปี เป็นคนแก่')

print('---------------------------------------')
showProgramName()
print('---------------------------------------')
name,age = inputData()
print('---------------------------------------')
checkShowStatus(name,age)
print('---------------------------------------')