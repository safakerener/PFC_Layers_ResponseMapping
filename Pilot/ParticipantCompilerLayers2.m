% written by Safak Erener (safakerener@gmail.com)
% last updated 06.11.2023

% Change to the desired working directory
% cd('C:\Users\willi\Desktop\PFC_Layers\PFC_Layers_ResponseMapping\Pilot')

% cd('C:\Users\erene\OneDrive\Desktop\PFC Layers\PFC_Layers_ResponseMapping\Pilot')

% Create a GUI for entering the participant number and number of blocks
prompt = {'Enter Participant Number:', 'Number of Blocks:'};
dlgtitle = 'Input Values';
definput = {'', '6'}; % Default values
dims = [1 50];
inputValues = inputdlg(prompt, dlgtitle, dims, definput);

if isempty(inputValues)
    return; % User canceled the input
end


participant = inputValues{1};
numBlocks = str2double(inputValues{2});

% Create a directory in the "participantData" folder based on the participant number
dataDir = fullfile('participantData', sprintf('s%s', participant));

if ~exist(dataDir, 'dir')
    mkdir(dataDir);
else
    disp('ERROR: Participant folder exists. Overwrite aborted.')
    return
end


% BLOCK 0 IS TRAINING

for n = 1:numBlocks+1

    % Set the random number generator seed for reproducibility
    
    block = sprintf('block_%s', num2str(n-1));

    rng((str2double(participant)+13)*log(str2double(block(end))+1));


    % Create a directory for each block within the participant's folder
    blockDir = fullfile(dataDir, block);

    if ~exist(blockDir, 'dir')
        mkdir(blockDir);
    else
        disp('ERROR: Block folder exists. Overwrite aborted.')
        return
    end

    % Load the Excel file
    filename = 'rootDesignMatrix.xlsx'; % Replace with your Excel file name
    sheet = 1; % Specify the sheet number if there are multiple sheets

    [num_data, txt_data, raw_data] = xlsread(filename, sheet);

    % Extract the header row
    header = raw_data(1, :);

    % Extract the first column
    first_column = raw_data(2:end, 1);

    % Remove the header row from the raw data
    raw_data(1, :) = [];
    raw_data(:, 15:end) = [];

    % Shuffle the remaining rows

    shuffled_indices = randperm(size(raw_data, 1));
    shuffled_data = raw_data(shuffled_indices, :);

    % Combine the header row and shuffled data
    shuffled_data_with_header = [header; shuffled_data];


    obj = {"Turtle" "Horse" "Car" "Shoe"};
    ori = {"Full Left" "Full Right" "Half Left" "Half Right"};

    
    [comb_objfirst, comb_orifirst] = tempperm(obj, ori);
    

    comb_objfirst(:, 9) = {'True'};
    comb_orifirst(:, 9) = {'False'};


    random_objfirst = comb_objfirst(randperm(size(comb_objfirst, 1), 32), :);
    random_orifirst = comb_orifirst(randperm(size(comb_orifirst, 1), 32), :);
    combined_responseSampled = [random_orifirst; random_objfirst];
    random_responseSampled = combined_responseSampled(randperm(size(combined_responseSampled, 1)), :);

     



    % Combine the header row and sampled data
    sampled_data_with_header = [header(5:13); random_responseSampled];
    
    shuffled_data_with_header(:,5:13) = sampled_data_with_header;

    sampled_and_shuffled_with_header = shuffled_data_with_header;
    

    % Create a new Excel file to store the shuffled data
    output_filename = fullfile(blockDir, sprintf('trialMatrix_s%s_%s.xlsx', participant, num2str(n)-1));




    
    % Generate 64 random numbers with a normal distribution around 2.5
    meanValue = 2.5;
    stdDeviation = 0.15; % You can adjust the standard deviation as needed
    randomNumbers = meanValue + stdDeviation * randn(1, 64);
    
    % Round the generated numbers to three decimal places
    roundedNumbers = round(randomNumbers, 3);
    
    % Create a cell array to store the data
    itidata = cell(65, 1);  % 65 rows (including the header) and 1 column
    itidata{1} = 'interval';  % Set the header
    
    for i = 1:64
        itidata{i+1} = roundedNumbers(i);
    end
    
    shuffled_data_with_header_ITI = [shuffled_data_with_header itidata];

    disp([block ' ITI distribution complete. ITI matrix saved.']);


    %%
    for s = 1 : height(shuffled_data_with_header_ITI)

        row = shuffled_data_with_header_ITI(s,:);

        if contains(row{3},'obj')
            if contains(row(4),row{1})
                corr = find(ismember(lower([row{5:12}]),row{1}));
                 if corr > 4
                     corr = corr - 4;
                 end
            end

            shuffled_data_with_header_ITI{s,14} = corr;


        elseif contains(row{3},'ori')

            if row{4}(end-4) == "1"
                optOri = "Full Left";

            elseif row{4}(end-4) == "2"     
                optOri = "Half Left";

            elseif row{4}(end-4) == "3"    
                optOri = "Half Right";

            elseif row{4}(end-4) == "4"    
                optOri = "Full Right";
            end
            
            corr = find(ismember([row{5:12}],optOri));

             if corr > 4
                 corr = corr - 4;
             end

             shuffled_data_with_header_ITI{s,14} = corr;

        end
    
    end








    %%    
    % Check if the output Excel file already exists
    if exist(output_filename, 'file') == 2
        error('The trial matrix Excel file already exists. Aborting compilation.');
    else
        try
            % Attempt to write data to the Excel file
            writecell(shuffled_data_with_header_ITI, output_filename);
            disp([block ' shuffling complete. Shuffled trials saved to "' output_filename '".']);
        catch
            error('Error writing data to Excel file.');
        end
    end
    

    %%
    % Calculate and display the average
    average = mean(roundedNumbers);
    fprintf('ITI average: %.3f\n', average);




end

    %% baby steps (self paced trainig trials

    
    % Sample 5 rows
    num_rows_to_sample = 8;
    num_total_rows = size(shuffled_data_with_header_ITI, 1);
    
    if num_rows_to_sample <= num_total_rows
        permuted_indices = randperm(num_total_rows);
        sampled_data = shuffled_data_with_header_ITI(permuted_indices(1:num_rows_to_sample), :);
        sampled_data_wHeader = [shuffled_data_with_header_ITI(1,:);sampled_data];
    else
        error('Number of rows to sample is greater than the total number of rows.');
    end
    


    output_baby = fullfile(dataDir, "block_0", sprintf('babySteps_s%s.xlsx',participant));


    % Save the sampled data to a new Excel file
    xlswrite(output_baby, sampled_data_wHeader, 'Sheet1');
    
    fprintf('\nbaby steps trials created.\n\n');






disp('Participant compiling complete.');

