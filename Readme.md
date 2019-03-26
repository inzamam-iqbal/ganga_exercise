# ganga_exercise

## Exercise one

### Running  
This project uses,
* PyPDF2 to split the pdf into pages.  
  PyPDF2 can be installed using `pip install PyPDF2`

* I have used textract to read pdf files.   
  The installation instruction for textract can be found [here](https://textract.readthedocs.io/en/stable/installation.html)

Now to run the Job simply run the command
```
ganga gangaJob.py
```

### Testing the Job
* Get the job id of the created job.  
* Run the command
```
ganga testJob.py <job_id>
```
### Files related to Exercise 1
#### gangaJob.py

* This file contains functions to split the CERN.pdf file to individual pages and save them as pdfs in
"pages" folder (which get created in the process). While doing that process it appends the relative path
of each file it creates to the args list to be used by ArgSplitter.   

* The getFiles method provides the list of LocalFile objects created using the files in the "pages" folder.   

* The file first calls the splitPdf function   
* Then it creates the Job using the following code.   

```python
j=Job(name='Ex1')
j.application.exe = File('theCounter.py')
j.inputfiles = getFiles()
j.splitter=ArgSplitter(args=args)
j.outputfiles = [ LocalFile('answer.txt') ]
j.postprocessors=CustomMerger(files=['answer.txt'],module=File('intAdderMerger.py'))
j.submit()
```

* Here I use ArgSplitter to split the task among sub processes such that each subProcess counts the occurrence of
the word "the" in one file.
* Each subProcess creates an answer.txt file in its corresponding output directory which contains the "the" count
of its corresponding file
* Then I use a customMerger to sum up all the values in the answer.txt files and to create a 'answer.txt' file in the
output directory of main job.

#### theCounter.py

* This is the file each sub-process calls with their argument.
* Initially it checks whether there are at least two arguments passed
* Then it opens the pdf file which is passed as argument with the help of "textract" library and counts the occurrence of
the word "the" using regex.
* Then it writes the count to answer.txt file

#### intAdderMerger.py

* This file provides the function `mergefiles(file_list,output_file)` which custom merger looks for.
* This iterate through input files and sum up the values in each file and write the final value to the output file.
* Finally returns True to indicate success.

#### testJob.py

* This takes job_id as a argument and fetches the job using jobs[job_id].
* Then it gets the output directory of that particular job to read the answer.txt file
* Then it uses getCount defined within the file to get the "the" count of the entire CERN.pdf file.
* Then it asserts that both values need to be same.

## Exercise two
### Running the docker container directly
```
sudo docker run inzamamiqbal/ganga_exercise:1.1
```
### Running the docker container using ganga Job
```shell
ganga runDockerJob.py <docker image name> <sudo password>

#To run the container created for exercise 2
ganga runDockerJob.py inzamamiqbal/ganga_exercise:1.1 <sudo password>
```

### Files related to exercise 2

#### DockerFile
* This file defines all the instructions to create the docker Image which runs the job created in exercise one when the
docker instance starts.
* Commands in DockerFile are well commented.

#### runDockerJob.py
* Recieves 2 explicite arguments from user:   
  * Docker image name
  * sudo password
* Runs the Job with runDockerCommand.sh as application.exe and passes both arguments to the shell script

#### runDockerCommand.sh
* Runs the docker run command.

