from django.shortcuts import render
# Create your views here.


meals = [
    {
        "strMeal": "BeaverTails",
        "strMealThumb": "https://www.themealdb.com/images/media/meals/ryppsv1511815505.jpg",
        "idMeal": "52928",
        "description": "BeaverTails is a popular Canadian pastry that is deep-fried and often served with various toppings like cinnamon sugar or chocolate."
    },
    {
        "strMeal": "Breakfast Potatoes",
        "strMealThumb": "https://www.themealdb.com/images/media/meals/1550441882.jpg",
        "idMeal": "52965",
        "description": "Breakfast Potatoes are a classic morning dish, typically consisting of diced or sliced potatoes seasoned and cooked until crispy."
    },
    {
        "strMeal": "Canadian Butter Tarts",
        "strMealThumb": "https://www.themealdb.com/images/media/meals/wpputp1511812960.jpg",
        "idMeal": "52923",
        "description": "Canadian Butter Tarts are sweet pastries filled with a gooey, buttery filling, often containing pecans or raisins."
    },
    {
        "strMeal": "Montreal Smoked Meat",
        "strMealThumb": "https://www.themealdb.com/images/media/meals/uttupv1511815050.jpg",
        "idMeal": "52927",
        "description": "Montreal Smoked Meat is a type of kosher-style deli meat made by curing and smoking beef brisket with a blend of spices."
    },
    {
        "strMeal": "Nanaimo Bars",
        "strMealThumb": "https://www.themealdb.com/images/media/meals/vwuprt1511813703.jpg",
        "idMeal": "52924",
        "description": "Nanaimo Bars are a no-bake Canadian dessert bar, consisting of three layers: a crumbly base, a custard-flavored middle, and a chocolate topping."
    },
    {
        "strMeal": "Pate Chinois",
        "strMealThumb": "https://www.themealdb.com/images/media/meals/yyrrxr1511816289.jpg",
        "idMeal": "52930",
        "description": "Pate Chinois, also known as Shepherd's Pie, is a classic Canadian comfort food made with layers of ground beef, corn, and mashed potatoes."
    },
    {
        "strMeal": "Pouding chomeur",
        "strMealThumb": "https://www.themealdb.com/images/media/meals/yqqqwu1511816912.jpg",
        "idMeal": "52932",
        "description": "Pouding chomeur is a traditional Quebecois dessert, consisting of a sticky, sweet cake-like pudding topped with a rich maple syrup sauce."
    },
    {
        "strMeal": "Poutine",
        "strMealThumb": "https://www.themealdb.com/images/media/meals/uuyrrx1487327597.jpg",
        "idMeal": "52804",
        "description": "Poutine is a famous Canadian dish that features french fries topped with cheese curds and smothered in gravy."
    },
    {
        "strMeal": "Rappie Pie",
        "strMealThumb": "https://www.themealdb.com/images/media/meals/ruwpww1511817242.jpg",
        "idMeal": "52933",
        "description": "Rappie Pie is a traditional Acadian dish made with grated potatoes, meat (such as chicken or pork), and sometimes vegetables."
    },
    {
        "strMeal": "Split Pea Soup",
        "strMealThumb": "https://www.themealdb.com/images/media/meals/xxtsvx1511814083.jpg",
        "idMeal": "52925",
        "description": "Split Pea Soup is a hearty soup made with dried split peas, vegetables, and often includes ham or bacon for added flavor."
    }
]


def home(request):
    return render(request, 'index.html', {'meals': meals})
