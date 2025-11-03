% --- Facts: dish(Name, Type, Taste) ---
dish(paneer_butter_masala, veg, mild).
dish(veg_biryani, veg, spicy).
dish(chicken_curry, nonveg, spicy).
dish(fish_fry, nonveg, mild).
dish(dal_tadka, veg, mild).
dish(chilli_chicken, nonveg, spicy).

% --- Rules for recommendations ---
recommend(Type, Taste, Dish) :-
    dish(Dish, Type, Taste).

% --- Example Queries ---
% ?- recommend(veg, spicy, D).
% ?- recommend(nonveg, mild, D).
