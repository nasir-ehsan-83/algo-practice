def bmi_calculator(weight: float, height: float) -> tuple[float, str]:
    
    bmi: float = weight / (height * height);
    category: str;

    if bmi < 18.5:
        category = "Underweight";
    
    elif bmi < 25:
        category = "Normal weight";
    
    elif bmi < 30:
        category = "Overweight";
    
    else:
        category = "Obese";
    
    return round(bmi,2), category;
