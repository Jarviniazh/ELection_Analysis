''' Practice expected output:
1.Total number of votes cast
2. A complete list of candidates who received votes
3. Total number of votes each candidate received
4. Percentage of votes each candidate won
5. The winner of the election based on popular vote'''

# 1. Add our dependencies
import csv
# Open the csv file
import os

# 2.1 Assign a variable to load a file from path
file_to_load = os.path.join("Resources", "election_results.csv")

# 2.2 Assign and Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis","election_analysis.txt")

# 3. Initialize a total vote counter需要在打开文件前就默认初始总数为0，目的是保证每一次打开文件时总数都是0
total_vote = 0

# 6.2 Create Candidate Options，这个空list需要在打开文件前先建好，这样可以保证每次打开时都没有任何内容，所有之后list出现的东西都是提取文件后进行的添加
candidate_options = []

# 7.1 Declare the empty dictionary, 需要提前创建好空的字典，原理同上 
candidate_votes = {}

# 9.1 Winning candidate and winning count tracker 先创建好结果中所有的variable
winning_candidate = ""
winning_count = 0 
winning_percentage = 0

# 4.1 Open the election results
with open (file_to_load) as election_data:

# Using the open() function with the "w" mode we will write data to the file.
# outfile = open(file_to_save, "w")

# Refactoring: Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

# # Write some data to the file.
# 	txt_file.write("Counties in the Election \n")
# 	txt_file.write("---------------\n")
# 	txt_file.write("Arapahoe \nDenver \nJefferson")

# 4.2 Read the file object with the csv reader function,记得首行缩进
	file_reader = csv.reader(election_data)

# 4.3 Read and print the header row
	headers = next(file_reader) # next()会直接跳过第一行，从第二行开始
	
# print each row in the csv file
	for row in file_reader:
	# 	print(row)

	# 5.1 Add to the total vote count ----Requirement 1
		total_vote += 1

	# 6.1 Print the candidate name from each row. 这里row是一个新的命令，默认csv中每一行为一个list 
		candidate_name = row[2] # 注意还在for loop中，首行缩进
	
	# 6.3添加if条件确保每个名字只出现一次 
		if candidate_name not in candidate_options:
	
		# 6.4 Add candidate name to a list --- Requirement 2 当满足条件时添加名字进list
			candidate_options.append(candidate_name) #注意缩进
	
		# 7.2 Begin tracking that candidate's vote count. --- Requirement 3 在字典中添加内容，[key] = value
			candidate_votes[candidate_name] = 0 #因为有3个名字，所以系统会直接生成3个key

		# 7.3 Add a vote to that candidate's count
		candidate_votes[candidate_name] += 1 #不能在if条件里，不然只有名字不同时才会触发if条件，然后+1，而这里计数是需要考虑所有的row的，所以要放回for loop里和if同级

# 10.1 Save the results to our text file, 需要顶头
with open(file_to_save, "w") as txt_file:

	# 10.2 Print the final vote count to the terminal.
	election_results = (
		f"\nElection Results \n"
		f"-------------------------\n"
		f"Total Votes: {total_vote:,}\n"
		f"-------------------------\n")
	print(election_results, end = "")

	# 10.3 Save the final vote count to the text file
	txt_file.write(election_results)

# 8 Determine the percentage of votes for each candidate by looping through the counts ---- Requirement 4
# 8.1 iterate through the candidate list
	for candidate_name in candidate_votes:

	# 8.2 retrieve vote count of a candidate
		votes = candidate_votes[candidate_name]

	# 8.3 calculate the percentage votes
		vote_percentage = float(votes)/ float(total_vote) * 100

	# 8.4 print the candidate name and percentage of votes
	# print(f"{candidate_name}: received {vote_percentage:.2f}% of the vote.")
	
	# 9.3/10.4 print out each candidate's name, vote count, and percentage of votes to the terminal.
		candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
		print(candidate_results)

	# 10.5 Save the candidate results to our text file.
		txt_file.write(candidate_results)

	# 9.2 Determine if the votes are greater than the winning count.
		if votes > winning_count and vote_percentage > winning_percentage:
			winning_percentage = vote_percentage
			winning_count = votes
			winning_candidate = candidate_name

	
# 5.2 print the total votes
# print(total_vote)

# 6.5 print the candidate list
# print(candidate_options)

# 7.4 print candidate vote dictionary
# print(candidate_votes)

# 9.4 Create the winning candidate summary
	winning_candidate_summary = (
		f"-------------------------\n"
		f"Winner: {winning_candidate}\n"
		f"Winning Vote Count: {winning_count:,}\n"
		f"Winning Percentage: {winning_percentage:.1f}%\n"
		f"-------------------------\n")

# 9.5 print the summary
	print(winning_candidate_summary)

# 10.4 Save the winning candidate's results to the text file.
	txt_file.write(winning_candidate_summary)
