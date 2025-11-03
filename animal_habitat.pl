% --- Facts: animal(Name, Type) ---
animal(fish, water).
animal(dolphin, water).
animal(lion, land).
animal(elephant, land).
animal(eagle, air).
animal(parrot, air).

% --- Rules ---
lives_in_water(X) :- animal(X, water).
lives_on_land(X)  :- animal(X, land).
can_fly(X)       :- animal(X, air).

% --- Example Queries ---
% ?- lives_in_water(dolphin).
% ?- lives_on_land(lion).
% ?- can_fly(eagle).
