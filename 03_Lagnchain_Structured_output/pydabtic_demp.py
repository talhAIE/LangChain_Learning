# we have to create a dictionary of a student where we want student name in string datatype
from pydantic import BaseModel,EmailStr,Field # Field for constraints
from typing import Optional

class Student(BaseModel):
    
    name:str

    # we can also set default values
    age:int = 32

    # with optional
    father_name: Optional[str]=None

    # Email data type in pydantic
    email: EmailStr

    cgpa: float =Field(gt=0,lt=4, default=1,description='decimal value representing the CGPA of Student')

# std={'name':'Talha'}
# std={'name':'Talha','father_name':'Talib'}
std={'name':'Talha','father_name':'Talib','age':'32','email':'abc@gmail.com'} #pydantic can automatically can to type converting
student=Student(**std)
print(student)
print(type(student))

student_dict=dict(student)
print(student_dict['age'])