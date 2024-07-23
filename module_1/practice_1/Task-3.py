str1 = "Я.внима?тельноне_слушал учителя.и?не_понял.!всё!!!"
str1 = str1.replace("_", " ")
str1 = str1.replace(".", " ")
str1 = str1.replace("не", "")
str1 = str1.replace("?", "")
str1 = str1.replace("!", "", 3)
print(str1)
