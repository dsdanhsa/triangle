from django.shortcuts import render

def home(request):
    # Initialize result as None by default
    result = None

    # Check if form data is submitted using POST method
    if request.method == 'POST':
        # Get the values of triangle sides from the form
        side1 = float(request.POST.get('side1', 0))
        side2 = float(request.POST.get('side2', 0))
        side3 = float(request.POST.get('side3', 0))

        # Check if any side is non-positive
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            result = "All sides must be positive values."

        # Check if the sum of any two sides is less than the third side
        elif side1 + side2 <= side3 or side2 + side3 <= side1 or side1 + side3 <= side2:
            result = "It's not a valid triangle. The sum of any two sides should be greater than the third side."

        # Check for special cases (equilateral, isosceles, or scalene)
        else:
            if side1 == side2 == side3:
                result = "It's an equilateral triangle!"
            elif side1 == side2 or side2 == side3 or side1 == side3:
                result = "It's an isosceles triangle."
            else:
                result = "It's a scalene triangle."

    # Render the HTML template with the result
    return render(request, 'tuapp/home.html', {'result': result})
