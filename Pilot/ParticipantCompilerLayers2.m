% written by Safak Erener (safakerener@gmail.com)
% date 26.09.2023

% Change to the desired working directory
%cd('C:\Users\willi\Desktop\PFC_Layers\PFC_Layers_ResponseMapping\Pilot')

cd('C:\Users\erene\OneDrive\Desktop\PFC Layers\PFC_Layers_ResponseMapping\Pilot')

% Create a GUI for entering the participant number and number of blocks
prompt = {'Enter Participant Number:', 'Number of Blocks:'};
dlgtitle = 'Input Values';
definput = {'', '6'}; % Default values
dims = [1 50];
inputValues = inputdlg(prompt, dlgtitle, dims, definput);

if isempty(inputValues)
    return; % User canceled the input
end

folderName = 'trialMatrices';

% Check if the folder already exists
if ~isfolder(folderName)
    % Create the folder
    mkdir(folderName);
    disp(['Folder "', folderName, '" has been created.']);
else
    disp(['Folder "', folderName, '" already exists.']);
end

participant = inputValues{1};
numBlocks = str2double(inputValues{2});

% Create a directory in the "participantData" folder based on the participant number
% dataDir = fullfile('participantData', sprintf('s%s', participant));

% if ~exist(dataDir, 'dir')
%     mkdir(dataDir);
% end

for n = 1:numBlocks
    block = sprintf('block_%s', num2str(n));

    % Create a directory for each block within the participant's folder
    % blockDir = fullfile(dataDir, block);

    % if ~exist(blockDir, 'dir')
    %     mkdir(blockDir);
    % else
    %     disp('ERROR: Participant folder exists. Overwrite aborted.')
    %     return
    % end

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
    raw_data(:, 13:end) = [];

    % Shuffle the remaining rows
    rng('shuffle'); % Seed the random number generator with current time
    shuffled_indices = randperm(size(raw_data, 1));
    shuffled_data = raw_data(shuffled_indices, :);

    % Combine the header row and shuffled data
    shuffled_data_with_header = [header; shuffled_data];

    % Load the permutations data from your Excel file
    permutations_filename = 'permutations.xlsx'; % Replace with the actual path to your Excel file
    sheet_name = 'Permutations'; % Modify the sheet name if needed
    raw_data_perm = readcell(permutations_filename);
    
    % Randomly sample 96 rows from the permutations data
    sample_size = 96; % Modify the sample size as needed
    num_permutations = size(raw_data_perm, 1);
    
    if num_permutations < sample_size
        error('Not enough permutations in the Excel file.');
    end
    
    sample_indices = randperm(num_permutations, sample_size);
    sampled_data = raw_data_perm(sample_indices, :);
    
    % Combine the header row and sampled data
    sampled_data_with_header = [header(5:end); sampled_data];
    
    shuffled_data_with_header(:,5:12) = sampled_data_with_header;

    sampled_and_shuffled_with_header = shuffled_data_with_header;
    

    % Create a new Excel file to store the shuffled data
    output_filename = fullfile('trialMatrices', sprintf('trialMatrix_s%s_%s.xlsx', participant, num2str(n)));

    % Check if the output Excel file already exists
    if exist(output_filename, 'file') == 2
        error('The trial matrix Excel file already exists. Aborting compilation.');
    else
        try
            % Attempt to write data to the Excel file
            writecell(shuffled_data_with_header, output_filename);
            disp([block ' shuffling complete. Shuffled trials saved to "' output_filename '".']);
        catch
            error('Error writing data to Excel file.');
        end
    end
end

disp('Participant compiling complete.');
