% participant compiler
% written by Safak Erener (safakerener@gmail.com)
% date 26.09.2023

% change to stim directory
% cd('C:\Users\dell\Dropbox\My PC (Safi)\Desktop\PFC\PFC_V1_consciousness_HiRes\test exp\scripts_and_stim')
% cd('C:\Users\erene\OneDrive\Desktop\PFC\PFC_V1_consciousness_HiRes\test exp\scripts_and_stim')

cd('C:\Users\willi\Desktop\PFC_Layers\PFC_Layers_ResponseMapping\Pilot')

% Create a GUI for entering the participant number

prompt = {'Enter Participant Number:', 'Number of Blocks:'};
dlgtitle = 'Input Values';
definput = {'', '6'}; % Default value
dims = [1 50];


inputValues = inputdlg(prompt, dlgtitle, dims, definput);

if isempty(inputValues)
    return; % User canceled the input
end

folderName = 'designMatrices';

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
dataDir = fullfile('participantData', sprintf('s%s', participant));

if ~exist(dataDir, 'dir')
    mkdir(dataDir);
end



% % Create headers and data for the new Excel file
% blockNumbers = (1:numBlocks)';
% designMatrixPaths = cell(numBlocks, 1);
% 
% for n = 1:numBlocks
%     block = sprintf('block_%s', num2str(n));
%     designMatrixPaths{n} = fullfile(dataDir, block, sprintf('designMatrix_%s_s%s.xlsx', num2str(n), participant));
% end
% 
% data = table(blockNumbers, designMatrixPaths, 'VariableNames', {'blockNumber', 'designMatrixPath'});
% 
% % Save the data as an Excel file in the subject folder
% outputFilename = fullfile(dataDir, 'blockData.xlsx');
% writetable(data, outputFilename);
% 
% disp(['Subject data saved to ' outputFilename]);





for n = 1:numBlocks
    

    block = sprintf('block_%s', num2str(n));

    % Create a directory for each block within the participant's folder
    blockDir = fullfile(dataDir, block); % Modify as needed

    if ~exist(blockDir, 'dir')
        mkdir(blockDir);
    else
        disp('ERROR: Participant folder exists. Overwrite aborted.')
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
    raw_data(:, 5:end) = [];
    
    % Shuffle the remaining rows
    rng('shuffle'); % Seed the random number generator with current time
    shuffled_indices = randperm(size(raw_data, 1));
    shuffled_data = raw_data(shuffled_indices, :);
    
    
    % Combine the header row and shuffled data
    shuffled_data_with_header = [header; shuffled_data];

    
    % Create a new Excel file to store the shuffled data
    output_filename = fullfile('designMatrices', sprintf('designMatrix_s%s_%s.xlsx',participant, num2str(n) ));
    % Check if the output Excel file already exists
    if exist(output_filename, 'file') == 2
        error('The design matrix Excel file already exists. Aborting compilation.');
    else
        try
            % Attempt to write data to the Excel file
            writecell(shuffled_data_with_header,output_filename);
            disp([block ' shuffling complete. Shuffled trials saved to "' output_filename '".']);
        catch
            error('Error writing data to Excel file.');
        end
    end

end

    disp('Participant compiling complete.')
