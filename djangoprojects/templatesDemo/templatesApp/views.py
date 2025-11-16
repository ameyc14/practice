from django.shortcuts import render




def renderTemplate(request):
    myDict={"name":"Amey","age":33}
    return render(request,'templatesApp/firstTemplate.html',myDict)

def renderEmployee(request):
    myDict={"id":123,"name":"amey","sal":1000}
    return render(request,'templatesApp/employeeTemplate.html',myDict)
