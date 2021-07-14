# 에러 처리
# try ~ except : 기본
# try ~ except ~ else :
# try ~ except ~ else ~ finally
# try ~ finally

print("에러 발생 처리")

x=[10,20,30]

try:
    print(x[3])
except:
    print("not found")

#%%
print("안녕하세요")
#%%
name =["Kim","Park","Lee"]


try:
    z="Let"
    x=name.index(z)
    print("{} found it! in name{1}".format(z,x+1))
except:
    print("Not found")

#%%






# %%
name=["Kim","Park","Lee"]


try:
    z="Kim"
    x=name.index(z) # ValueError
    print("{0} found it! in name{1}".format(z,x+1))
except ValueError: #Exception => 무슨 에러인지 모르면 한꺼번에 처리 가능
    print("Not found")
else:
    print("OK!!")

# %%
x=[10,20,30]

try:
    print(x[3])
except:
    print("not found")
else: 
    print("found")
finally:
    print("OK!!")

# %%
try:
    print("Try")
finally:
    print("Finally")

# %%
name1=["choi","park","kim","lee"]

try:
    name1.index("cho")
except ValueError:
    print("ValueError")
except IndexError:
    print("IndexError")
except Exception:
    print("Exception")
else: #에러가 안나는 경우
    print("else")
finally: #무조건 실행
    print("finally")

# %%
try:
    a='333'
    if a=="kim":
        print("허가!!!")
    else:
        raise ValueError
except ValueError:
    print("문제 발생")
except Exception as e:
    print(e)
else:
    print('OK')


# %%
number = int(input("정수입력 : "))

if number >0:
    raise NotImplementedError
else:
    raise NotImplementedError