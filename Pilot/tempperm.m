function [comb_objfirst, comb_orifirst] = tempperm(obj, ori)

% Calculate all permutations of names and shapes
% Generate all 24x24 combinations

% Calculate all permutations of names and shapes
perm_obj = npermutek(obj, 4);
perm_ori = npermutek(ori, 4);


% Initialize an empty cell array to store the combinations
comb_objfirst = cell(24*24, 8);

% Iterate through each name and combine it with each shape
count = 1;
for i = 1:24
    cur_obj = perm_obj(i,:);
    for j = 1:24
        cur_ori = perm_ori(j,:);
        comb_objfirst(count,:) = [cur_obj cur_ori];
        count = count + 1;
    
    end
end


% Initialize an empty cell array to store the combinations
comb_orifirst = cell(24*24, 8);

% Iterate through each name and combine it with each shape
count = 1;
for k = 1:24
    cur_ori = perm_ori(k,:);
    for l = 1:24
        cur_obj = perm_obj(l,:);
        comb_orifirst(count,:) = [cur_ori cur_obj];
        count = count + 1;
    
    end
end


% Define the file name
file_objfirst = 'comb_objfirst.xlsx';
file_orifirst = 'comb_orifirst.xlsx';

fprintf('Combinations created.');
