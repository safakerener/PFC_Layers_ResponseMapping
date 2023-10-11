% Generate all permutations of 8 items
items = ["turtle" "cat" "auto" "hand" "farleft" "farright" "nearleft" "nearright"];
all_permutations = perms(items);

% Create an Excel file to save the permutations
output_filename = "permutations.xlsx";
writematrix(all_permutations, output_filename, "Sheet", "Permutations");

disp(["All permutations of 8 items have been saved to ", output_filename]);