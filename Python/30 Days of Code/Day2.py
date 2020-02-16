#!/bin/python3

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    tax_cost = meal_cost * tax_percent/100
    tip_cost = meal_cost * tip_percent/100
    total_cost = meal_cost + tip_percent + tax_percent
    print(round(meal_cost + tax_cost + tip_cost))
