from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def recipe_view(request, dish):
    # Получаем рецепт из DATA
    recipe = DATA.get(dish)
    
    if recipe is None:
        # Если рецепт не найден, возвращаем пустой словарь
        context = {'recipe': {}}
        return render(request, 'calculator/index.html', context)
    
    # Создаем копию рецепта для модификации
    calculated_recipe = recipe.copy()
    
    # Обрабатываем параметр servings (необязательный)
    servings = request.GET.get('servings')
    if servings:
        try:
            servings_int = int(servings)
            if servings_int > 0:
                # Умножаем все ингредиенты на количество порций
                for ingredient in calculated_recipe:
                    calculated_recipe[ingredient] *= servings_int
        except (ValueError, TypeError):
            # Если servings не число, используем исходный рецепт
            pass
    
    context = {
        'recipe': calculated_recipe
    }
    
    return render(request, 'calculator/index.html', context)
