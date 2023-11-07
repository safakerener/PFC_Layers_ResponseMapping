% Set the parameters
mean_value = 2.5;
std_deviation = 0.05; % Adjust the standard deviation as needed

% Generate 64 random numbers from a normal distribution
random_numbers = mean_value + std_deviation * randn(1, 64);

% Ensure the numbers are within the range [2, 3]
random_numbers(random_numbers < 2) = 2;
random_numbers(random_numbers > 3) = 3;

% Round the random numbers to 3 decimal places
random_numbers_rounded = round(random_numbers, 3);

% Calculate and display the average
average = mean(random_numbers_rounded);
disp('Generated Random Numbers:');
disp(random_numbers_rounded);
disp(['Average: ' num2str(average)]);
