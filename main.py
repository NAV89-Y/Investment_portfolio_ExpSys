import pandas as pd


def safe_input(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Пожалуйста, введите число от {min_val} до {max_val}.")
        except ValueError:
            print("Ошибка: введите целое число.")


def get_division(profile, term):
    rules = {
        'консервативный': {
            'короткий': {'Акции': 0, 'Облигации': 20, 'Депозиты': 65, 'Металлы': 15},
            'средний': {'Акции': 10, 'Облигации': 30, 'Депозиты': 45, 'Металлы': 15},
            'длинный': {'Акции': 20, 'Облигации': 35, 'Депозиты': 30, 'Металлы': 15}
        },
        'умеренный': {
            'короткий': {'Акции': 10, 'Облигации': 40, 'Депозиты': 40, 'Металлы': 10},
            'средний': {'Акции': 30, 'Облигации': 40, 'Депозиты': 15, 'Металлы': 15},
            'длинный': {'Акции': 50, 'Облигации': 25, 'Депозиты': 5, 'Металлы': 20}
        },
        'агрессивный': {
            'короткий': {'Акции': 40, 'Облигации': 30, 'Депозиты': 20, 'Металлы': 10},
            'средний': {'Акции': 60, 'Облигации': 15, 'Депозиты': 5, 'Металлы': 20},
            'длинный': {'Акции': 80, 'Облигации': 0, 'Депозиты': 0, 'Металлы': 20}
        }
    }
    return rules[profile][term]


def fmt_rub(x):
    return f"{x:,.2f}".replace(",", " ")


user_data = None
division = None
while True:
    print("=" * 60 + "\n\tМеню:"
                     "\n1 - определение риск-профиля и горизонта вложения"
                     "\n2 - ввод риск-профиля и горизонта вложения"
                     "\n3 - определение распределения активов в портфеле"
                     "\n4 - ввод распределения активов в портфеле"
                     "\n5 - рекомендация по составлению инвестиционного портфеля"
                     "\n0 - выход\n" + "=" * 60)
    choice = safe_input("Выберите пункт: ",0,5)
    if choice == 0:
        print("Выход из программы.")
        break
    elif choice == 1:
        print("\n" + "=" * 60)
        print("\t=== Определение риск-профиля и горизонта вложения ==="
              "\nДля этого необходимо пройти небольшой тест:")

        print("\n\t1) Какую сумму вы планируете инвестировать?"
              "\n1 - до 100 000 руб."
              "\n2 - 100 000 - 500 000 руб."
              "\n3 - 500 000 - 1 000 000 руб."
              "\n4 - 1 000 000 - 3 000 000 руб."
              "\n5 - более 3 000 000 руб.")
        sum_choice = safe_input("Ответ: ", 1, 5)
        summary = {1: 50000, 2: 300000, 3: 750000, 4: 2000000, 5: 5000000}[sum_choice]

        print("\n\t2) На какой срок вы готовы инвестировать средства?"
              "\n1 - менее 1 года"
              "\n2 - от 1 года до 3 лет"
              "\n3 - более 3 лет")
        term_choice = safe_input("Ответ: ", 1, 3)
        term = {1: "короткий", 2: "средний", 3: "длинный"}[term_choice]

        print("\n\t3) Как вы отреагируете, если стоимость вашего портфеля через месяц снизится на 10%?"
              "\n1 - Продам всё, чтобы не потерять больше"
              "\n2 - Подожду, но буду сильно нервничать"
              "\n3 - Ничего не предприму, восприму как нормальное колебание"
              "\n4 - Куплю ещё, так как вижу возможность")
        risk_choice = safe_input("Ответ: ", 1, 4)
        risk = {1: 0, 2: 1, 3: 2, 4: 3}[risk_choice]

        print("\n\t4) Какая цель вам ближе?"
              "\n1 - Сохранить капитал, избежать любых убытков"
              "\n2 - Получить доход немного выше инфляции, риски минимальны"
              "\n3 - Сбалансированный рост с приемлемыми рисками"
              "\n4 - Максимальный долгосрочный рост, готов к сильным колебаниям")
        risk_choice = safe_input("Ответ: ", 1, 4)
        risk += {1: 0, 2: 1, 3: 2, 4: 3}[risk_choice]

        print("\n\t5) Какая максимальная годовая просадка (в процентах от портфеля) допустима для вас?"
              "\n1 - не более 5%"
              "\n2 - от 5% до 10%"
              "\n3 - от 10% до 20%"
              "\n4 - более 20%")
        risk_choice = safe_input("Ответ: ", 1, 4)
        risk += {1: 0, 2: 1, 3: 2, 4: 3}[risk_choice]

        if risk <= 2:
            profile = "консервативный"
        elif risk <= 6:
            profile = "умеренный"
        else:
            profile = "агрессивный"

        print("\n" + "=" * 60)
        print("\tРезультаты опроса:")
        print(f"Сумма инвестиций: {summary} руб.")
        print(f"Горизонт вложения: {term}")
        print(f"Риск-профиль: {profile}")

        user_data = {
            "Сумма инвестиций": summary,
            "Горизонт вложения": term,
            "Риск-профиль": profile
        }
    elif choice == 2:
        print("\n" + "=" * 60)
        print("\t=== Ввод риск-профиля и горизонта вложения ===")
        print("\n\tВыберите риск-профиль:"
              "\n1 - консервативный"
              "\n2 - умеренный"
              "\n3 - агрессивный")
        profile_choice = safe_input("Ответ: ", 1, 3)
        profile = {1: "консервативный", 2: "умеренный", 3: "агрессивный"}[profile_choice]
        print("\n\tВыберите горизонт инвестирования:"
              "\n1 - короткий (до 1 года)"
              "\n2 - средний (1-3 года)"
              "\n3 - длинный (более 3 лет)")
        term_choice = safe_input("Ответ: ", 1, 3)
        term = {1: "короткий", 2: "средний", 3: "длинный"}[term_choice]
        print("\n\tВыберите сумму инвестирования:"
              "\n1 - до 100 000 руб."
              "\n2 - 100 000 - 500 000 руб."
              "\n3 - 500 000 - 1 000 000 руб."
              "\n4 - 1 000 000 - 3 000 000 руб."
              "\n5 - более 3 000 000 руб.")
        sum_choice = safe_input("Ответ: ", 1, 5)
        summary = {1: 50000, 2: 300000, 3: 750000, 4: 2000000, 5: 5000000}[sum_choice]

        print("\n" + "=" * 60)
        print("\tРезультаты ввода:")
        print(f"Сумма инвестиций: {summary} руб.")
        print(f"Горизонт вложения: {term}")
        print(f"Риск-профиль: {profile}")

        user_data = {
            "Сумма инвестиций": summary,
            "Горизонт вложения": term,
            "Риск-профиль": profile
        }
    elif choice == 3:
        print("\n" + "=" * 60)
        if user_data is None:
            print("Сначала выполните опрос (пункт 1) или ручной ввод (пункт 2).")
        else:
            print("\t=== Расчёт распределения активов в портфеле ===")
            profile = user_data['Риск-профиль']
            term = user_data['Горизонт вложения']
            division = get_division(profile, term)
            print("\n" + "=" * 60)
            print("Рекомендуемая структура портфеля:")
            print(f"  Акции:       {division['Акции']}%")
            print(f"  Облигации:   {division['Облигации']}%")
            print(f"  Депозиты:    {division['Депозиты']}%")
            print(f"  Металлы:     {division['Металлы']}%")
            print("=" * 60)
    elif choice == 4:
        print("\n" + "=" * 60)
        print("\t=== Ввод распределения акций в портфеле ==="
              "\nВведите доли активов в процентах:")
        stocks = safe_input("Доля акций: ", 0, 100)
        bonds = safe_input("Доля облигаций: ", 0, 100 - stocks)
        deposits = safe_input("Доля депозитов: ", 0, 100 - stocks - bonds)
        metals = safe_input("Доля металлов: ", 0, 100 - stocks - bonds - deposits)
        total = stocks + bonds + deposits + metals
        if total != 100:
            print(
                f"Сумма долей {total}% не равна 100%. Автоматическая корректировка: металлы = {100 - stocks - bonds - deposits}%")
            metals = 100 - stocks - bonds - deposits
        division = {
            'Акции': stocks,
            'Облигации': bonds,
            'Депозиты': deposits,
            'Металлы': metals
        }
        print("\n" + "=" * 60)
        print("Введенная структура портфеля:")
        print(f"  Акции:       {division['Акции']}%")
        print(f"  Облигации:   {division['Облигации']}%")
        print(f"  Депозиты:    {division['Депозиты']}%")
        print(f"  Металлы:     {division['Металлы']}%")
    elif choice == 5:
        print("\n" + "=" * 60)
        if user_data is None:
            print("Сначала выполните опрос (пункт 1) или ручной ввод (пункт 2).")
            continue
        if division is None:
            print("Сначала рассчитайте или введите распределение активов (пункт 3 или 4).")
            continue

        amount = user_data["Сумма инвестиций"]
        term = user_data["Горизонт вложения"]
        profile = user_data["Риск-профиль"]

        try:
            file = pd.read_excel('Assets.xlsx', sheet_name='Лист1', dtype={'ticker': str})
        except Exception as e:
            print(f"Ошибка загрузки файла: {e}")
            continue

        num_cols = ['current_price', 'dividend_yield_percent', 'beta',
                    'duration_years', 'term_year', 'expected_return_annual', 'volatility_annual']
        for col in num_cols:
            if col in file.columns:
                file[col] = pd.to_numeric(file[col], errors='coerce')

        stocks_file = file[file['asset_class'] == 'Акции'].copy()
        bonds_file = file[file['asset_class'] == 'Облигации'].copy()
        deposits_file = file[file['asset_class'] == 'Депозиты'].copy()
        metals_file = file[file['asset_class'] == 'Металлы'].copy()

        if profile == 'консервативный':
            stocks_file = stocks_file[stocks_file['beta'] < 0.9]
            stocks_file = stocks_file.sort_values('dividend_yield_percent', ascending=False)
        elif profile == 'агрессивный':
            stocks_file = stocks_file[stocks_file['beta'] > 1.1]
            stocks_file = stocks_file.sort_values('upside_potential_percent', ascending=False)
        else:
            stocks_file = stocks_file[(stocks_file['beta'] >= 0.8) & (stocks_file['beta'] <= 1.2)]
            stocks_file = stocks_file.sort_values('dividend_yield_percent', ascending=False)
        if len(stocks_file) < 2:
            stocks_file = file[file['asset_class'] == 'Акции'].copy()
            stocks_file = stocks_file.sort_values('dividend_yield_percent', ascending=False)
        top_stocks = stocks_file.head(3)

        bonds_file = bonds_file[bonds_file['dividend_yield_percent'].notna()]
        if bonds_file.empty:
            bonds_file = file[file['asset_class'] == 'Облигации'].copy()
        else:
            if profile == 'консервативный':
                bonds_file = bonds_file[(bonds_file['duration_years'] < 5) | (bonds_file['duration_years'].isna())]
                bonds_file = bonds_file[
                    bonds_file['credit_rating'].isin(['AAA', 'AA', 'AA-']) | bonds_file['credit_rating'].isna()]
            elif profile == 'агрессивный':
                bonds_file = bonds_file[(bonds_file['duration_years'] >= 3) | (bonds_file['duration_years'].isna())]
            else:
                bonds_file = bonds_file[(bonds_file['duration_years'] <= 7) | (bonds_file['duration_years'].isna())]
            bonds_file = bonds_file.sort_values('dividend_yield_percent', ascending=False)
        if bonds_file.empty:
            bonds_file = file[file['asset_class'] == 'Облигации'].copy().head(2)
        top_bonds = bonds_file.head(2)

        if term == 'короткий':
            target_term = 0.5
        elif term == 'средний':
            target_term = 2
        else:
            target_term = 5
        best_deposit = None
        deposits_file['term_diff'] = abs(deposits_file['term_year'] - target_term)
        best_deposit = deposits_file.loc[deposits_file['term_diff'].idxmin()].copy()

        selected_metals = []
        if profile == 'консервативный':
            gold = metals_file[metals_file['ticker'] == 'GOLD']
            selected_metals.append(gold.iloc[0].copy())
        elif profile == 'умеренный':
            for ticker in ['GOLD', 'SILV']:
                metal = metals_file[metals_file['ticker'] == ticker]
                selected_metals.append(metal.iloc[0].copy())
        else:
            for ticker in ['GOLD', 'SILV', 'PLAT', 'PALL']:
                metal = metals_file[metals_file['ticker'] == ticker]
                selected_metals.append(metal.iloc[0].copy())

        rub_stocks = amount * division['Акции'] / 100
        rub_bonds = amount * division['Облигации'] / 100
        rub_deposits = amount * division['Депозиты'] / 100
        rub_metals = amount * division['Металлы'] / 100

        stocks_result = []
        if division['Акции'] > 0 and not top_stocks.empty:
            per_stock = rub_stocks / len(top_stocks)
            for index, row in top_stocks.iterrows():
                price = row['current_price']
                qty = int(per_stock // price)
                cost = qty * price
                div_yield = row.get('dividend_yield_percent', 0)
                income = cost * div_yield / 100
                stocks_result.append({
                    'name': row['name'], 'ticker': row['ticker'],
                    'price': price, 'qty': qty, 'cost': cost,
                    'div_yield': div_yield, 'income': income
                })

        bonds_result = []
        if division['Облигации'] > 0 and not top_bonds.empty:
            per_bond = rub_bonds / len(top_bonds)
            for index, row in top_bonds.iterrows():
                price = row['current_price']
                qty = int(per_bond // price)
                cost = qty * price
                ytm = row.get('dividend_yield_percent', 0)
                income = cost * ytm / 100
                bonds_result.append({
                    'name': row['name'], 'ticker': row['ticker'],
                    'price': price, 'qty': qty, 'cost': cost,
                    'ytm': ytm, 'income': income
                })

        deposit_result = None
        if division['Депозиты'] > 0 and best_deposit is not None:
            rate = best_deposit.get('dividend_yield_percent', 0)
            cost = rub_deposits
            income = cost * rate / 100
            deposit_result = {
                'name': best_deposit['name'],
                'rate': rate,
                'cost': cost,
                'income': income,
                'term': best_deposit.get('term_year'),
                'capitalization': best_deposit.get('capitalization')
            }

        metals_result = []
        if division['Металлы'] > 0 and selected_metals:
            per_metal = rub_metals / len(selected_metals)
            for metal in selected_metals:
                price = metal['current_price']
                qty = per_metal / price
                cost = qty * price
                exp_return = metal.get('expected_return_annual')
                income = cost * exp_return / 100
                metals_result.append({
                    'name': metal['name'], 'ticker': metal['ticker'],
                    'price': price, 'qty': qty, 'cost': cost,
                    'exp_return': exp_return, 'income': income
                })

        print("=== Рекомендации для составления инвестиционного портфеля ===")
        print(f"\nСумма инвестиций: {fmt_rub(amount)} руб.")
        print(f"Риск-профиль: {profile.capitalize()} | Горизонт: {term}")
        print("\nСтруктура портфеля:")
        print(f"\tАкций:     {division['Акции']}%  на {fmt_rub(rub_stocks)} руб.")
        print(f"\tОблигаций: {division['Облигации']}%  на {fmt_rub(rub_bonds)} руб.")
        print(f"\tДепозит:  {division['Депозиты']}%  на {fmt_rub(rub_deposits)} руб.")
        print(f"\tМеталлов:   {division['Металлы']}%  на {fmt_rub(rub_metals)} руб.")

        all_costs = 0
        all_incomes = 0

        if stocks_result:
            print("-" * 60)
            print("=== Акции ===")
            total_cost = sum(i['cost'] for i in stocks_result)
            all_costs += total_cost
            total_income = sum(i['income'] for i in stocks_result)
            all_incomes += total_income
            for i in stocks_result:
                print(f"\n{i['name']} ({i['ticker']})")
                print(f"\tЦена: {i['price']:.2f} руб.")
                print(f"\tКоличество: {i['qty']} шт.")
                print(f"\tЗатраты: {fmt_rub(i['cost'])} руб.")
                print(f"\tДив.доходность: {i['div_yield']:.2f}%")
                print(f"\tОжидаемый дивидендный доход в год: {fmt_rub(i['income'])} руб.")
            print(
                f"Всего по акциям:\n\tзатраты - {fmt_rub(total_cost)} руб.\n\tгодовой доход - {fmt_rub(total_income)} руб.")
        else:
            print("-" * 60)
            print("Акции не определены")

        if bonds_result:
            print("-" * 60)
            print("=== Облигации ===")
            total_cost = sum(i['cost'] for i in bonds_result)
            all_costs += total_cost
            total_income = sum(i['income'] for i in bonds_result)
            all_incomes += total_income
            for i in bonds_result:
                print(f"\n{i['name']} ({i['ticker']})")
                print(f"\tЦена: {i['price']:.2f} руб.")
                print(f"\tКоличество: {i['qty']} шт.")
                print(f"\tЗатраты: {fmt_rub(i['cost'])} руб.")
                print(f"\tДоходность (YTM): {i['ytm']:.2f}%")
                print(f"\tОжидаемый купонный доход в год: {fmt_rub(i['income'])} руб.")
            print(
                f"Всего по облигациям:\n\tзатраты - {fmt_rub(total_cost)} руб.\n\tгодовой доход - {fmt_rub(total_income)} руб.")
        else:
            print("-" * 60)
            print("Облигации не определены")

        if deposit_result:
            all_costs += deposit_result['cost']
            all_incomes += deposit_result['income']
            print("-" * 60)
            print("=== Депозит ===")
            print(f"\n{deposit_result['name']}")
            print(f"\tСумма вклада: {fmt_rub(deposit_result['cost'])} руб.")
            print(f"\tСтавка: {deposit_result['rate']:.2f}% годовых")
            print(f"\tСрок: {deposit_result['term']} лет")
            print(f"\tКапитализация: {'Да' if deposit_result['capitalization'] == 'Yes' else 'Нет'}")
            print(f"\tОжидаемый доход за год: {fmt_rub(deposit_result['income'])} руб.")
            if deposit_result['capitalization'] == 'Yes':
                print("\t(При капитализации фактический доход будет выше за счёт сложного процента)")
        else:
            print("-" * 60)
            print("Депозит не определён")

        if metals_result:
            print("-" * 60)
            print("=== Драгоценные металлы ===")
            total_cost = sum(i['cost'] for i in metals_result)
            all_costs += total_cost
            total_income = sum(i['income'] for i in metals_result)
            all_incomes += total_income
            for i in metals_result:
                print(f"\n{i['name']} ({i['ticker']})")
                print(f"\tЦена за грамм: {i['price']:.2f} руб.")
                print(f"\tКоличество грамм: {i['qty']:.3f} г")
                print(f"\tЗатраты: {fmt_rub(i['cost'])} руб.")
                print(f"\tОжидаемая доходность (оценка): {i['exp_return']:.1f}% годовых")
                print(f"\tПотенциальный доход за год: {fmt_rub(i['income'])} руб.")
            print(
                f"Всего по металлам:\n\tзатраты {fmt_rub(total_cost)} руб.\n\tпотенциальный доход {fmt_rub(total_income)} руб.")
        else:
            print("-" * 60)
            print("Металлы не определены")

        overall_yield = (all_incomes / all_costs) * 100

        print("\n" + "=" * 60)
        print("=== ИТОГО ===")
        print(f"\nОбщая сумма вложений: {fmt_rub(all_costs)} руб.")
        print(f"Суммарный ожидаемый годовой доход: {fmt_rub(all_incomes)} руб.")
        print(f"Ожидаемая годовая доходность портфеля: {overall_yield:.2f}%")
    else:
        print("Неверный ввод, попробуйте снова.")
