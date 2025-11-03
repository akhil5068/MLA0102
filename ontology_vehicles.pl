% --- Facts: vehicle(Name, Wheels, EngineType, Size) ---
vehicle(car, 4, petrol, medium).
vehicle(truck, 6, diesel, large).
vehicle(bike, 2, petrol, small).
vehicle(bus, 6, diesel, large).

% --- Rules for classification ---
is_two_wheeler(V) :- vehicle(V, 2, _, _).
is_four_wheeler(V) :- vehicle(V, 4, _, _).
is_heavy_vehicle(V) :- vehicle(V, _, diesel, large).
is_light_vehicle(V) :- vehicle(V, _, petrol, small).

% --- Example Queries ---
% ?- is_two_wheeler(bike).
% ?- is_heavy_vehicle(bus).
% ?- is_four_wheeler(car).
