% Facts: diseases and their key symptoms
disease(malaria) :- has(fever), has(headache), has(cold).
disease(typhoid) :- has(fever), has(headache), has(cough).
disease(flu) :- has(fever), has(cough), has(cold).

% Ask user about a symptom
has(S) :- write('Do you have '), write(S), write('? (yes/no): '), read(yes).

% Diagnosis
diagnose :- disease(D), write('You may have: '), write(D), nl.
